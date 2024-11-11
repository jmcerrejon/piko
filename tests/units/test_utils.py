import locale
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

    def test_get_header_message(self) -> None:
        app_version = "1.0.0"
        header = Utils.get_header_message(app_version)
        self.assertIn(f"Version: {app_version}", header)

    @patch("locale.getdefaultlocale", return_value=("en_US", "UTF-8"))
    def test_get_locale(self, mock_getdefaultlocale: unittest.mock.Mock) -> None:
        locale = Utils.get_locale()
        self.assertEqual(locale, "en_US")

    @patch("src.helpers.utils.Utils.get_locale", return_value="en_US")
    def test_get_message_content(self, mock_get_locale: unittest.mock.Mock) -> None:
        message = Utils.get_message_content()
        get_locale = locale.getlocale()[0]
        expected_message = (
            "You are an AI assistant tasked with answering with humor. "
            f"Use {get_locale} as output language."
        )
        self.assertEqual(message, expected_message)


if __name__ == "__main__":
    unittest.main()
