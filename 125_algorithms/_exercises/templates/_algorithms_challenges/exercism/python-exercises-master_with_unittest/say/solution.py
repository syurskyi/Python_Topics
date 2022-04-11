___ say(number, recursive=F..
    small d..(e..((
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')))

    tens {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    k, m, b, t 1e3, 1e6, 1e9, 1e12

    __ number < 0:
        r.. AttributeError('number is negative')
    __ number >_ t:
        r.. AttributeError('number is too large: %s' % s..(number

    __ number < 20:
        r.. small[number] __ n.. recursive ____ 'and ' + small[number]

    __ number < 100:
        __ number % 10 __ 0:
            r.. small[number]
        r.. tens[number // 10 * 10] + '-' + small[number % 10]

    __ number < k:
        __ number % 100 __ 0:
            r.. small[number // 100] + ' hundred'
        r.. small[number // 100] + ' hundred and ' + say(number % 100)

    __ number < m:
        __ number % k __ 0:
            r.. say(number // k) + ' thousand'
        r.. say(number // k) + ' thousand ' + say(number % k, T..)

    __ number < b:
        __ number % m __ 0:
            r.. say(number // m) + ' million'
        r.. say(number // m) + ' million ' + say(number % m, T..)

    __ number % b __ 0:
        r.. say(number // b) + ' billion'
    r.. say(number // b) + ' billion ' + say(number % b, T..)
