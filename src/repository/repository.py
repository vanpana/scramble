from domain.entities import Word


class WordException(Exception):
    pass

class WordRepository(object):
    '''
    Class where all the words type object are being saved.
    '''
    def __init__(self, validator):
        self.__validator = validator
        self.__entities = []

    def find_word(self, string):
        '''
        Finds a word object having the given string
        :param string: given string to search
        :return: object of type word
        '''
        for word in self.__entities:
            if word.word == string:
                return word
        return None

    def find_number(self, number):
        '''
        Finds word with position specified by number
        :param number: integer
        :return: object of type word
        '''
        return self.__entities[number]

    def save(self, word):
        '''
        Saves a word into repository entites
        :param word: a word type object
        :return:
        :raises: WordException if invalid word
        '''
        try:
            self.__validator.validate(word)
        except Exception:
            raise WordException("Invalid word!")
        self.__entities.append(Word(word))


    def get_all(self):
        '''
        Returns a list of all words in repository
        :return: list
        '''
        return self.__entities