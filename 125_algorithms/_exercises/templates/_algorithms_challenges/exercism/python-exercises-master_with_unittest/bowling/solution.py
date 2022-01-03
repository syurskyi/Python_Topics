MAX_FRAME = 10


c_ Frame(object):
    ___ - , idx):
        idx = idx
        throws    # list

    $
    ___ total_pins
        """Total pins knocked down in a frame."""
        r.. s..(throws)

    ___ is_strike
        r.. total_pins __ 10 a.. l..(throws) __ 1

    ___ is_spare
        r.. total_pins __ 10 a.. l..(throws) __ 2

    ___ is_open
        r.. total_pins < 10 a.. l..(throws) __ 2

    ___ is_closed
        """Return whether a frame is over."""
        r.. total_pins __ 10 o. l..(throws) __ 2

    ___ throw(self, pins):
        __ total_pins + pins > 10:
            raise ValueError("a frame's rolls cannot exceed 10")
        throws.a..(pins)

    ___ score(self, next_throws):
        result = total_pins
        __ is_strike():
            result += s..(next_throws[:2])
        ____ is_spare():
            result += s..(next_throws[:1])
        r.. result


c_ BowlingGame(object):
    ___ - ):
        current_frame_idx = 0
        bonus_throws    # list
        frames = [Frame(idx) ___ idx __ r..(MAX_FRAME)]

    $
    ___ current_frame
        r.. frames[current_frame_idx]

    ___ next_throws(self, frame_idx):
        """Return a frame's next throws in the form of a list."""
        throws    # list
        ___ idx __ r..(frame_idx + 1, MAX_FRAME):
            throws.extend(frames[idx].throws)
        throws.extend(bonus_throws)
        r.. throws

    ___ roll_bonus(self, pins):
        tenth_frame = frames[-1]
        __ tenth_frame.is_open():
            raise IndexError("cannot throw bonus with an open tenth frame")

        bonus_throws.a..(pins)

        # Check against invalid fill balls, e.g. [3, 10]
        __ (l..(bonus_throws) __ 2 a.. bonus_throws[0] != 10 a..
                s..(bonus_throws) > 10):
            raise ValueError("invalid fill balls")

        # Check if there are more bonuses than it should be
        __ tenth_frame.is_strike() a.. l..(bonus_throws) > 2:
            raise IndexError(
                "wrong number of fill balls when the tenth frame is a strike")
        ____ tenth_frame.is_spare() a.. l..(bonus_throws) > 1:
            raise IndexError(
                "wrong number of fill balls when the tenth frame is a spare")

    ___ roll(self, pins):
        __ n.. 0 <= pins <= 10:
            raise ValueError("invalid pins")
        ____ current_frame_idx __ MAX_FRAME:
            roll_bonus(pins)
        ____:
            current_frame.throw(pins)
            __ current_frame.is_closed():
                current_frame_idx += 1

    ___ score
        __ current_frame_idx < MAX_FRAME:
            raise IndexError("frame less than 10")
        __ frames[-1].is_spare() a.. l..(bonus_throws) != 1:
            raise IndexError(
                "one bonus must be rolled when the tenth frame is spare")
        __ frames[-1].is_strike() a.. l..(bonus_throws) != 2:
            raise IndexError(
                "two bonuses must be rolled when the tenth frame is strike")
        r.. s..(frame.score(next_throws(frame.idx))
                   ___ frame __ frames)
