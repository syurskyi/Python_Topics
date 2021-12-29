MAX_FRAME = 10


class Frame(object):
    ___ __init__(self, idx):
        self.idx = idx
        self.throws = []

    @property
    ___ total_pins(self):
        """Total pins knocked down in a frame."""
        return sum(self.throws)

    ___ is_strike(self):
        return self.total_pins == 10 and len(self.throws) == 1

    ___ is_spare(self):
        return self.total_pins == 10 and len(self.throws) == 2

    ___ is_open(self):
        return self.total_pins < 10 and len(self.throws) == 2

    ___ is_closed(self):
        """Return whether a frame is over."""
        return self.total_pins == 10 or len(self.throws) == 2

    ___ throw(self, pins):
        __ self.total_pins + pins > 10:
            raise ValueError("a frame's rolls cannot exceed 10")
        self.throws.append(pins)

    ___ score(self, next_throws):
        result = self.total_pins
        __ self.is_strike():
            result += sum(next_throws[:2])
        elif self.is_spare():
            result += sum(next_throws[:1])
        return result


class BowlingGame(object):
    ___ __init__(self):
        self.current_frame_idx = 0
        self.bonus_throws = []
        self.frames = [Frame(idx) for idx in range(MAX_FRAME)]

    @property
    ___ current_frame(self):
        return self.frames[self.current_frame_idx]

    ___ next_throws(self, frame_idx):
        """Return a frame's next throws in the form of a list."""
        throws = []
        for idx in range(frame_idx + 1, MAX_FRAME):
            throws.extend(self.frames[idx].throws)
        throws.extend(self.bonus_throws)
        return throws

    ___ roll_bonus(self, pins):
        tenth_frame = self.frames[-1]
        __ tenth_frame.is_open():
            raise IndexError("cannot throw bonus with an open tenth frame")

        self.bonus_throws.append(pins)

        # Check against invalid fill balls, e.g. [3, 10]
        __ (len(self.bonus_throws) == 2 and self.bonus_throws[0] != 10 and
                sum(self.bonus_throws) > 10):
            raise ValueError("invalid fill balls")

        # Check if there are more bonuses than it should be
        __ tenth_frame.is_strike() and len(self.bonus_throws) > 2:
            raise IndexError(
                "wrong number of fill balls when the tenth frame is a strike")
        elif tenth_frame.is_spare() and len(self.bonus_throws) > 1:
            raise IndexError(
                "wrong number of fill balls when the tenth frame is a spare")

    ___ roll(self, pins):
        __ not 0 <= pins <= 10:
            raise ValueError("invalid pins")
        elif self.current_frame_idx == MAX_FRAME:
            self.roll_bonus(pins)
        else:
            self.current_frame.throw(pins)
            __ self.current_frame.is_closed():
                self.current_frame_idx += 1

    ___ score(self):
        __ self.current_frame_idx < MAX_FRAME:
            raise IndexError("frame less than 10")
        __ self.frames[-1].is_spare() and len(self.bonus_throws) != 1:
            raise IndexError(
                "one bonus must be rolled when the tenth frame is spare")
        __ self.frames[-1].is_strike() and len(self.bonus_throws) != 2:
            raise IndexError(
                "two bonuses must be rolled when the tenth frame is strike")
        return sum(frame.score(self.next_throws(frame.idx))
                   for frame in self.frames)
