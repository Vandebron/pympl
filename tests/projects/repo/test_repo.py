import unittest

from pyaml_env import parse_config

from src.pympl.repo import RepoConfig
from src.pympl.repo import Repository

from tests import root_test_path


class RepoTestCase(unittest.TestCase):
    resource_path = root_test_path / "test_resources"

    @unittest.skip("FIXME: main is not available in github action")
    def test_changes_in_commit_should_be_in_branch(self):
        repo = Repository(RepoConfig({'cvs': {'git': 'main_branch'}}))
        changes_in_branch = repo.changes_in_branch()
        changes_in_commit = repo.changes_in_commit()

        self.assertTrue(changes_in_commit.issubset(changes_in_branch))

    def test_load_config(self):
        yaml_values = parse_config(self.resource_path / "config.yml")
        config = RepoConfig(yaml_values)
        self.assertEqual(config.main_branch, 'main')


if __name__ == '__main__':
    unittest.main()
