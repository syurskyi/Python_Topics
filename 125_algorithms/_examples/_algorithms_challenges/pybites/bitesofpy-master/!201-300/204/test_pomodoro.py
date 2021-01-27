from typing import Union

import pytest

from pomodoro import break_time, lunch_time, main, session, work_time


@pytest.mark.asyncio
async def test_break_time(capfd):
    anno = break_time.__annotations__
    a__ anno["delay"] == Union[int, float]
    a__ anno["loop"] == int
    a__ anno["return"] is None
    delay = 0.0001
    await break_time(delay, 1)
    output = capfd.readouterr()[0].strip()
    a__ "[1]" in output
    a__ f"Time for a {int(delay/60)} min break!" in output


@pytest.mark.asyncio
async def test_lunch_time(capfd):
    anno = lunch_time.__annotations__
    a__ anno["delay"] == Union[int, float]
    a__ anno["return"] is None
    delay = 0.06
    await lunch_time(delay)
    output = capfd.readouterr()[0].strip()
    a__ "Time for lunch!" in output


@pytest.mark.asyncio
async def test_work_time(capfd):
    anno = work_time.__annotations__
    a__ anno["delay"] == Union[int, float]
    a__ anno["return"] is None
    delay = 0.0025
    await work_time(delay, 3)
    output = capfd.readouterr()[0].strip()
    a__ "[3]" in output
    a__ "Time to work!" in output


@pytest.mark.asyncio
async def test_session(capfd):
    anno = session.__annotations__
    a__ anno["work_length"] == Union[int, float]
    a__ anno["short_break_length"] == Union[int, float]
    a__ anno["long_break_length"] == Union[int, float]
    a__ anno["return"] is None
    await session(0.0025, 0.0005, 0.003)
    output = capfd.readouterr()[0].strip()
    a__ "Time to work!" in output
    a__ "min break!" in output
    a__ "Time for lunch!" not in output
    a__ len(output.splitlines()) == 8


@pytest.mark.asyncio
async def test_main(capfd):
    anno = main.__annotations__
    a__ anno["work_length"] == Union[int, float]
    a__ anno["short_break_length"] == Union[int, float]
    a__ anno["long_break_length"] == Union[int, float]
    a__ anno["lunch_length"] == Union[int, float]
    a__ anno["return"] is None
    await main(0.0025, 0.0005, 0.003, 0.01)
    output = capfd.readouterr()[0].strip()
    a__ "Pomodor timer started at" in output
    a__ "Time to work!" in output
    a__ "min break!" in output
    a__ "Time for lunch!" in output
    a__ "Work day completed at" in output
    a__ len(output.splitlines()) == 45