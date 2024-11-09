import unittest
from unittest.mock import patch

from src.helpers.utils import Utils


class TestUtils(unittest.TestCase):
    @patch("webbrowser.open")
    def test_open_default_browser(self, mock_open: unittest.mock.Mock) -> None:
        url = "http://example.com"
        Utils.open_default_browser(url)
        mock_open.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
