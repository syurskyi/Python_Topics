"""
All that is open must be closed...
http://www.codewars.com/kata/55679d644c58e2df2a00009c/train/python
"""
___ is_balanced(source, caps
    count = {}
    stack = []
    for c in source:
        __ c in caps:
            i = caps.index(c)
            __ i % 2 __ 0:
                __ caps[i] __ caps[i + 1]:
                    __ caps[i] in count:
                        count[caps[i]] += 1
                    ____
                        count[caps[i]] = 1
                ____
                    stack.append(c)
            ____
                __ caps[i - 1] __ caps[i]:
                    __ caps[i] in count:
                        count[caps[i]] += 1
                    ____
                        count[caps[i]] = 1
                ____
                    __ le.(stack) __ 0 or stack.pop() != caps[i - 1]:
                        r_ False
    r_ (le.(stack) __ 0) and ((sum([v for k, v in count.items()])) % 2 __ 0)

print(is_balanced("(Sensei says yes!)", "()") __ True)
print(is_balanced("(Sensei says no!", "()") __ False)

print(is_balanced("(Sensei [says] yes!)", "()[]") __ True)
print(is_balanced("(Sensei [says) no!]", "()[]") __ False)

print(is_balanced("Sensei says -yes-!", "--") __ True)
print(is_balanced("Sensei -says no!", "--") __ False)
