# Dependency Inversion Principle (DIP)

# High-level objects should not depend on low-level implementation. Both should depend on abstractions.
from abc import abstractmethod, ABC
from time import sleep


class TurnableOnObject(ABC):
    def __init__(self):
        self._on = False

    @property
    def on(self) -> bool:
        return self._on

    @abstractmethod
    def turn_on(self) -> None:
        pass


class Lamp(TurnableOnObject):
    def turn_on(self):
        self._on = True


class TimedLamp(Lamp):
    def turn_on(self):
        self._on = True
        print("Waiting for 1 second before turning the lamp off.")
        sleep(1)
        self._on = False


class OnButton:
    def __init__(self, lamp: Lamp):
        self.lamp = lamp

    def press(self):
        if not self.lamp.on:
            self.lamp.turn_on()
            print("The lamp has been turned on.")
        else:
            print("The lamp was already on.")


if __name__ == "__main__":
    lamp = Lamp()
    on_button = OnButton(lamp)
    on_button.press()
    on_button.press()
    on_button.press()

    timed_lamp = TimedLamp()
    on_button_2 = OnButton(timed_lamp)
    # on_button_2.press()
    # on_button_2.press()
