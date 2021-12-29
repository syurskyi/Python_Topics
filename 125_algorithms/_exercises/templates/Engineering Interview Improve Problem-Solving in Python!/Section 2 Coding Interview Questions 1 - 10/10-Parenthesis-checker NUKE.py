# ((()())()) => True
# )())) = False
# (() => False
# )( => False

___ check(s):
    left  0
    ___ c __ s:
        __ c __ '(':
            left + 1
        ____:
            __ left __ 0:
                r.. F..
            left - 1
    r.. left __ 0

print(check("((()())())"))
print(check("(()()))"))
print(check(")("))