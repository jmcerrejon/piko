from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass


class Answerable(ABC):
    @abstractmethod
    def answer(self, input: str) -> str:
        pass
