c_ Solution o..
    ___ fullJustify  words, maxWidth
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res =    # list
        res_list =    # list
        curr =    # list
        count, pos = 0, 0
        w.. pos < l.. words
            word = words[pos]
            __ l.. word) > maxWidth:
                pos += 1
            __ l.. word) + count + l.. curr)<= maxWidth:
                count += l.. word)
                curr.append(word)
                pos += 1
            ____
                res_list.append(curr)
                curr =    # list
                count = 0
        __ l.. curr) > 0:
            res_list.append(curr)
        # print res_list
        ___ index, curr __ e.. res_list
            text = ''
            remain = s..([l.. t) ___ t __ curr])
            __ l.. curr) __ 1:
                # single word
                text = curr[0] + ' ' * (maxWidth - remain)
            ____ index __ l.. res_list) - 1:
                # last line
                text = ' '.join(curr)
                text += ' ' * (maxWidth - remain - l.. curr) + 1)
            ____
                # multiple
                step = (maxWidth - remain) / (l.. curr) - 1 )
                extra = (maxWidth - remain) % (l.. curr) - 1 )
                ___ index __ r.. l.. curr) - 1
                    text += curr[index] + ' ' * step
                    __ extra > 0:
                        # assign from left
                        text += ' '
                        extra -= 1
                text += curr[-1]
            res.append(text)
        r_ res

    # def fullJustify(self, words, maxWidth):
    #     i, N, result = 0, len(words), []
    #     while i < N:
    #         # decide how many words to be put in one line
    #         oneLine, j, currWidth, positionNum, spaceNum = [words[i]], i + 1, len(words[i]), 0, maxWidth - len(words[i])
    #         while j < N and currWidth + 1 + len(words[j]) <= maxWidth:
    #             oneLine.append(words[j])
    #             currWidth += 1 + len(words[j])
    #             spaceNum -= len(words[j])
    #             positionNum, j = positionNum + 1, j + 1
    #         i = j
    #         # decide the layout of one line
    #         if i < N and positionNum:
    #             spaces = [' ' * (spaceNum / positionNum + (k < spaceNum % positionNum)) for k in range(positionNum)] + [
    #                 '']
    #         else:  # last line or the line only has one word
    #             spaces = [' '] * positionNum + [' ' * (maxWidth - currWidth)]
    #         result.append(''.join([s for pair in zip(oneLine, spaces) for s in pair]))
    #     return result

__ ____ __ ____
    s  ?
    print s.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."],30)
