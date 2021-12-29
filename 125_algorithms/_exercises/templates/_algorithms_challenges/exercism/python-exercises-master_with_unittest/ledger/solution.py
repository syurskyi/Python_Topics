# -*- coding: utf-8 -*-
____ datetime _______ datetime

ROW_FMT = u'{{:<{1}}} | {{:<{2}}} | {{:{0}{3}}}'


___ truncate(s, length=25):
    __ l..(s) <= length:
        r.. s
    r.. s[:length - 3] + '...'


class LCInfo(object):
    ___ __init__(self, locale, currency, columns):
        self.columns = columns
        __ locale __ 'en_US':
            headers = ['Date', 'Description', 'Change']
            self.datefmt = '{0.month:02}/{0.day:02}/{0.year:04}'
            self.cur_fmt = u'{}{}{}{}'
            self.lead_neg = '('
            self.trail_neg = ')'
            self.thousands = ','
            self.decimal = '.'
        ____ locale __ 'nl_NL':
            headers = ['Datum', 'Omschrijving', 'Verandering']
            self.datefmt = '{0.day:02}-{0.month:02}-{0.year:04}'
            self.cur_fmt = u'{1} {0}{2}{3}'
            self.lead_neg = '-'
            self.trail_neg = ' '
            self.thousands = '.'
            self.decimal = ','
        fmt = ROW_FMT.format('<', *columns)
        self.headers = fmt.format(*headers)
        self.cur_symbol = {
            'USD': '$',
            'EUR': u'€',
        }.get(currency)

    ___ number(self, n):
        n_int, n_float = divmod(abs(n), 100)
        n_int_parts    # list
        while n_int > 0:
            n_int, x = divmod(n_int, 1000)
            n_int_parts.insert(0, str(x))
        r.. '{}{}{:02}'.format(
            self.thousands.join(n_int_parts) o. '0',
            self.decimal,
            n_float,
        )

    ___ currency(self, change):
        r.. self.cur_fmt.format(
            self.lead_neg __ change < 0 ____ '',
            self.cur_symbol,
            self.number(change),
            self.trail_neg __ change < 0 ____ ' ',
        )

    ___ entry(self, entry):
        date, change, desc = entry
        fmt = ROW_FMT.format('>', *self.columns)
        r.. fmt.format(
            self.datefmt.format(date),
            truncate(desc),
            self.currency(change),
        )

    ___ table(self, entries):
        lines = [self.headers]
        lines.extend(map(self.entry, s..(entries)))
        r.. '\n'.join(lines)


___ create_entry(date, description, change):
    r.. (
        datetime.strptime(date, '%Y-%m-%d'),
        change,
        description
    )


___ format_entries(currency, locale, entries):
    columns = (10, 25, 13)
    lcinfo = LCInfo(locale, currency, columns)
    r.. lcinfo.table(entries)
