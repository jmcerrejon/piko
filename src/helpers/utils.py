import os
import subprocess
import sys

additional_header_message = ""


class Utils:
    """
    A utility class providing various helper methods.
    Methods:
        open_default_browser(url: str) -> None:
        create_virtualenv() -> None:
        get_header_message(app_version: str) -> str:
            Generate a header message with the given application version.
    """

    __DEFAULT_LOCALE = "en_US"

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
            activate_script = (
                ".venv/bin/activate" if os.name != "nt" else ".venv\\Scripts\\activate"
            )

            print("Virtual environment not detected.\nCreating virtual environment...")
            subprocess.check_call([sys.executable, "-m", "venv", ".venv"])

            print(
                f"Now activate the environment with the command: source {activate_script} and run It again."
            )
            exit(0)

    @staticmethod
    def get_header_message(app_version: str) -> str:
        """
        Generate a header message with the given application version.
        """

        return f"""
    d8888b. d888888b db   dD  .d88b.  
    88  `8D   `88'   88 ,8P' .8P  Y8. 
    88oodD'    88    88,8P   88    88 
    88~~~      88    88`8b   88    88 
    88        .88.   88 `88. `8b  d8' 
    88      Y888888P YP   YD  `Y88P'  

Version: {app_version}

Hi! I'm PIKO!. 🪰

The new AI created from the collective mind of trillons of flies.

I'm going to answer your questions using your language ({Utils.get_locale()}). You can use it, too!

Type [exit] to exit the program. {additional_header_message}
"""

    @staticmethod
    def get_locale() -> str:
        """
        Get the locale of the system.

        Returns:
            str: The locale of the system.
        """
        import locale

        return str(locale.getlocale()[0] or Utils.__DEFAULT_LOCALE)

    @staticmethod
    def get_message_content() -> str:
        """
        Get the message content from the response for the AI.

        Returns:
            str: The message content.
        """

        return f"You are an AI assistant tasked with answering with humor. Use {Utils.get_locale()} as output language."
