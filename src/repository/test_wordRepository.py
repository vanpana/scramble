from unittest import TestCase

from domain.entities import Word
from domain.validator import WordValidator
from repository.repository import WordRepository


class TestWordRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__repository = WordRepository(WordValidator)
        self.__repository.save("aeiou bcd")

    def test_find_word(self):
        w = "aeiou bcd"
        self.assertEqual(self.__repository.find_word(w).word, "aeiou bcd", "The word should've been found")

    def test_find_number(self):
        self.assertEqual(self.__repository.find_word(0), None, "No word wound")

    def test_save(self):
        self.__repository.save("bcd ddd ddc")
        self.assertEqual(len(self.__repository.get_all()), 2, "2 words should be in the repo")

    def test_get_all(self):
        self.assertEqual(len(self.__repository.get_all()), 1, "1 word should be in the repo")
