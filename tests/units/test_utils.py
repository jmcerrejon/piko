import sys
import unittest
from unittest.mock import patch

from src.helpers.utils import Utils


class TestUtils(unittest.TestCase):
    @patch("webbrowser.open")
    def test_open_default_browser(self, mock_open: unittest.mock.Mock) -> None:
        url = "http://example.com"
        Utils.open_default_browser(url)
        mock_open.assert_called_once_with(url)

    @patch("os.getenv", return_value=None)
    @patch("subprocess.check_call")
    @patch("builtins.exit")
    def test_create_virtualenv(
        self,
        mock_exit: unittest.mock.Mock,
        mock_check_call: unittest.mock.Mock,
        mock_getenv: unittest.mock.Mock,
    ) -> None:
        Utils.create_virtualenv()
        mock_getenv.assert_called_once_with("VIRTUAL_ENV")
        mock_check_call.assert_called_once_with([sys.executable, "-m", "venv", ".venv"])
        mock_exit.assert_called_once_with(0)


if __name__ == "__main__":
    unittest.main()
