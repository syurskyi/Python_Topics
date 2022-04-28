# ____ c.. _______ n..
# ____ d__ _______ d__
# _______ i..
#
# Composer n.. 'Composer', 'name born died'
# Opera n.. 'Opera', 'author play date'
#
# composers
#     "beethoven": ? "Ludwig van Beethoven",
#                           "17 December 1770", "26 March 1827"),
#     "wagner": ? "Richard Wagner",
#                        "22 May 1813", "13 February 1883"),
#     "verdi": ? "Giuseppe Verdi",
#                       "9 October 1813", "27 January 1901"),
#     "mozart": ? "Wolfgang Amadeus Mozart",
#                        "27 January 1756", "5 December 1791"),
#
#
# operas
#     ? "mozart", "Apollo and Hyacinth", "13 May 1767"),
#     ? "mozart", "Marriage of Figaro", "1 May 1786"),
#     ? "mozart", "Don Giovanni", "29 October 1787"),
#     ? "mozart", "Così fan tutte", "6 January 1790"),
#     ? "mozart", "The Clemency of Titus", "6 September 1791"),
#     ? "mozart", "The Magic Flute", "30 September 1791"),
#     ? "wagner", "The Fairies", "29 June 1888"),
#     ? "wagner", "Rienzi", "20 October 1842"),
#     ? "wagner", "The Flying Dutchman", "2 January 1843"),
#     ? "wagner", "Tannhäuser", "19 October 1845"),
#     ? "wagner", "Lohengrin", "28 August 1850"),
#     ? "wagner", "The Rhinegold", "22 September 1869"),
#     ? "wagner", "The Valkyrie", "26 June 1870"),
#     ? "wagner", "Siegfried", "16 August 1876"),
#     ? "wagner", "Twilight of the Gods", "17 August 1876"),
#     ? "wagner", "Tristan and Isolde", "10 June 1865"),
#     ? "wagner", "The Master-Singers of Nuremberg", "21 June 1868"),
#     ? "wagner", "Parsifal", "26 July 1882"),
#     ? "beethoven", "Fidelio", "20 November 1805"),
#     ? "verdi", "Nabucco", "9 March 1842"),
#     ? "verdi", "Ernani", "9 March 1844"),
#     ? "verdi", "Macbeth", "14 March 1847"),
#     ? "verdi", "Il corsaro", "25 October 1848"),
#     ? "verdi", "Rigoletto", "11 March 1851"),
#     ? "verdi", "La traviata", "6 March 1853"),
#     ? "verdi", "Aroldo", "16 August 1857"),
#     ? "verdi", "Macbeth", "21 April 1865"),
#     ? "verdi", "Don Carlos", "11 March 1867"),
#     ? "verdi", "Aida", "24 December 1871"),
#     ? "verdi", "Otello", "5 February 1887"),
#     ? "verdi", "Falstaff", "9 February 1893"),
#
#
#
# ___ _get_date date_str
#     r.. d__.d.. d__.s.. ? _d _B _Y
#
#
# ___ operas_both_at_premiere guest composer
#     """Retrieves a list of titles of operas, where the guest and the composer
#        could have been together at premiere.
#
#        That is the Opera.author matches the composer passed in, and both guest
#        and composer are alive at the time of Opera.date.
#
#        If guest and/or composer are not in the composers dict, raise a
#        ValueError
#
#        Args:
#        guest (str): one of the composers but not the author of an opera
#        composer (str): the author of an opera
#
#        Returns a list (or generator) of titles of operas.
#     """
#
#
#     __ composer n.. __ ? o. ? n.. __ ?
#         r.. V... "Both composer and guest must be valid composers"
#
#
#     guest c.. ?
#     composer_name ?
#     composer c.. ?
#
#     guest_birthday _? g__.b..
#     guest_death_day _? g__.d..
#
#     composer_death_day _? c__.d..
#
#
#
#     ___ opera __ f.. l.... x ?.a.. __ c.. o..
#         play_date _? ?.d..
#         __ g.. <_ ? < g.. a.. c.. > ?
#             y.. ?.p..
#
#
#
#
#
