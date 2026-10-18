"""Unit tests for the read-only registry consistency validator."""
from pathlib import Path
import tempfile
import unittest

from tools.registry_validator import validate


MAI_WITH_ENTRIES = """# MAI-001
| SIOS-BASELINE-001 | Frozen 1.1.0 |
| KOM-001 | Approved 0.2.0 |
"""
EMPTY_CLAIM = "# Registry\n\n**Status:** No artifacts currently registered.\n"


class RegistryValidatorTests(unittest.TestCase):
    def write(self, root: Path, relative: str, content: str) -> None:
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def test_detects_explicit_maI_secondary_registry_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "01-Foundation/Registry/MAI-001.md", MAI_WITH_ENTRIES)
            self.write(root, "12-Registry/README.md", EMPTY_CLAIM)

            findings = validate(root)

            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].code, "MAI_REGISTRY_CONFLICT")
            self.assertIn("no source is automatically preferred", findings[0].message)

    def test_passes_when_secondary_registry_does_not_claim_empty(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "01-Foundation/Registry/MAI-001.md", MAI_WITH_ENTRIES)
            self.write(root, "12-Registry/README.md", "# Registry\n\nStatus under review.\n")

            self.assertEqual(validate(root), [])

    def test_reports_missing_master_index(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            findings = validate(Path(directory))

            self.assertEqual(len(findings), 1)
            self.assertEqual(findings[0].code, "MAI_MISSING")

    def test_does_not_modify_workspace_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            mai = root / "01-Foundation/Registry/MAI-001.md"
            secondary = root / "12-Registry/README.md"
            self.write(root, mai.relative_to(root).as_posix(), MAI_WITH_ENTRIES)
            self.write(root, secondary.relative_to(root).as_posix(), EMPTY_CLAIM)
            before = (mai.read_bytes(), secondary.read_bytes())

            validate(root)

            self.assertEqual((mai.read_bytes(), secondary.read_bytes()), before)


if __name__ == "__main__":
    unittest.main()
