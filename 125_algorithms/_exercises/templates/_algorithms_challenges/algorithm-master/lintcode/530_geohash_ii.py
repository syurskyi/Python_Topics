"""
main concept is in `../module/geohash.py`
"""


c_ GeoHash:
    base32    # list

    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    ___ decode  geohash
        __ n.. geohash:
            r.. []
        __ n.. base32:
            base32 get_base32_list()

        bin_codes    # list
        ___ char __ geohash:
            __ char n.. __ base32:
                r.. []
            bin_codes.e.. _oct_to_bins(base32.i.. char)))

        n l..(bin_codes)
        lat_codes [bin_codes[i] ___ i __ r..(1, n, 2)]
        lng_codes [bin_codes[i] ___ i __ r..(0, n, 2)]

        r.. [
            _bins_to_loc(lat_codes,  -90,  90),
            _bins_to_loc(lng_codes, -180, 180)
        ]

    ___ _bins_to_loc  bins, left, right
        mid 0

        ___ code __ bins:
            mid left + (right - left) / 2.0
            __ code:
                left mid
            ____
                right mid

        r.. left + (right - left) / 2.0

    ___ _oct_to_bins  val_in_oct
        bins    # list
        ___ i __ r..(5
            __ val_in_oct % 2:
                bins.a..(1)
            ____
                bins.a..(0)
            val_in_oct val_in_oct >> 1

        r.. r..(bins)

    ___ get_base32_list
        base32_list [s..(i) ___ i __ r..(10)]

        ignored_char (o..('a'), o..('i'), o..('l'), o..('o'
        ___ i __ r..(o..('a'), o..('z') + 1
            __ i __ ignored_char:
                _____
            base32_list.a..(chr(i

        r.. base32_list
