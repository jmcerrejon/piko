#
# Author: Jose Cerrejon
# Email: contact at ulysess_.gmail_com
# License: MIT
#
import os

from openai import OpenAI

from src.helper.dot_env_loader import DotenvLoader
from src.helper.utils import Utils

DotenvLoader.load(".env")
APP_VERSION = "0.2.QRS"
MODEL_NAME = {"text": "gpt-4o-mini", "image": "dall-e-3"}

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def print_header():
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


def draw() -> str:
    print("\nYou want a picture!")
    prompt = input("\nImagine... ")

    if prompt == "exit":
        print("\nBye! I hope I was helpful!")
        exit()

    print("\nLet me draw something about that...\n")
    answer = client.images.generate(
        model=MODEL_NAME["image"],
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    url = answer.data[0].url
    Utils.open_default_browser(url)

    return url


def answer(input) -> str:
    prompt = f"""
    Input: {input}
    
    Based on the above information, answer the input with humor (you are a millions of flies).
    """

    response = client.chat.completions.create(
        model=MODEL_NAME["text"],
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant tasked with answering with hummor.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    print("\nLet me think about that...")

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print_header()

    while True:
        prompt = input("\nBuzZ: ")

        if prompt == "exit":
            print("\nBye! I hope I was helpful! Bzzz 🪰")
            break

        response = answer(prompt) if prompt != "imagine" else draw()
        print(response)
