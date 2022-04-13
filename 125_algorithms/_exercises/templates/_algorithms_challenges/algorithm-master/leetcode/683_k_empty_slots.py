"""
>>> gotcha = []
>>> for s in (Solution(), Solution2()):
...     for _in, _out in (
...         (([1,3,2], 1), 2),
...         (([1,2,3], 1), -1),
...     ):
...         res = s.kEmptySlots(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""
_______ b__


c_ Solution:
    """
    Maintain pos by bloom order
    """
    ___ kEmptySlots  flowers, k
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        bloom    # list

        ___ day __ r..(l..(flowers:
            x flowers[day]
            i b__.bisect_left(bloom, x)
            ___ _x __ bloom[m..(0, i - 1i + 1]:
                __ a..(_x - x) - 1 __ k:
                    r.. day + 1  # changed to 1-based
            bloom.insert(i, x)

        r.. -1


c_ Solution2:
    """
    Two Pointer:
    https://blog.csdn.net/magicbean2/article/details/79235465
    """
    ___ kEmptySlots  flowers, k
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n l..(flowers)
        x2day [0] * n
        ___ day __ r..(n
            """
            day: 0-based => 1-based
            x:   1-based => 0-based
            """
            x flowers[day]
            x2day[x - 1] day + 1

        ans INF f__('inf')
        left, right 0, k + 1
        i 0

        w.... right < n:
            __ a__((
                x2day[i] < x2day[left],
                x2day[i] <_ x2day[right],
            :
                __ i __ right:
                    ans m..(ans, m..(x2day[left], x2day[right]
                left, right i, k + i + 1
            i += 1

        r.. ans __ ans < INF ____ -1
