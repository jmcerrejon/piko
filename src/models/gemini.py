import os
from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass(frozen=True)
class AIConstants:
    DEFAULT_QUALITY: str = "standard"
    DEFAULT_SIZE: str = "1024x1024"
    DEFAULT_TEMPERATURE: int = 0
    DEFAULT_N: int = 1

    TEXT_MODEL: Dict[str, Any] = field(
        default_factory=lambda: {
            "model_name": "gpt-4o-mini",
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


class Gemini:
    def __init__(self) -> None:
        self.constants = AIConstants()
        self.client = GeminiClient(api_key=os.environ.get("GEMINI_API_KEY"))
        self.model_type: Dict[str, Dict[str, Any]] = {
            "text": self.constants.TEXT_MODEL,
            "image": self.constants.IMAGE_MODEL,
        }

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
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant tasked with answering with humor.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=self.model_type.get("text", {}).get("temperature"),
        )
        content = response.choices[0].message.content
        if content is None:
            return "Sorry, I couldn't come up with a humorous response."

        return content.strip()

    def __repr__(self) -> str:
        return str(f"({__name__}) parameters: {self.model_type}")
