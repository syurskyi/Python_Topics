# Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
# Score: 10


___ handler(a
    command = input().split()[0]
    new_set = set(map(int, input().split()))
    __ command __ 'intersection_update':
        a.intersection_update(new_set)
    __ command __ 'update':
        a.update(new_set)
    __ command __ 'symmetric_difference_update':
        a.symmetric_difference_update(new_set)
    __ command __ 'difference_update':
        a.difference_update(new_set)


_, a = input(), set(map(int, input().split()))
for i in range(int(input())):
    handler(a)
print(sum(a))
