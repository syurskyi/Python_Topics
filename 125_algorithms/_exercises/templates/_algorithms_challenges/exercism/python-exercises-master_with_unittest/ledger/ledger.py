# -*- coding: utf-8 -*-
____ d__ _______ d__


c_ LedgerEntry(o..
    ___ -
        date N..
        description N..
        change N..


___ create_entry(date, description, change
    entry LedgerEntry()
    entry.date d__.s..(date, '_Y-%m-_d')
    entry.description description
    entry.change change
    r.. entry


___ format_entries(currency, locale, entries
    __ locale __ 'en_US':
        # Generate Header Row
        table 'Date'
        ___ _ __ r..(7
            table += ' '
        table += '| Description'
        ___ _ __ r..(15
            table += ' '
        table += '| Change'
        ___ _ __ r..(7
            table += ' '

        w.... l..(entries) > 0
            table += '\n'

            # Find next entry in order
            min_entry_index -1
            ___ i __ r..(l..(entries:
                entry entries[i]
                __ min_entry_index < 0:
                    min_entry_index i
                    _____
                min_entry entries[min_entry_index]
                __ entry.date < min_entry.date:
                    min_entry_index i
                    _____
                __ (
                    entry.date __ min_entry.date a..
                    entry.change < min_entry.change

                    min_entry_index i
                    _____
                __ (
                    entry.date __ min_entry.date a..
                    entry.change __ min_entry.change a..
                    entry.description < min_entry.description

                    min_entry_index i
                    _____
            entry entries[min_entry_index]
            entries.p.. min_entry_index)

            # Write entry date to table
            month entry.date.month
            month s..(month)
            __ l..(month) < 2:
                month '0' + month
            date_str month
            date_str += '/'
            day entry.date.day
            day s..(day)
            __ l..(day) < 2:
                day '0' + day
            date_str += day
            date_str += '/'
            year entry.date.year
            year s..(year)
            w.... l..(year) < 4:
                year '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            __ l..(entry.description) > 25:
                ___ i __ r..(22
                    table += entry.description[i]
                table += '...'
            ____
                ___ i __ r..(25
                    __ l..(entry.description) > i:
                        table += entry.description[i]
                    ____
                        table += ' '
            table += ' | '

            # Write entry change to table
            __ currency __ 'USD':
                change_str ''
                __ entry.change < 0:
                    change_str '('
                change_str += '$'
                change_dollar a..(i..(entry.change / 100.0
                dollar_parts    # list
                w.... change_dollar > 0
                    dollar_parts.insert(0, s..(change_dollar % 1000
                    change_dollar change_dollar // 1000
                __ l..(dollar_parts) __ 0:
                    change_str += '0'
                ____
                    w... T...
                        change_str += dollar_parts[0]
                        dollar_parts.p.. 0)
                        __ l..(dollar_parts) __ 0:
                            _____
                        change_str += ','
                change_str += '.'
                change_cents a..(entry.change) % 100
                change_cents s..(change_cents)
                __ l..(change_cents) < 2:
                    change_cents '0' + change_cents
                change_str += change_cents
                __ entry.change < 0:
                    change_str += ')'
                ____
                    change_str += ' '
                w.... l..(change_str) < 13:
                    change_str ' ' + change_str
                table += change_str
            ____ currency __ 'EUR':
                change_str ''
                __ entry.change < 0:
                    change_str '('
                change_str += u'€'
                change_euro a..(i..(entry.change / 100.0
                euro_parts    # list
                w.... change_euro > 0
                    euro_parts.insert(0, s..(change_euro % 1000
                    change_euro change_euro // 1000
                __ l..(euro_parts) __ 0:
                    change_str += '0'
                ____
                    w... T...
                        change_str += euro_parts[0]
                        euro_parts.p.. 0)
                        __ l..(euro_parts) __ 0:
                            _____
                        change_str += ','
                change_str += '.'
                change_cents a..(entry.change) % 100
                change_cents s..(change_cents)
                __ l..(change_cents) < 2:
                    change_cents '0' + change_cents
                change_str += change_cents
                __ entry.change < 0:
                    change_str += ')'
                ____
                    change_str += ' '
                w.... l..(change_str) < 13:
                    change_str ' ' + change_str
                table += change_str
        r.. table
    ____ locale __ 'nl_NL':
        # Generate Header Row
        table 'Datum'
        ___ _ __ r..(6
            table += ' '
        table += '| Omschrijving'
        ___ _ __ r..(14
            table += ' '
        table += '| Verandering'
        ___ _ __ r..(2
            table += ' '

        w.... l..(entries) > 0
            table += '\n'

            # Find next entry in order
            min_entry_index -1
            ___ i __ r..(l..(entries:
                entry entries[i]
                __ min_entry_index < 0:
                    min_entry_index i
                    _____
                min_entry entries[min_entry_index]
                __ entry.date < min_entry.date:
                    min_entry_index i
                    _____
                __ (
                    entry.date __ min_entry.date a..
                    entry.change < min_entry.change

                    min_entry_index i
                    _____
                __ (
                    entry.date __ min_entry.date a..
                    entry.change __ min_entry.change a..
                    entry.description < min_entry.description

                    min_entry_index i
                    _____
            entry entries[min_entry_index]
            entries.p.. min_entry_index)

            # Write entry date to table
            day entry.date.day
            day s..(day)
            __ l..(day) < 2:
                day '0' + day
            date_str day
            date_str += '-'
            month entry.date.month
            month s..(month)
            __ l..(month) < 2:
                month '0' + month
            date_str += month
            date_str += '-'
            year entry.date.year
            year s..(year)
            w.... l..(year) < 4:
                year '0' + year
            date_str += year
            table += date_str
            table += ' | '

            # Write entry description to table
            # Truncate if necessary
            __ l..(entry.description) > 25:
                ___ i __ r..(22
                    table += entry.description[i]
                table += '...'
            ____
                ___ i __ r..(25
                    __ l..(entry.description) > i:
                        table += entry.description[i]
                    ____
                        table += ' '
            table += ' | '

            # Write entry change to table
            __ currency __ 'USD':
                change_str '$ '
                __ entry.change < 0:
                    change_str += '-'
                change_dollar a..(i..(entry.change / 100.0
                dollar_parts    # list
                w.... change_dollar > 0
                    dollar_parts.insert(0, s..(change_dollar % 1000
                    change_dollar change_dollar // 1000
                __ l..(dollar_parts) __ 0:
                    change_str += '0'
                ____
                    w... T...
                        change_str += dollar_parts[0]
                        dollar_parts.p.. 0)
                        __ l..(dollar_parts) __ 0:
                            _____
                        change_str += '.'
                change_str += ','
                change_cents a..(entry.change) % 100
                change_cents s..(change_cents)
                __ l..(change_cents) < 2:
                    change_cents '0' + change_cents
                change_str += change_cents
                change_str += ' '
                w.... l..(change_str) < 13:
                    change_str ' ' + change_str
                table += change_str
            ____ currency __ 'EUR':
                change_str u'€ '
                __ entry.change < 0:
                    change_str += '-'
                change_euro a..(i..(entry.change / 100.0
                euro_parts    # list
                w.... change_euro > 0
                    euro_parts.insert(0, s..(change_euro % 1000
                    change_euro change_euro // 1000
                __ l..(euro_parts) __ 0:
                    change_str += '0'
                ____
                    w... T...
                        change_str += euro_parts[0]
                        euro_parts.p.. 0)
                        __ l..(euro_parts) __ 0:
                            _____
                        change_str += '.'
                change_str += ','
                change_cents a..(entry.change) % 100
                change_cents s..(change_cents)
                __ l..(change_cents) < 2:
                    change_cents '0' + change_cents
                change_str += change_cents
                change_str += ' '
                w.... l..(change_str) < 13:
                    change_str ' ' + change_str
                table += change_str
        r.. table
