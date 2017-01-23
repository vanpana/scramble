import random

class WordController(object):
    '''
    Class controller is a bridge between UI level and repository level
    '''
    def __init__(self, repository):
        self.__repository = repository

    def get_random(self):
        '''
        Gets random word from repository
        :return: word type object
        '''
        rInt = random.randint(0, len(self.__repository.get_all()) - 1)
        word = self.__repository.find_number(rInt)
        word.scrambled = self.__scramble(self.strToList(word.word), word.score)
        return word

    def strToList(self, string):
        '''
        Converts a string to a list
        :param string: string to be converted
        :return: list
        '''
        l = []
        for c in string:
            l.append(c)
        return l

    def listToStr(self, l):
        '''
        Converts a list to a string
        :param l: list to be converted
        :return: string
        '''
        s = ""
        for elem in l:
            s = s + elem
        return s

    def __scramble(self, word, length):
        '''
        Scrambles the word for the first print
        :param word: word type object
        :param length: the maximum length
        :return: modified word type object
        '''
        times = random.randint(0, 100)
        for i in range(0, times):
            a, b = 0, 0
            while a == b:
                a = random.randint(1, length - 2)
                b = random.randint(1, length - 2)
                if word[a] == " " or word[b] == " " or word[a-1] == " " or word[a+1] == " " or word[b-1] == " " or word[b+1] == " ":
                    a = b
            word[a], word[b] = word[b], word[a]
        return self.listToStr(word)

    def checkValid(self, word):
        '''
        Check if score is still valid
        :param word: word type object
        :return: True/False
        '''
        if word.score == 0:
            return False
        return True

    def getPos(self, text, w, l):
        '''
        Gets position for swapping
        :param text: text in a list
        :param w: how many words
        :param l: how many letters
        :return: position - int
        '''
        i = 0
        length = 0
        if w > 0:
            length += 1
        while w > 0:
            length += 1
            i += 1
            if text[i] == " ":
                w -= 1
        length += l
        return length

    def undo(self, the_word):
        '''
        Undo operation
        :param the_word: word type object
        :return: modified word type object
        '''
        the_word.scrambled = the_word.undo
        return the_word

    def swapSomething(self, the_word, word1, letter1, word2, letter2):
        '''
        Swaps the two given positions
        :param the_word: word type object
        :param word1: position of the first word
        :param letter1: position of the first letter
        :param word2: position of the second word
        :param letter2: position of the second letter
        :return: modified word type object
        '''
        the_word.undo = the_word.scrambled
        word = self.strToList(the_word.scrambled)
        pos1 = self.getPos(word, word1, letter1)
        pos2 = self.getPos(word, word2, letter2)
        word[pos1], word[pos2] = word[pos2], word[pos1]
        the_word.score = the_word.score - 1
        the_word.scrambled = self.listToStr(word)
        return the_word

    def isCorrect(self, word):
        '''
        Check if scrambled word is the original word
        :param word: word type object
        :return: True/False
        '''
        if word.word == word.scrambled:
            return True
        return False

    def get_all(self):
        '''
        Gets all words in repository level
        :return: list of word type objects
        '''
        return self.__repository.get_all()