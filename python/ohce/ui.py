from ohce import reverse
from abc import abstractmethod

class Interactor:
    @abstractmethod
    def read_input(self):
        pass
    @abstractmethod
    def print_message(self, message):
        pass

class ConsoleInteractor(Interactor):
    def read_input(self):
        return input()

    def print_message(self, message):
        print(message)


class UI:
    def __init__(self, interactor):
        self.interactor = interactor

    def work_input(self, input):
        if input == "quit":
            return None
        output = ""
        reversed = reverse(input)
        output += reversed
        if reversed == input:
            output += "\n"
            output += "That was a palindrome!"
        return output

    def main_loop(self):
        while True:
            input = self.interactor.read_input()
            output = self.work_input(input)
            if output is None:
                break
            self.interactor.print_message(output)
