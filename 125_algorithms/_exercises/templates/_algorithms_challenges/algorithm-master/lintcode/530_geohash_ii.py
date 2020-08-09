"""
main concept is in `../module/geohash.py`
"""


class GeoHash:
    base32 = []

    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    ___ decode(self, geohash
        __ not geohash:
            r_ []
        __ not self.base32:
            self.base32 = self.get_base32_list()

        bin_codes = []
        ___ char in geohash:
            __ char not in self.base32:
                r_ []
            bin_codes.extend(self._oct_to_bins(self.base32.index(char)))

        n = le.(bin_codes)
        lat_codes = [bin_codes[i] ___ i in range(1, n, 2)]
        lng_codes = [bin_codes[i] ___ i in range(0, n, 2)]

        r_ [
            self._bins_to_loc(lat_codes,  -90,  90),
            self._bins_to_loc(lng_codes, -180, 180)
        ]

    ___ _bins_to_loc(self, bins, left, right
        mid = 0

        ___ code in bins:
            mid = left + (right - left) / 2.0
            __ code:
                left = mid
            ____
                right = mid

        r_ left + (right - left) / 2.0

    ___ _oct_to_bins(self, val_in_oct
        bins = []
        ___ i in range(5
            __ val_in_oct % 2:
                bins.append(1)
            ____
                bins.append(0)
            val_in_oct = val_in_oct >> 1

        r_ reversed(bins)

    ___ get_base32_list(self
        base32_list = [str(i) ___ i in range(10)]

        ignored_char = (ord('a'), ord('i'), ord('l'), ord('o'))
        ___ i in range(ord('a'), ord('z') + 1
            __ i in ignored_char:
                continue
            base32_list.append(chr(i))

        r_ base32_list
