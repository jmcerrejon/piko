class Utils:
    """
    A utility class that provides various helper methods.
    Methods:
        open_default_browser(url: str) -> None:
    """

    @staticmethod
    def open_default_browser(url: str) -> None:
        """
        Open the specified URL in the default web browser.

        Args:
            url (str): The URL to be opened in the web browser.

        Returns:
            None
        """
        import webbrowser

        webbrowser.open(url)
