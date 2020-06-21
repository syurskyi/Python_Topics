def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Note sure who you are"


print(ensure_correct_info("hello", False, 78))  # Not sure who you are...

print(ensure_correct_info(1, True, "Steele", "Colt"))

