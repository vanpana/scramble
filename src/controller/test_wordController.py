from unittest import TestCase

from controller.controller import WordController
from domain.entities import Word
from domain.validator import WordValidator
from repository.filerepository import WordFileRepository


class TestWordController(TestCase):
    def setUp(self):
        super().setUp()
        self.__repository = WordFileRepository(WordValidator, "/Users/vanpana/PycharmProjects/practical_exam/data/input.txt")
        self.__controller = WordController(self.__repository)

    def test_get_random(self):
        word = self.__controller.get_random()
        self.assertEqual(type(word), Word, "Randomly generated word")

    def test_strToList(self):
        string = "aeiou"
        self.assertEqual(type(self.__controller.strToList(string)), list, "Should be a list")

    def test_listToStr(self):
        list = ["a", "e", "i"]
        self.assertEqual(type(self.__controller.listToStr(list)), str, "Should be a string")

    def test_checkValid(self):
        word = Word("da")
        self.assertEqual(self.__controller.checkValid(word), True, "It's totally valid")
        word = Word("")
        self.assertEqual(self.__controller.checkValid(word), False, "It's totally invalid")

    def test_getPos(self):
        word = "ab aa aa"
        w = 0
        l = 1
        self.assertEqual(word[self.__controller.getPos(word,w,l)], "b", "Should be b")

    def test_undo(self):
        word = Word("aa bb cc")
        word.scrambled = "ab ba ca"
        word.undo = "aa bb cc"
        self.assertEqual(self.__controller.undo(word).scrambled, "aa bb cc", "Undone!")

    def test_swapSomething(self):
        word = Word("aa bb cc")
        word.scrambled = "ab ba ca"
        self.assertEqual(self.__controller.swapSomething(word, 1, 0, 1, 1).scrambled, "ab ab ca")

    def test_isCorrect(self):
        word = Word("aa bb cc")
        word.scrambled = "aa bb cc"
        self.assertEqual(self.__controller.isCorrect(word), True, "It's true")

    def test_get_all(self):
        self.assertEqual(len(self.__controller.get_all()), 6, "There should be 6")
