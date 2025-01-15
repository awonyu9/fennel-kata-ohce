import pytest
from ohce.greeter import Clock, Greeter
import unittest
from ohce.ui import Interactor, UI

class Test_clock(Clock):
    __test__ = False
    def __init__(self, hour):
        self.hour = hour

    def current_hour(self):
        return self.hour
    
class Test_interactor(Interactor):
    __test__ = False
    def __init__(self, message):
        self.message = message

    def read_input(self):
        return self.message
    
    def print_message(self, input):
        return input

@pytest.fixture
def greeter():
    test_clock = Test_clock(0)
    greeter = Greeter(test_clock)

    yield greeter

def test_nightly_greeting(greeter):
    """
    Assert that greeter says "Good night" at midnight
    (when current hour is 0)
    """
    assert greeter.greet() == "Good night"


def test_greeting_never_returns_none():
    """
    Check that for each hour from 0 to 23, the greet()
    method never return None
    """
    for hour in range(24):
        test_clock = Test_clock(hour)
        greeter = Greeter(test_clock)
        assert greeter.greet() is not None


def test_ohce_main_loop():
    """
    Given the following inputs:
    - hello
    - oto
    - quit

    Check that the following messages are printed:
    - olleh
    - oto
    - That was a palindrome!
    """
    inputs = ["hello", "oto", "quit"]
    expected_messages = ["olleh", "oto\nThat was a palindrome!", None]
    for input in inputs:
        test_interactor = Test_interactor(input)
        ui = UI(test_interactor)
        output = ui.work_input(input)
        assert output == expected_messages[inputs.index(input)]

    # pytest.fail("TODO")
