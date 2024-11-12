import unittest

from src.ai import AI
from src.helpers.dot_env_loader import DotenvLoader
from src.models.gemini import Gemini
from src.models.openai import OpenAI


class TestAI(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        DotenvLoader.load(".env")

    def test_ai_creates_openai_instance(self) -> None:
        ai_instance = AI("openai")
        self.assertIsInstance(ai_instance, OpenAI)

    def test_ai_creates_gemini_instance(self) -> None:
        ai_instance = AI("gemini")
        self.assertIsInstance(ai_instance, Gemini)

    def test_ai_raises_value_error_for_unknown_model(self) -> None:
        with self.assertRaises(ValueError) as context:
            AI("unknown_model")
        self.assertEqual(str(context.exception), "Unknown AI library: unknown_model")


if __name__ == "__main__":
    unittest.main()
