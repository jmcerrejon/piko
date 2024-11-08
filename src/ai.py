import os

from openai import OpenAI

from src.helper.utils import Utils


class AI:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.model_name = {"text": "gpt-4o-mini", "image": "dall-e-3"}

    def draw(self) -> str:
        print("\nYou want a picture!")
        prompt = input("\nImagine... ")

        if prompt == "exit":
            print("\nBye! I hope I was helpful!")
            exit()

        print("\nLet me draw something about that...\n")
        answer = self.client.images.generate(
            model=self.model_name["image"],
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        url = answer.data[0].url
        Utils.open_default_browser(url)

        return url

    def answer(self, input) -> str:
        prompt = f"""
        Input: {input}
        
        Based on the above information, answer the input with humor (you are a millions of flies).
        """

        response = self.client.chat.completions.create(
            model=self.model_name["text"],
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant tasked with answering with humor.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )
        print("\nLet me think about that...")

        return response.choices[0].message.content.strip()
