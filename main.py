#
# Author: Jose Cerrejon
# Email: contact at ulysess_.gmail_com
# License: MIT
#
import signal
import sys
import typing

from src.ai import AI
from src.helpers.dot_env_loader import DotenvLoader

DotenvLoader.load(".env")
APP_VERSION = "0.3.STV"
_BYE_MESSAGE = "\nBye! I hope I was helpful! Bzzz 🪰"


def print_header() -> None:
    print(f"""
    d8888b. d888888b db   dD  .d88b.  
    88  `8D   `88'   88 ,8P' .8P  Y8. 
    88oodD'    88    88,8P   88    88 
    88~~~      88    88`8b   88    88 
    88        .88.   88 `88. `8b  d8' 
    88      Y888888P YP   YD  `Y88P'  

    Version: {APP_VERSION}

Hi! I'm PIKO!. 🪰

The new AI created from the collective mind of trillons of flies.

Type [exit] to exit the program or [imagine] to get a picture about something you want.
""")


def signal_handler(sig: int, frame: typing.Any) -> None:
    print(_BYE_MESSAGE)
    sys.exit(0)


if __name__ == "__main__":
    ai = AI()

    signal.signal(signal.SIGINT, signal_handler)
    print_header()

    while True:
        prompt = input("\nBuzZ: ")

        if prompt == "exit":
            print(_BYE_MESSAGE)
            break

        response = ai.answer(prompt) if prompt != "imagine" else ai.draw()
        print(response)
