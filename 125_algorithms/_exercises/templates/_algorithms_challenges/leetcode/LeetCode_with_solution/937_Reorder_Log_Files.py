c_ Solution o..
    # def reorderLogFiles(self, logs):
    #     """
    #     :type logs: List[str]
    #     :rtype: List[str]
    #     """
    #     def f(log):
    #         id_, rest = log.split(" ", 1)
    #         return (0, rest, id_) if rest[0].isalpha() else (1,)
        
    #     # Python sort is stable, so digit with keep their order
    #     return sorted(logs, key = f)

    ___ reorderLogFiles  logs):
        letter_logs =    # list
        digit_logs =    # list
        ___ log __ logs:
            __ log.split(' ')[1].isnumeric():
                digit_logs.append(log)
            ____
                letter_logs.append(log)
        r_ sorted(letter_logs, key=lambda x: x.split(' ')[1:] + x.split(' ')[0]) + digit_logs
        