import traceback
from time import sleep


class Console(object):
    def __init__(self, controller):
        self.__controller = controller
        self.__the_word = None

    def initialise(self):
        '''
        Getting the random word
        :return: Nothing
        '''
        print("Hello to Scramble!")
        sleep(0.5)
        print("Wait to scramble your word...")
        sleep(0.5)
        print("Good luck, your word is: \n")
        self.__the_word = self.__controller.get_random()
        print(self.__the_word)

    def getCommand(self):
        '''
        Gets input from user
        :return: command - string
        '''
        command = input("")
        return command

    def validateCommand(self, command):
        '''
        Validates given command
        :param command: string
        :return: True/False
        '''
        if command == "undo":
            return True
        command = command.split(" ")
        if len(command) != 6:
            return False
        try:
            command[1] = int(command[1])
            command[2] = int(command[2])
            command[4] = int(command[4])
            command[5] = int(command[5])
        except ValueError:
            return False

        if command[1] == command[4] and command[2] == command[5]:
            return False

        if command[1] + command[2] == 0:
            return False

        if command[4] + command[5] == len(self.__the_word.word):
            return False

        if command[0] != "swap":
            return False

        if type(command[1]) != int or type(command[2]) != int or type(command[4]) != int or type(command[5]) != int:
            return False

        if command[3] != "-":
            return False

        if command[2] + command[1] > len(self.__the_word.word) - 1 or command[5] + command[4] > len(self.__the_word.word) - 1:
            return False

        word = self.__the_word.word.split(" ")
        if command[1] > len(word) - 1 or command[4] > len(word) - 1:
            return False

        if command[2] > len(word[command[1]]) or command[5] > len(word[command[4]]):
            return False

        return True

    def swapSomething(self, word1, letter1, word2, letter2):
        '''
        Sends the params to controller and if the users loses, message is printed!
        :param word1: position of the first word
        :param letter1: position of the first letter
        :param word2: position of the second word
        :param letter2: position of the second letter
        :return: may return false if user loses
        '''
        self.__the_word = self.__controller.swapSomething(self.__the_word, word1, letter1, word2, letter2)
        if self.__controller.checkValid(self.__the_word) == False:
            print("You lose!")
            return False

    def doUndo(self):
        '''
        UI undo function
        '''
        self.__the_word = self.__controller.undo(self.__the_word)

    def loop(self):
        '''
        The main loop. Terminates once user loses or wins.
        '''
        self.initialise()
        while True:
            try:
                if self.__controller.isCorrect(self.__the_word) == True:
                    print("Hooray! You won with {0} points!".format(self.__the_word.score))
                    break
                while True:
                    command = self.getCommand()
                    if self.validateCommand(command) == True:
                        break
                    else:
                        print("Invalid command")
                if command == "undo":
                    self.doUndo()
                    print(self.__the_word)
                else:
                    command = command.split(" ")
                    if self.swapSomething(int(command[1]), int(command[2]), int(command[4]), int(command[5])) == False:
                        break
                    else:
                        print(self.__the_word)
            except Exception as pve:
                print(pve)
                traceback.print_exc()

    def runApp(self):
        self.loop()