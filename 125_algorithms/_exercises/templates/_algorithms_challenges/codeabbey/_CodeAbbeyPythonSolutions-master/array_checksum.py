amount_values = int(input())

___ get_checksum(values):
    limit = 10000007
    result = 0
    seed = 113

    ___ i __ values:
        result = (result + i) * seed
        __(result > limit):
            result = result % limit

    r.. result

values = l..(map(int, input().split()))

__ __name__ __ "__get_checksum__":
    get_checksum(values)

print(get_checksum(values))
