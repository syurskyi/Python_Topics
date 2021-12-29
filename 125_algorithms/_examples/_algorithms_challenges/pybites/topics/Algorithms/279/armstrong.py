def is_armstrong(n: int) -> bool:
    total = 0
    for digit in range(len(str(n))):
        total += int(str(n)[digit]) ** len(str(n))
    if total == n:
        return True
    else:
        return False