___ say(number, recursive=False):
    small = dict(enumerate((
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')))

    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
            60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    k, m, b, t = 1e3, 1e6, 1e9, 1e12

    __ number < 0:
        raise AttributeError('number is negative')
    __ number >= t:
        raise AttributeError('number is too large: %s' % str(number))

    __ number < 20:
        return small[number] __ not recursive else 'and ' + small[number]

    __ number < 100:
        __ number % 10 == 0:
            return small[number]
        return tens[number // 10 * 10] + '-' + small[number % 10]

    __ number < k:
        __ number % 100 == 0:
            return small[number // 100] + ' hundred'
        return small[number // 100] + ' hundred and ' + say(number % 100)

    __ number < m:
        __ number % k == 0:
            return say(number // k) + ' thousand'
        return say(number // k) + ' thousand ' + say(number % k, True)

    __ number < b:
        __ number % m == 0:
            return say(number // m) + ' million'
        return say(number // m) + ' million ' + say(number % m, True)

    __ number % b == 0:
        return say(number // b) + ' billion'
    return say(number // b) + ' billion ' + say(number % b, True)
