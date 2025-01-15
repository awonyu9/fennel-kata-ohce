from ohce.greeter import Greeter
from ohce.ui import UI, ConsoleInteractor
from ohce.greeter import SystemClock


def main():
    clock = SystemClock()
    greeter = Greeter(clock)
    greetings = greeter.greet()
    print(greetings)

    interactor = ConsoleInteractor()
    ui = UI(interactor)
    ui.main_loop()


main()
