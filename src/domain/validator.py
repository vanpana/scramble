class Validator(Exception):
    pass

class WordValidatorException(Exception):
    pass

class WordValidator(object):
    '''
    Class that validates if given word is correct.
    '''
    @staticmethod
    def validate(word):
        if len(word) == 0:
            raise WordValidatorException("Can't be an empty word")