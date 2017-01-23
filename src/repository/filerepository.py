from repository.repository import WordRepository


class WordFileRepository(WordRepository):
    '''
    Class that reads from file all the strings
    '''
    def __init__(self, validator, filename):
        self.__validator = super().__init__(validator)
        self.__filename = filename
        self.__load(filename)

    def __load(self, filename):
        '''
        Function that loads into memory the file contents
        :param filename: Name of the file
        :return:
        '''
        with open(filename) as f:
            for line in f:
                line = line.strip("\n")
                super().save(line)