import os
import subprocess
from dataclasses import dataclass, field
from typing import Any, Dict

from src.helpers.utils import Utils
from src.models.interfaces import Answerable

try:
    Utils.create_virtualenv()
    import google.generativeai  # noqa: F401
except ImportError:
    print("Installing the google-generativeai library...", sep="")
    subprocess.run(
        ["pip", "install", "google-generativeai"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("Done!\n")
import google.generativeai as genai


@dataclass(frozen=True)
class AIConstants:
    DEFAULT_QUALITY: str = "standard"
    DEFAULT_SIZE: str = "1024x1024"
    DEFAULT_TEMPERATURE: int = 0
    DEFAULT_N: int = 1

    TEXT_MODEL: Dict[str, Any] = field(
        default_factory=lambda: {
            "model_name": "gemini-1.5-flash",
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


class Gemini(Answerable):
    def __init__(self) -> None:
        self.constants = AIConstants()
        self.client = genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        self.model_type: Dict[str, Dict[str, Any]] = {
            "text": self.constants.TEXT_MODEL,
            "image": self.constants.IMAGE_MODEL,
        }

    def draw(self) -> str:
        return f"Sorry, I can't draw images with {self.__class__.__name__} yet."

    def answer(self, input: str) -> str:
        prompt = f"""
        Input: {input}
        
        Based on the above information, answer the input with humor (you are a millions of flies).
        """

        model = genai.GenerativeModel(self.model_type.get("text", {}).get("model_name"))
        response = model.generate_content(
            ["You are an AI assistant tasked with answering with humor.", prompt]
        )

        content = str(response.text)
        if content is None:
            return "Sorry, I couldn't come up with a humorous response."

        return content.strip()

    def __repr__(self) -> str:
        return str(f"({__name__}) parameters: {self.model_type}")
