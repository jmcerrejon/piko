import os
import subprocess
import sys


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

    @staticmethod
    def create_virtualenv() -> None:
        """
        Creates and activates a virtual environment if one is not already active.
        This function checks if a virtual environment is currently active by
        inspecting the 'VIRTUAL_ENV' environment variable. If no virtual
        environment is detected, it creates a new one using the '.venv' module.
        
        Returns:
            None
        """
        if os.getenv("VIRTUAL_ENV") is None:
            activate_script = ".venv/bin/activate" if os.name != "nt" else ".venv\\Scripts\\activate"

            print("Virtual environment not detected.\nCreating virtual environment...")
            subprocess.check_call([sys.executable, "-m", "venv", ".venv"])
            
            print(f"Now activate the environment with the command: source {activate_script} and run It again.")
            exit(0)
