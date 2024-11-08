class Utils:
    @staticmethod
    def open_default_browser(url):
        """
        Open the specified URL in the default web browser.

        Args:
            url (str): The URL to be opened in the web browser.

        Returns:
            None
        """
        import webbrowser

        webbrowser.open(url)
