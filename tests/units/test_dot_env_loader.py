import os
import unittest
from unittest.mock import mock_open, patch

from src.helpers.dot_env_loader import DotenvLoader


class TestDotenvLoader(unittest.TestCase):
    @patch(
        "builtins.open", new_callable=mock_open, read_data="OPENAI_API_KEY=TEST_VALUE\n"
    )
    @patch("pathlib.Path.exists", return_value=True)
    def test_load_valid_file(
        self, mock_exists: unittest.mock.Mock, mock_open: unittest.mock.Mock
    ) -> None:
        DotenvLoader.load(".env")
        self.assertEqual(os.environ.get("OPENAI_API_KEY"), "TEST_VALUE")

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="# Comment line\nOPENAI_API_KEY=TEST_VALUE\n",
    )
    @patch("pathlib.Path.exists", return_value=True)
    def test_load_file_with_comments(
        self, mock_exists: unittest.mock.Mock, mock_open: unittest.mock.Mock
    ) -> None:
        DotenvLoader.load(".env")
        self.assertEqual(os.environ.get("OPENAI_API_KEY"), "TEST_VALUE")

    @patch("pathlib.Path.exists", return_value=False)
    @patch("builtins.exit")
    def test_load_nonexistent_file(
        self, mock_exit: unittest.mock.Mock, mock_exists: unittest.mock.Mock
    ) -> None:
        DotenvLoader.load(".env")
        mock_exit.assert_called_once_with(0)


if __name__ == "__main__":
    unittest.main()
