# -*- coding: utf-8 -*-
____ datetime _______ datetime


class LedgerEntry(object):
    ___ __init__(self):
        self.date = N..
        self.description = N..
        self.change = N..


___ create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    r.. entry


___ format_entries(currency, locale, entries):
    __ locale __ 'en_US':
        # Generate Header Row
        table = 'Date'
        ___ _ __ r..(7):
            table += ' '
        table += '| Description'
        ___ _ __ r..(15):
            table += ' '
        table += '| Change'
        ___ _ __ r..(7):
            table += ' '

        while l..(entries) > 0:
            table += '\n'

            # Find next entry in order
            min_entry_index = -1
            ___ i __ r..(l..(entries)):
                entry = entries[i]
                __ min_entry_index < 0:
                    min_entry_index = i
                    continue
                min_entry = entries[min_entry_index]
                __ entry.date < min_entry.date:
                    min_entry_index = i
                    continue
                __ (
                    entry.date __ min_entry.date and
                    entry.change < min_entry.change
                ):
                    min_entry_index = i
                    continue
                __ (
                    entry.date __ min_entry.date and
                    entry.change __ min_entry.change and
                    entry.description < min_entry.description
                ):
                    min_entry_index = i
                    continue
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table
            month = entry.date.month
            month = str(month)
            __ l..(month) < 2:
                month = '0' + month
            date_str = month
            date_str += '/'
            day = entry.date.day
            day = str(day)
            __ l..(day) < 2:
                day = '0' + day
            date_str += day
            date_str += '/'
            year = entry.date.year
            year = str(year)
            while l..(year) < 4:
                year = '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            __ l..(entry.description) > 25:
                ___ i __ r..(22):
                    table += entry.description[i]
                table += '...'
            ____:
                ___ i __ r..(25):
                    __ l..(entry.description) > i:
                        table += entry.description[i]
                    ____:
                        table += ' '
            table += ' | '

            # Write entry change to table
            __ currency __ 'USD':
                change_str = ''
                __ entry.change < 0:
                    change_str = '('
                change_str += '$'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts    # list
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                __ l..(dollar_parts) __ 0:
                    change_str += '0'
                ____:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        __ l..(dollar_parts) __ 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                __ l..(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                __ entry.change < 0:
                    change_str += ')'
                ____:
                    change_str += ' '
                while l..(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            ____ currency __ 'EUR':
                change_str = ''
                __ entry.change < 0:
                    change_str = '('
                change_str += u'€'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts    # list
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                __ l..(euro_parts) __ 0:
                    change_str += '0'
                ____:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        __ l..(euro_parts) __ 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                __ l..(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                __ entry.change < 0:
                    change_str += ')'
                ____:
                    change_str += ' '
                while l..(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        r.. table
    ____ locale __ 'nl_NL':
        # Generate Header Row
        table = 'Datum'
        ___ _ __ r..(6):
            table += ' '
        table += '| Omschrijving'
        ___ _ __ r..(14):
            table += ' '
        table += '| Verandering'
        ___ _ __ r..(2):
            table += ' '

        while l..(entries) > 0:
            table += '\n'

            # Find next entry in order
            min_entry_index = -1
            ___ i __ r..(l..(entries)):
                entry = entries[i]
                __ min_entry_index < 0:
                    min_entry_index = i
                    continue
                min_entry = entries[min_entry_index]
                __ entry.date < min_entry.date:
                    min_entry_index = i
                    continue
                __ (
                    entry.date __ min_entry.date and
                    entry.change < min_entry.change
                ):
                    min_entry_index = i
                    continue
                __ (
                    entry.date __ min_entry.date and
                    entry.change __ min_entry.change and
                    entry.description < min_entry.description
                ):
                    min_entry_index = i
                    continue
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table
            day = entry.date.day
            day = str(day)
            __ l..(day) < 2:
                day = '0' + day
            date_str = day
            date_str += '-'
            month = entry.date.month
            month = str(month)
            __ l..(month) < 2:
                month = '0' + month
            date_str += month
            date_str += '-'
            year = entry.date.year
            year = str(year)
            while l..(year) < 4:
                year = '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            __ l..(entry.description) > 25:
                ___ i __ r..(22):
                    table += entry.description[i]
                table += '...'
            ____:
                ___ i __ r..(25):
                    __ l..(entry.description) > i:
                        table += entry.description[i]
                    ____:
                        table += ' '
            table += ' | '

            # Write entry change to table
            __ currency __ 'USD':
                change_str = '$ '
                __ entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts    # list
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                __ l..(dollar_parts) __ 0:
                    change_str += '0'
                ____:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        __ l..(dollar_parts) __ 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                __ l..(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while l..(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            ____ currency __ 'EUR':
                change_str = u'€ '
                __ entry.change < 0:
                    change_str += '-'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts    # list
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                __ l..(euro_parts) __ 0:
                    change_str += '0'
                ____:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        __ l..(euro_parts) __ 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                __ l..(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while l..(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        r.. table
