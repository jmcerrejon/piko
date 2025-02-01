#
# Author: Jose Cerrejon
# Email: contact at ulysess_.gmail_com
# License: MIT
#
import os
import signal
import sys
import typing
import unicodedata

from src.ai import AI
from src.helpers.dot_env_loader import DotenvLoader
from src.helpers.utils import Utils

DotenvLoader.load(".env")
APP_VERSION = "1.2.DEF"
BYE_MESSAGE = "\nBye! I hope I was helpful! Bzzz 🪰"
DEFAULT_LIBRARY = "openai"
MAX_INPUT_LENGTH = 255


def print_header() -> None:
    print(Utils.get_header_message(APP_VERSION))


def signal_handler(sig: int, frame: typing.Any) -> None:
    print(BYE_MESSAGE)
    sys.exit(0)


def normalize_text(text: str) -> str:
    return unicodedata.normalize("NFKC", text)


if __name__ == "__main__":
    ai = AI(os.environ.get("USE_LIBRARY", DEFAULT_LIBRARY))

    signal.signal(signal.SIGINT, signal_handler)
    print_header()

    while (prompt := input("\nBuzz: ")) != "exit":
        if len(prompt) > MAX_INPUT_LENGTH:
            raise ValueError("Input exceeds maximum allowed length.")
        response = (
            ai.answer(normalize_text(prompt)) if prompt != "imagine" else ai.draw()
        )  # type: ignore
        print(response)
    print(BYE_MESSAGE)
