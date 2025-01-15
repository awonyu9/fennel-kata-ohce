from ohce.greeter import Greeter
from ohce.ui import UI
from ohce.greeter import SystemClock


def main():
    clock = SystemClock()
    greeter = Greeter(clock)
    greetings = greeter.greet()
    print(greetings)

    ui = UI()
    ui.main_loop()


main()
