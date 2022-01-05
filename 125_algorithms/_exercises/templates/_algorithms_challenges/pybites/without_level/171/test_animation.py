_______ p__

____ animation _______ spinner, SPINNER_STATES __ states


@p__.mark.parametrize("seconds, rounds, slice_", [
    (0.2, 0, 2),
    (0.4, 1, 0),
    (1, 2, 2),
    (1.2, 3, 0),
])
___ test_spinner(monkeypatch, capfd, seconds, rounds, slice_):
    spinner(seconds)
    actual = ?.r .. 0].s...s..('\r')
    expected = states * rounds
    __ slice_:
        expected += states[:slice_]
    ... actual __ expected