_______ asyncio
_______ time

# ONE_MIN = 60
# FIVE_MIN = ONE_MIN * 5
# TWENTY_FIVE_MIN = ONE_MIN * 25
# THIRTY_MIN = ONE_MIN * 30
# HOUR = ONE_MIN * 60
# CURRENT_SESSION = 1
____ asyncio _______ sleep
____ typing _______ Union

ONE_MIN = .006
FIVE_MIN = ONE_MIN * .0005
TWENTY_FIVE_MIN = ONE_MIN * .0025
THIRTY_MIN = ONE_MIN * .003
HOUR = ONE_MIN * .06
CURRENT_SESSION = 1


async ___ break_time(delay: Union[i.., float], loop: i..) __ N..
    """Break time

    :param delay: float of delay in seconds
    :param loop: int of the current loop
    :return: None
    """
    _delay = i..(delay / ONE_MIN)
    print(f"[{loop}] {time.strftime('%X')} Time for a {_delay} min break!")
    await sleep(delay)


async ___ lunch_time(delay: Union[i.., float]) __ N..
    """Lunch time

    :param delay: float of delay in seconds
    :return: None
    """
    print(f"\n** {time.strftime('%X')} Time for lunch! **")
    await sleep(delay)


async ___ work_time(delay: Union[i.., float], loop: i..) __ N..
    """Work time

    :param delay: float of delay in seconds
    :param loop: int of the current loop
    :return: None
    """
    print(f"[{loop}] {time.strftime('%X')} Time to work!")
    await sleep(delay)


async ___ session(
    work_length: Union[i.., float] = TWENTY_FIVE_MIN,
    short_break_length: Union[i.., float] = FIVE_MIN,
    long_break_length: Union[i.., float] = THIRTY_MIN,
) __ N..
    """Session

    :param work_length: float of work length in seconds
    :param short_break_length: float of short break length in seconds
    :param long_break_length: float of long break length in seconds
    :return: None
    """
    loop = 1

    w.... loop < 4:
        await work_time(work_length, loop)
        await break_time(short_break_length, loop)
        loop += 1

    await work_time(work_length, loop)

    __ CURRENT_SESSION % 2 != 0:
        await break_time(long_break_length, loop)


async ___ main(
    work_length: Union[i.., float] = TWENTY_FIVE_MIN,
    short_break_length: Union[i.., float] = FIVE_MIN,
    long_break_length: Union[i.., float] = THIRTY_MIN,
    lunch_length: Union[i.., float] = HOUR,
) __ N..
    """Main entry point

    :param work_length: float of work length in seconds
    :param short_break_length: float of short break length in seconds
    :param long_break_length: float of long break length in seconds
    :param lunch_length: float of lunch length in seconds
    :return: None
    """
    global CURRENT_SESSION
    print(f"Pomodor timer started at: {time.strftime('%X')}")

    w.... CURRENT_SESSION <= 4:
        print(f"\nSession: {CURRENT_SESSION}")
        await session(work_length, short_break_length, long_break_length)
        __ CURRENT_SESSION __ 2:
            await lunch_time(lunch_length)
        CURRENT_SESSION += 1

    print(f"\n{time.strftime('%X')} Time to go home!")

    print(f"\nWork day completed at: {time.strftime('%X')}")


__ __name__ __ "__main__":
    asyncio.run(main())