"""
All that is open must be closed...
http://www.codewars.com/kata/55679d644c58e2df2a00009c/train/python
"""
___ is_balanced(source, caps):
    count = {}
    stack = []
    for c in source:
        __ c in caps:
            i = caps.index(c)
            __ i % 2 == 0:
                __ caps[i] == caps[i + 1]:
                    __ caps[i] in count:
                        count[caps[i]] += 1
                    else:
                        count[caps[i]] = 1
                else:
                    stack.append(c)
            else:
                __ caps[i - 1] == caps[i]:
                    __ caps[i] in count:
                        count[caps[i]] += 1
                    else:
                        count[caps[i]] = 1
                else:
                    __ len(stack) == 0 or stack.pop() != caps[i - 1]:
                        return False
    return (len(stack) == 0) and ((sum([v for k, v in count.items()])) % 2 == 0)

print(is_balanced("(Sensei says yes!)", "()") == True)
print(is_balanced("(Sensei says no!", "()") == False)

print(is_balanced("(Sensei [says] yes!)", "()[]") == True)
print(is_balanced("(Sensei [says) no!]", "()[]") == False)

print(is_balanced("Sensei says -yes-!", "--") == True)
print(is_balanced("Sensei -says no!", "--") == False)
