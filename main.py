#
# Author: Jose Cerrejon
# Email: contact at ulysess_.gmail_com
# License: MIT
#
import os
import signal
import sys
import typing

from src.ai import AI
from src.helpers.dot_env_loader import DotenvLoader
from src.helpers.utils import Utils

DotenvLoader.load(".env")
APP_VERSION = "1.1.ABC"
BYE_MESSAGE = "\nBye! I hope I was helpful! Bzzz 🪰"
DEFAULT_LIBRARY = "openai"


def print_header() -> None:
    print(Utils.get_header_message(APP_VERSION))


def signal_handler(sig: int, frame: typing.Any) -> None:
    print(BYE_MESSAGE)
    sys.exit(0)


if __name__ == "__main__":
    ai = AI(os.environ.get("USE_LIBRARY", DEFAULT_LIBRARY))

    signal.signal(signal.SIGINT, signal_handler)
    print_header()

    while True:
        prompt = input("\nBuzZ: ")

        if prompt == "exit":
            print(BYE_MESSAGE)
            break

        response = ai.answer(prompt) if prompt != "imagine" else ai.draw()  # type: ignore
        print(response)
