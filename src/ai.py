from src.models.gemini import Gemini
from src.models.openai import OpenAI


class AI:
    def __new__(cls, model_name: str = "openai", *args, **kwargs):
        if model_name == "openai":
            return OpenAI(*args, **kwargs)
        elif model_name == "gemini":
            return Gemini(*args, **kwargs)
        else:
            raise ValueError(f"Modelo desconocido: {model_name}")
