import os
import subprocess
from dataclasses import dataclass, field
from typing import Any, Dict

import src.helpers.utils
from src.helpers.utils import Utils
from src.models.interfaces import Answerable, Drawable

try:
    Utils.create_virtualenv()
    import openai
except ImportError:
    print("Installing the openai library...", sep="")
    subprocess.run(
        ["pip", "install", "openai"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("Done!\n")
from openai import OpenAI as OpenAIClient


@dataclass(frozen=True)
class AIConstants:
    DEFAULT_QUALITY: str = "standard"
    DEFAULT_SIZE: str = "1024x1024"
    DEFAULT_TEMPERATURE: int = 0
    DEFAULT_N: int = 1

    TEXT_MODEL: Dict[str, Any] = field(
        default_factory=lambda: {
            "model_name": os.environ.get("MODEL_NAME"),
            "temperature": AIConstants.DEFAULT_TEMPERATURE,
        }
    )

    IMAGE_MODEL: Dict[str, Any] = field(
        default_factory=lambda: {
            "model_name": "dall-e-3",
            "size": AIConstants.DEFAULT_SIZE,
            "quality": AIConstants.DEFAULT_QUALITY,
            "n": AIConstants.DEFAULT_N,
        }
    )


class OpenAI(Drawable, Answerable):
    def __init__(self) -> None:
        self.constants = AIConstants()
        self.client = OpenAIClient(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model_type: Dict[str, Dict[str, Any]] = {
            "text": self.constants.TEXT_MODEL,
            "image": self.constants.IMAGE_MODEL,
        }
        src.helpers.utils.additional_header_message = "Type: imagine + [Enter] to get a prompt and make an image about something you want."

    def draw(self) -> str:
        print("\nYou want a picture!")
        prompt = input("\nImagine... ")

        if prompt == "exit":
            print("\nBye! I hope I was helpful!")
            exit()

        print("\nLet me draw something about that...\n")
        answer = self.client.images.generate(
            model=self.model_type.get("image", {}).get("model_name"),
            prompt=prompt,
            size=self.model_type.get("image", {}).get("size"),
            quality=self.model_type.get("image", {}).get("quality"),  # type: ignore
            n=self.model_type.get("image", {}).get("n"),
        )
        url = answer.data[0].url
        if url is None or not url.startswith("http"):
            return ""

        Utils.open_default_browser(url)

        return url

    def answer(self, input: str) -> str:
        prompt = f"""
        Input: {input}
        
        Based on the above information, answer the input with humor (you are a millions of flies).
        """

        response = self.client.chat.completions.create(
            model=self.model_type.get("text", {}).get("model_name"),  # type: ignore
            messages=[{
                "role": "system",
                "content": Utils.get_message_content(),
            }, {
                "role": "user",
                "content": prompt
            }],
            temperature=self.model_type.get("text", {}).get("temperature"),
        )
        content = response.choices[0].message.content
        if content is None:
            return "Sorry, I couldn't come up with a humorous response."

        return content.strip()

    def __repr__(self) -> str:
        return str(f"({__name__}) parameters: {self.model_type}")
