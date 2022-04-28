c_ Solution o..
    ___ canPlaceFlowers  flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        ___ i __ r.. l.. flowerbed)):
            curr = flowerbed[i]
            __ i - 1 >= 0:
                curr += flowerbed[i - 1]
            __ i + 1 < l.. flowerbed):
                curr += flowerbed[i + 1]
            __ curr __ 0:
                count += 1
                flowerbed[i] = 1
                __ count >= n:
                    r_ True
        r_ False
