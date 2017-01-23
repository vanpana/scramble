from unittest import TestCase

from domain.validator import WordValidator
from repository.filerepository import WordFileRepository

class TestWordFileRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__filerepo = WordFileRepository(WordValidator, "/Users/vanpana/PycharmProjects/practical_exam/data/input.txt")

    def test_get_all(self):
        self.assertEqual(len(self.__filerepo.get_all()), 6, "6 words should be imported from file")
