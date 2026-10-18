import unittest

from scripts.validate_gdr_oai import validate_package


class GdrOaiMigrationValidationTests(unittest.TestCase):
    def test_staged_package_satisfies_schemas_and_cross_references(self):
        self.assertEqual([], validate_package())


if __name__ == "__main__":
    unittest.main()
