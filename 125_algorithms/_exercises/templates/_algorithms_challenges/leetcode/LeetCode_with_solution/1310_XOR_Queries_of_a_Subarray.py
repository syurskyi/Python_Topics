c_ Solution:
    ___ xorQueries  arr: List[i..], queries: List[List[i..]])   List[i..]:
        pref = [0]
        # Compute accumulated xor from head
        ___ e __ arr:
            pref.a.. e ^ pref[-1])
        ans =    # list
        # query result equal to xor[0, l] xor x[0, r]
        ___ [l, r] __ queries:
            ans.a.. pref[r+1] ^ pref[l])
        r_ ans

    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    #     for i in range(len(arr) - 1):
    #         arr[i + 1] ^= arr[i]
    #     return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]
