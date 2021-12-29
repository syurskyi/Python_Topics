# enumerate() use cases

# this is crap, because I might pass out of range value and generate exception
def test_case1():
    for i in range(0, 3):
        print(f'Index = {i} value = {list1[i]}')


def test_case2():
    for item in enumerate(list1):
        print(item)