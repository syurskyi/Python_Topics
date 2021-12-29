# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry(object):
    ___ __init__(self):
        self.date = None
        self.description = None
        self.change = None


___ create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


___ format_entries(currency, locale, entries):
    __ locale == 'en_US':
        # Generate Header Row
        table = 'Date'
        for _ in range(7):
            table += ' '
        table += '| Description'
        for _ in range(15):
            table += ' '
        table += '| Change'
        for _ in range(7):
            table += ' '

        while len(entries) > 0:
            table += '\n'

            # Find next entry in order
            min_entry_index = -1
            for i in range(len(entries)):
                entry = entries[i]
                __ min_entry_index < 0:
                    min_entry_index = i
                    continue
                min_entry = entries[min_entry_index]
                __ entry.date < min_entry.date:
                    min_entry_index = i
                    continue
                __ (
                    entry.date == min_entry.date and
                    entry.change < min_entry.change
                ):
                    min_entry_index = i
                    continue
                __ (
                    entry.date == min_entry.date and
                    entry.change == min_entry.change and
                    entry.description < min_entry.description
                ):
                    min_entry_index = i
                    continue
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table
            month = entry.date.month
            month = str(month)
            __ len(month) < 2:
                month = '0' + month
            date_str = month
            date_str += '/'
            day = entry.date.day
            day = str(day)
            __ len(day) < 2:
                day = '0' + day
            date_str += day
            date_str += '/'
            year = entry.date.year
            year = str(year)
            while len(year) < 4:
                year = '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            __ len(entry.description) > 25:
                for i in range(22):
                    table += entry.description[i]
                table += '...'
            else:
                for i in range(25):
                    __ len(entry.description) > i:
                        table += entry.description[i]
                    else:
                        table += ' '
            table += ' | '

            # Write entry change to table
            __ currency == 'USD':
                change_str = ''
                __ entry.change < 0:
                    change_str = '('
                change_str += '$'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                __ len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        __ len(dollar_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                __ len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                __ entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = ''
                __ entry.change < 0:
                    change_str = '('
                change_str += u'€'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                __ len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        __ len(euro_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                __ len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                __ entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        return table
    elif locale == 'nl_NL':
        # Generate Header Row
        table = 'Datum'
        for _ in range(6):
            table += ' '
        table += '| Omschrijving'
        for _ in range(14):
            table += ' '
        table += '| Verandering'
        for _ in range(2):
            table += ' '

        while len(entries) > 0:
            table += '\n'

            # Find next entry in order
            min_entry_index = -1
            for i in range(len(entries)):
                entry = entries[i]
                __ min_entry_index < 0:
                    min_entry_index = i
                    continue
                min_entry = entries[min_entry_index]
                __ entry.date < min_entry.date:
                    min_entry_index = i
                    continue
                __ (
                    entry.date == min_entry.date and
                    entry.change < min_entry.change
                ):
                    min_entry_index = i
                    continue
                __ (
                    entry.date == min_entry.date and
                    entry.change == min_entry.change and
                    entry.description < min_entry.description
                ):
                    min_entry_index = i
                    continue
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table
            day = entry.date.day
            day = str(day)
            __ len(day) < 2:
                day = '0' + day
            date_str = day
            date_str += '-'
            month = entry.date.month
            month = str(month)
            __ len(month) < 2:
                month = '0' + month
            date_str += month
            date_str += '-'
            year = entry.date.year
            year = str(year)
            while len(year) < 4:
                year = '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            __ len(entry.description) > 25:
                for i in range(22):
                    table += entry.description[i]
                table += '...'
            else:
                for i in range(25):
                    __ len(entry.description) > i:
                        table += entry.description[i]
                    else:
                        table += ' '
            table += ' | '

            # Write entry change to table
            __ currency == 'USD':
                change_str = '$ '
                __ entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                __ len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        __ len(dollar_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                __ len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = u'€ '
                __ entry.change < 0:
                    change_str += '-'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                __ len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        __ len(euro_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                __ len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        return table
