class AI:
    def __new__(cls: type, model_name: str = "openai", *args: tuple, **kwargs: dict):  # type: ignore
        match model_name:
            case "openai":
                from src.models.openai import OpenAI

                return OpenAI(*args, **kwargs)
            case "gemini":
                from src.models.gemini import Gemini

                return Gemini(*args, **kwargs)
            case _:
                raise ValueError(f"Unknown AI library: {model_name}")
