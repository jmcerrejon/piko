import os
import subprocess
from dataclasses import dataclass, field
from typing import Any, Dict

from src.helpers.utils import Utils
from src.models.interfaces import Answerable

try:
    Utils.create_virtualenv()
    import ollama
except ImportError:
    print("Installing the ollama library...", sep="")
    subprocess.run(
        ["pip", "install", "ollama"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("Done!\n")
from ollama import ChatResponse, chat


@dataclass(frozen=True)
class AIConstants:
    DEFAULT_TEMPERATURE: int = 0
    DEFAULT_N: int = 1

    TEXT_MODEL: Dict[str, Any] = field(
        default_factory=lambda: {
            "model_name": os.environ.get("MODEL_NAME"),
            "temperature": AIConstants.DEFAULT_TEMPERATURE,
        }
    )

class Ollama(Answerable):
    def __init__(self) -> None:
        self.constants = AIConstants()
        self.model_type: Dict[str, Dict[str, Any]] = {
            "text": self.constants.TEXT_MODEL,
        }

    def answer(self, input: str) -> str:
        prompt = f"""
        Input: {input}
        
        Show the result, and then use a joke.
        """

        response: ChatResponse = chat(model=self.constants.TEXT_MODEL["model_name"], messages=[{
            "role": "system",
            "content": Utils.get_message_content(),
        }, {
            "role": "user",
            "content": prompt
        }])
        content = response['message']['content']
        if content is None:
            return "Sorry, I couldn't come up with a humorous response."

        return str(content).strip()

    def __repr__(self) -> str:
        return str(f"({__name__}) parameters: {self.model_type}")