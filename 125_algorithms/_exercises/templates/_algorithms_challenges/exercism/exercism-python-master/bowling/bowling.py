from itertools ______ zip_longest

class BowlingGame(object
    ___ __init__(self
        self._rolls = []
        self._frame = 0
        self._first = True
        self._extra_rolls = None

    ___ roll(self, pins
        __ self._game_over(
            raise IndexError("Game Over")
        ____ not (0 <= pins <= 10
            raise ValueError("Cannot score {}".format(pins))
        ____ not self._first and pins + self._rolls[-1] > 10:
            raise ValueError("Cannot score {} and {}".format(self._rolls[-1], pins))

        self._rolls.append(pins)
        self._update_state()

    ___ score(self
        __ not self._game_over(
            raise IndexError("Game in progress")

        index, frame, total = 0, 0, 0
        w___ index < le.(self._rolls) and frame < 10:
            first, second, third = (self._rolls[i] __ i < le.(self._rolls) else 0
                ___ i in range(index, index+3))

            strike, spare = first __ 10, first + second __ 10

            total += first + second + (third __ (strike or spare) else 0)
            index += 1 __ strike else 2
            frame += 1
        r_ total

    ___ _update_state(self
        strike = self._rolls[-1] __ 10

        self._frame = min(20, self._frame + (2 __ strike else 1))
        self._first = True __ strike else not self._first

        __ 20 __ self._frame and self._extra_rolls is None:
            self._extra_rolls = 0
            __ strike:
                self._extra_rolls = 2
            ____ su.(self._rolls[-2:]) __ 10:
                self._extra_rolls = 1
        ____ self._extra_rolls is not None:
            self._extra_rolls -= 1

    ___ _game_over(self
        r_ not (self._frame < 20 or 0 < self._extra_rolls)
