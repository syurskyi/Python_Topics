_______ unittest
_______ j__

____ rest_api _______ RestAPI


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.1

c_ RestAPITest(unittest.TestCase
    ___ test_no_users
        database {"users":    # list}
        api RestAPI(database)
        response api.g.. '/users')
        assertDictEqual(j__.l.. (response), database)

    ___ test_add_user
        database {"users":    # list}
        api RestAPI(database)
        payload j__.d..{
            'user': 'Adam'
        })
        response api.p.. '/add', payload)
        e.. {
            'name': 'Adam',
            'owes': {},
            'owed_by': {},
            'balance': 0
        }
        assertDictEqual(j__.l.. (response), e..)

    ___ test_get_single_user
        database {
            'users': [
                {
                    'name': 'Adam',
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                },
                {
                    'name': 'Bob',
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                }
            ]
        }
        api RestAPI(database)
        payload j__.d..{
            'users':  'Bob'
        })
        response api.g.. '/users', payload)
        e.. {
            'users': [
                {
                    'name': 'Bob',
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                }
            ]
        }
        assertDictEqual(j__.l.. (response), e..)

    ___ test_iou_both_users_have_0_balance
        database {
            'users': [
                {
                    'name': 'Adam',
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                },
                {
                    'name': 'Bob',
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                }
            ]
        }
        api RestAPI(database)
        payload j__.d..{
            'lender': 'Adam',
            'borrower': 'Bob',
            'amount': 3
        })
        response api.p.. '/iou', payload)
        e.. {
            'users': [
                {
                    'name': 'Adam',
                    'owes': {},
                    'owed_by': {
                        'Bob': 3
                    },
                    'balance': 3
                },
                {
                    'name': 'Bob',
                    'owes': {
                        'Adam': 3
                    },
                    'owed_by': {},
                    'balance': -3
                }
            ]
        }
        assertDictEqual(j__.l.. (response), e..)

    ___ test_borrower_has_negative_balance
        database {
            'users': [
                {
                    'name': 'Adam',
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                },
                {
                    'name': 'Bob',
                    'owes': {
                        'Chuck': 3
                    },
                    'owed_by': {},
                    'balance': -3
                },
                {
                    'name': 'Chuck',
                    'owes': {},
                    'owed_by': {
                        'Bob': 3
                    },
                    'balance': 3
                }
            ]
        }
        api RestAPI(database)
        payload j__.d..{
            'lender': 'Adam',
            'borrower': 'Bob',
            'amount': 3
        })
        response api.p.. '/iou', payload)
        e.. {
            'users': [
                {
                    'name': 'Adam',
                    'owes': {},
                    'owed_by': {
                        'Bob': 3
                    },
                    'balance': 3
                },
                {
                    'name': 'Bob',
                    'owes': {
                        'Adam': 3,
                        'Chuck': 3
                    },
                    'owed_by': {},
                    'balance': -6
                }
            ]
        }
        assertDictEqual(j__.l.. (response), e..)

    ___ test_lender_has_negative_balance
        database {
            'users': [
                {
                    'name': 'Adam',
                    'owes': {},
                    'owed_by': {},
                    'balance': 0
                },
                {
                    'name': 'Bob',
                    'owes': {
                        'Chuck': 3
                    },
                    'owed_by': {},
                    'balance': -3
                },
                {
                    'name': 'Chuck',
                    'owes': {},
                    'owed_by': {
                        'Bob': 3
                    },
                    'balance': 3
                }
            ]
        }
        api RestAPI(database)
        payload j__.d..{
            'lender': 'Bob',
            'borrower': 'Adam',
            'amount': 3
        })
        response api.p.. '/iou', payload)
        e.. {
            'users': [
                {
                    'name': 'Adam',
                    'owes': {
                        'Bob': 3
                    },
                    'owed_by': {},
                    'balance': -3
                },
                {
                    'name': 'Bob',
                    'owes': {
                        'Chuck': 3
                    },
                    'owed_by': {
                        'Adam': 3
                    },
                    'balance': 0
                }
            ]
        }
        assertDictEqual(j__.l.. (response), e..)

    ___ test_lender_owes_borrower
        database {
            "users": [
                {
                    "name": "Adam",
                    "owes": {
                        "Bob": 3.0
                    },
                    "owed_by": {},
                    "balance": -3.0
                },
                {
                    "name": "Bob",
                    "owes": {},
                    "owed_by": {
                        "Adam": 3.0
                    },
                    "balance": 3.0
                }
            ]
        }
        api RestAPI(database)
        payload j__.d..{
            'lender': 'Adam',
            'borrower': 'Bob',
            'amount': 2
        })
        response api.p.. '/iou', payload)
        e.. {
            'users': [
                {
                    "name": "Adam",
                    "owes": {
                        "Bob": 1.0
                    },
                    "owed_by": {},
                    "balance": -1.0
                },
                {
                    "name": "Bob",
                    "owes": {},
                    "owed_by": {
                        "Adam": 1.0
                    },
                    "balance": 1.0
                }
            ]
        }
        assertDictEqual(j__.l.. (response), e..)

    ___ test_lender_owes_borrower_less_than_new_loan
        database {
            "users": [
                {
                    "name": "Adam",
                    "owes": {
                        "Bob": 3.0
                    },
                    "owed_by": {},
                    "balance": -3.0
                },
                {
                    "name": "Bob",
                    "owes": {},
                    "owed_by": {
                        "Adam": 3.0
                    },
                    "balance": 3.0
                }
            ]
        }
        api RestAPI(database)
        payload j__.d..{
            'lender': 'Adam',
            'borrower': 'Bob',
            'amount': 4.0
        })
        response api.p.. '/iou', payload)
        e.. {
            'users': [
                {
                    "name": "Adam",
                    "owes": {
                    },
                    "owed_by": {
                        "Bob": 1.0
                    },
                    "balance": 1.0
                },
                {
                    "name": "Bob",
                    "owes": {
                        "Adam": 1.0
                    },
                    "owed_by": {
                    },
                    "balance": -1.0
                }
            ]
        }
        assertDictEqual(j__.l.. (response), e..)

    ___ test_lender_owes_borrower_same_as_new_loan
        database {
            "users": [
                {
                    "name": "Adam",
                    "owes": {
                        "Bob": 3.0
                    },
                    "owed_by": {},
                    "balance": -3.0
                },
                {
                    "name": "Bob",
                    "owes": {},
                    "owed_by": {
                        "Adam": 3.0
                    },
                    "balance": 3.0
                }
            ]
        }
        api RestAPI(database)
        payload j__.d..{
            'lender': 'Adam',
            'borrower': 'Bob',
            'amount': 3.0
        })
        response api.p.. '/iou', payload)
        e.. {
            'users': [
                {
                    "name": "Adam",
                    "owes": {
                    },
                    "owed_by": {
                    },
                    "balance": 0.0
                },
                {
                    "name": "Bob",
                    "owes": {
                    },
                    "owed_by": {
                    },
                    "balance": 0.0
                }
            ]
        }
        assertDictEqual(j__.l.. (response), e..)


__ _____ __ _____
    unittest.main()
