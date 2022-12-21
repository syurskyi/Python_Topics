c_ Solution o..
    ___ getHint  secret, guess
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        check  # dict
        ls = l.. secret)
        bull, cow = 0, 0
        different =    # list
        ___ i __ r.. ls
            __ guess[i] __ secret[i]:
                bull += 1
            ____
                # store possible index and count for cow
                different.append(i)
                try:
                    check[secret[i]] += 1
                except KeyError:
                    check[secret[i]] = 1
        ___ i __ different:
            try:
                __ check[guess[i]] > 0:
                    cow += 1
                    check[guess[i]] -= 1
            except:
                pass
        r_ "%dA%dB" % (bull, cow)


__ __name__ __ "__main__":
    s  ?
    print s.getHint("1122", "1222")
