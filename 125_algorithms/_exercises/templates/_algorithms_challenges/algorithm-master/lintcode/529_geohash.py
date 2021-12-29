"""
main concept is in `../module/geohash.py`
"""


class GeoHash:
    base32    # list

    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    ___ encode(self, latitude, longitude, precision=5):
        __ n.. self.base32:
            self.base32 = self.get_base32_list()

        times = (precision * 5) // 2 + 1
        lat_codes = self._loc_to_bins( latitude, times,  -90,  90)
        lng_codes = self._loc_to_bins(longitude, times, -180, 180)

        bin_codes    # list
        ___ i __ r..(times):
            bin_codes.extend((str(lng_codes[i]), str(lat_codes[i])))

        hash_codes    # list
        hash_code = ''
        ___ i __ r..(0, l..(bin_codes), 5):
            hash_code = int(''.join(bin_codes[i : i + 5]), 2)
            hash_codes.a..(self.base32[hash_code])

        r.. ''.join(hash_codes[:precision])

    ___ _loc_to_bins(self, location, times, left, right):
        mid = 0
        bins    # list

        ___ i __ r..(times):
            mid = left + (right - left) / 2.0
            __ location > mid:
                left = mid
                bins.a..(1)
            ____:
                right = mid
                bins.a..(0)

        r.. bins

    ___ get_base32_list(self):
        base32_list = [str(i) ___ i __ r..(10)]

        ignored_char = (ord('a'), ord('i'), ord('l'), ord('o'))
        ___ i __ r..(ord('a'), ord('z') + 1):
            __ i __ ignored_char:
                continue
            base32_list.a..(chr(i))

        r.. base32_list
