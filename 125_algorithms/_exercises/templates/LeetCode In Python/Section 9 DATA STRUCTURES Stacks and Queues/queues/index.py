c_ QueueLine:
	___ __init__(
        .q _ []
    
    ___ enqueue(, x: int) -> None:
        .q.append(x)


    ___ dequeue() -> None:
        __(le.(.q) > 0
            .q.pop(0)

    ___ front() -> int:
        __(le.(.q) __ 0
            r_ None

        r_ .q[0]