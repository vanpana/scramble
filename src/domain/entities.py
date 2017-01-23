class Word(object):
    def __init__(self, word):
        self.__word = word
        self.__score = self.__getScore(word)
        self.__scrambled = None
        self.__undo = None

    def __getScore(self, word):
        counter = 0
        for c in word:
            if c == " ":
                counter += 1
        return len(word) - counter

    @property
    def word(self):
        return self.__word

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def scrambled(self):
        return self.__scrambled

    @scrambled.setter
    def scrambled(self, value):
        self.__scrambled = value

    @property
    def undo(self):
        return self.__undo

    @undo.setter
    def undo(self, value):
        self.__undo = value

    def __str__(self):
        return "{0} [score is: {1}]".format(self.__scrambled, self.__score)