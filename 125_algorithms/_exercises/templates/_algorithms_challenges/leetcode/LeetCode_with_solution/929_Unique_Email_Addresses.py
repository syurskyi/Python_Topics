c_ Solution o..
    ___ numUniqueEmails  emails
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = s..()
        ___ email __ emails:
            elements = email.split('@')
            email_set.add(elements[0].split('+')[0].replace('.', '') + elements[1])
        r_ l.. email_set)
