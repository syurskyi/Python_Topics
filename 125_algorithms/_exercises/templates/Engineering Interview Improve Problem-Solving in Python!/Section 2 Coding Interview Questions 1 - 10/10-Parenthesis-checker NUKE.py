# ((()())()) => True
# )())) = False
# (() => False
# )( => False

___ check(s):
    left  0
    for c in s:
        __ c __ '(':
            left + 1
        else:
            __ left __ 0:
                return F..
            left - 1
    return left __ 0

print(check("((()())())"))
print(check("(()()))"))
print(check(")("))