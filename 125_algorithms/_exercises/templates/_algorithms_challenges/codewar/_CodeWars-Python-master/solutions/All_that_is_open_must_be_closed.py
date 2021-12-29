"""
All that is open must be closed...
http://www.codewars.com/kata/55679d644c58e2df2a00009c/train/python
"""
___ is_balanced(source, caps):
    count = {}
    stack    # list
    ___ c __ source:
        __ c __ caps:
            i = caps.index(c)
            __ i % 2 __ 0:
                __ caps[i] __ caps[i + 1]:
                    __ caps[i] __ count:
                        count[caps[i]] += 1
                    ____:
                        count[caps[i]] = 1
                ____:
                    stack.a..(c)
            ____:
                __ caps[i - 1] __ caps[i]:
                    __ caps[i] __ count:
                        count[caps[i]] += 1
                    ____:
                        count[caps[i]] = 1
                ____:
                    __ l..(stack) __ 0 o. stack.pop() != caps[i - 1]:
                        r.. False
    r.. (l..(stack) __ 0) and ((s..([v ___ k, v __ count.items()])) % 2 __ 0)

print(is_balanced("(Sensei says yes!)", "()") __ True)
print(is_balanced("(Sensei says no!", "()") __ False)

print(is_balanced("(Sensei [says] yes!)", "()[]") __ True)
print(is_balanced("(Sensei [says) no!]", "()[]") __ False)

print(is_balanced("Sensei says -yes-!", "--") __ True)
print(is_balanced("Sensei -says no!", "--") __ False)
