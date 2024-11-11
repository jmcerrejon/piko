import unittest
from abc import ABC, abstractmethod

from src.models.interfaces import Answerable, Drawable


class TestDrawable(unittest.TestCase):
    def test_drawable_is_abstract(self) -> None:
        with self.assertRaises(TypeError):

            class IncompleteDrawable(Drawable):
                pass

            IncompleteDrawable()


class TestAnswerable(unittest.TestCase):
    def test_answerable_is_abstract(self) -> None:
        with self.assertRaises(TypeError):

            class IncompleteAnswerable(Answerable):
                pass

            IncompleteAnswerable()


if __name__ == "__main__":
    unittest.main()
