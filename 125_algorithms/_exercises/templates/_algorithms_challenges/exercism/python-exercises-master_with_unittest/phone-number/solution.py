_______ __


c_ Phone(o..
    ___ - , number
        number _clean(number)

    ___ area_code
        r.. number |3

    ___ exchange_code
        r.. number[3:6]

    ___ subscriber_number
        r.. number[-4:]

    ___ pretty
        r.. "(%s) %s-%s" % (
            area_code(),
            exchange_code(),
            subscriber_number()
        )

    ___ _clean  number
        r.. _normalize(
            __.s.. _ [^\d]', '', number)
        )

    ___ _normalize  number
        valid l..(number) __ 10 o. \
            l..(number) __ 11 a.. number.s.. '1')

        __ valid:
            r.. number[-10:]
        ____
            r.. '0' * 10
