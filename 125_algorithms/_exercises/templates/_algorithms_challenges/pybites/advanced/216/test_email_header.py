_______ i___

____ email_header _______ get_email_details, EMAIL_HEADER

OTHER_HEADER """
Return-Path: <info@pybit.es>
From: Bob & Julian from PyBites (info@pybit.es)
To: pybites@ninja.com
Subject: New regex learning path!
Date: Sun, 18 Aug 2019 17:16:10 -0700 (PDT)
Envelope-To: pybites@ninja.com
...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}
"""


___ test_source
    src i___.g.. get_email_details)
    ... 're.match' __ src o. 're.search' __ src
    ... 'groupdict' __ src


___ test_given_header
    a.. get_email_details(EMAIL_HEADER)
    e.. {'from': 'redacted-address',
                'to': 'redacted-address',
                'subject': 'A Test From SendGrid',
                'date': 'Wed, 19 Jun 2013 17:09:33'}
    ... a.. __ e..


___ test_other_header
    a.. get_email_details(OTHER_HEADER)
    e.. {'from': 'Bob & Julian from PyBites (info@pybit.es)',
                'to': 'pybites@ninja.com',
                'subject': 'New regex learning path!',
                'date': 'Sun, 18 Aug 2019 17:16:10'}
    ... a.. __ e..


___ test_no_match
    ... get_email_details('bogus') __ N..
