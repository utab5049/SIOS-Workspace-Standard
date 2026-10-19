"""Inspect and summarize local SIOS workflow execution history."""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any


class HistoryReadError(ValueError):
    """Raised when history cannot be read or contains invalid JSONL records."""


def _parse_timestamp(value: str, label: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise HistoryReadError(f"{label} must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise HistoryReadError(f"{label} must include a timezone")
    return parsed


def load_history(path: Path) -> list[dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise HistoryReadError(f"could not read history file: {exc}") from exc
    entries: list[dict[str, Any]] = []
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise HistoryReadError(f"invalid JSON on line {line_number}: {exc.msg}") from exc
        if not isinstance(value, dict):
            raise HistoryReadError(f"history line {line_number} must contain a JSON object")
        for field in ("run_id", "timestamp", "status"):
            if not isinstance(value.get(field), str) or not value[field].strip():
                raise HistoryReadError(f"history line {line_number} requires a non-empty {field}")
        _parse_timestamp(value["timestamp"], f"timestamp on line {line_number}")
        entries.append(value)
    return entries


def inspect_history(
    entries: list[dict[str, Any]],
    *,
    run_id: str | None = None,
    status: str | None = None,
    since: datetime | None = None,
    until: datetime | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    filtered = []
    for entry in entries:
        timestamp = _parse_timestamp(entry["timestamp"], "history timestamp")
        if run_id is not None and entry["run_id"] != run_id:
            continue
        if status is not None and entry["status"] != status:
            continue
        if since is not None and timestamp < since:
            continue
        if until is not None and timestamp > until:
            continue
        filtered.append(entry)
    filtered.sort(key=lambda entry: _parse_timestamp(entry["timestamp"], "history timestamp"), reverse=True)
    total_matching = len(filtered)
    if limit is not None:
        filtered = filtered[:limit]
    statuses = Counter(entry["status"] for entry in filtered)
    durations = [entry["duration_ms"] for entry in filtered if isinstance(entry.get("duration_ms"), (int, float))]
    return {
        "history_schema_version": "1.0",
        "matched_runs": total_matching,
        "returned_runs": len(filtered),
        "status_counts": dict(sorted(statuses.items())),
        "average_duration_ms": round(sum(durations) / len(durations), 3) if durations else None,
        "runs": filtered,
    }


def _print_text(result: dict[str, Any]) -> None:
    print(f"Matched runs: {result['matched_runs']} (showing {result['returned_runs']})")
    print("Status counts: " + (", ".join(f"{key}={value}" for key, value in result["status_counts"].items()) or "none"))
    average = result["average_duration_ms"]
    print(f"Average duration: {average} ms" if average is not None else "Average duration: n/a")
    if not result["runs"]:
        print("No matching runs.")
        return
    print()
    print("TIMESTAMP | STATUS | WORKFLOW | OPERATION | RUN ID")
    for entry in result["runs"]:
        operation = entry.get("operation_type") or "-"
        workflow = entry.get("workflow_id") or "-"
        print(f"{entry['timestamp']} | {entry['status']} | {workflow} | {operation} | {entry['run_id']}")
        if entry.get("error"):
            print(f"  error: {entry['error']}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect local SIOS workflow execution history (JSONL).")
    parser.add_argument("history", type=Path, help="path to history JSONL file")
    parser.add_argument("--run-id", help="show one exact run ID")
    parser.add_argument("--status", help="filter by exact status, e.g. completed, blocked, error")
    parser.add_argument("--since", help="include runs at or after an ISO-8601 timestamp with timezone")
    parser.add_argument("--until", help="include runs at or before an ISO-8601 timestamp with timezone")
    parser.add_argument("--limit", type=int, help="maximum number of newest matching runs to display")
    parser.add_argument("--json", action="store_true", help="print the full filtered summary as JSON")
    args = parser.parse_args(argv)
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    try:
        since = _parse_timestamp(args.since, "--since") if args.since else None
        until = _parse_timestamp(args.until, "--until") if args.until else None
        if since and until and since > until:
            raise HistoryReadError("--since must not be later than --until")
        entries = load_history(args.history)
        result = inspect_history(entries, run_id=args.run_id, status=args.status, since=since, until=until, limit=args.limit)
    except HistoryReadError as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        _print_text(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
