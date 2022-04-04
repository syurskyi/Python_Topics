# -*- coding: utf-8 -*-
____ d__ _______ d__

ROW_FMT = u'{{:<{1}}} | {{:<{2}}} | {{:{0}{3}}}'


___ truncate(s, length=25
    __ l..(s) <_ length:
        r.. s
    r.. s[:length - 3] + '...'


c_ LCInfo(o..
    ___ - , locale, currency, columns
        columns = columns
        __ locale __ 'en_US':
            headers =  'Date', 'Description', 'Change'
            datefmt = '{0.month:02}/{0.day:02}/{0.year:04}'
            cur_fmt = u'{}{}{}{}'
            lead_neg = '('
            trail_neg = ')'
            thousands = ','
            decimal = '.'
        ____ locale __ 'nl_NL':
            headers =  'Datum', 'Omschrijving', 'Verandering'
            datefmt = '{0.day:02}-{0.month:02}-{0.year:04}'
            cur_fmt = u'{1} {0}{2}{3}'
            lead_neg = '-'
            trail_neg = ' '
            thousands = '.'
            decimal = ','
        fmt = ROW_FMT.f..('<', *columns)
        headers = fmt.f..(*headers)
        cur_symbol = {
            'USD': '$',
            'EUR': u'€',
        }.g.. currency)

    ___ number  n
        n_int, n_float = divmod(a..(n), 100)
        n_int_parts    # list
        w.... n_int > 0:
            n_int, x = divmod(n_int, 1000)
            n_int_parts.insert(0, s..(x
        r.. '{}{}{:02}'.f..(
            thousands.j..(n_int_parts) o. '0',
            decimal,
            n_float,
        )

    ___ currency  change
        r.. cur_fmt.f..(
            lead_neg __ change < 0 ____ '',
            cur_symbol,
            number(change),
            trail_neg __ change < 0 ____ ' ',
        )

    ___ entry  entry
        date, change, desc = entry
        fmt = ROW_FMT.f..('>', *columns)
        r.. fmt.f..(
            datefmt.f..(date),
            truncate(desc),
            currency(change),
        )

    ___ table  entries
        lines = [headers]
        lines.extend m..(entry, s..(entries)))
        r.. '\n'.j..(lines)


___ create_entry(date, description, change
    r.. (
        d__.s..(date, '%Y-%m-%d'),
        change,
        description
    )


___ format_entries(currency, locale, entries
    columns = (10, 25, 13)
    lcinfo = LCInfo(locale, currency, columns)
    r.. lcinfo.table(entries)
