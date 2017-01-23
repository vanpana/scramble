from controller.controller import WordController
from domain.validator import WordValidator
from repository.filerepository import WordFileRepository
from ui.console import Console

if __name__ == "__main__":
    '''
    Creating repository, controller and console classes
    '''
    repository = WordFileRepository(WordValidator, "../data/input.txt")
    controller = WordController(repository)
    console = Console(controller)

    console.runApp()