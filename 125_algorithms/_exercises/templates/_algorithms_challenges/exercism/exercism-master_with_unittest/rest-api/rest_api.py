_______ json


c_ RestAPI(object):

    ___ - , database_ N..
        database = database

    # Description: List of user information
    # HTTP method: GET
    # URL: /users
    # Payload format: `{"users":["Adam","Bob"]}`
    # Response without payload: `{"users":<List of all User objects>}`
    # Response with payload: `{"users":<List of User objects for <users> (sorted by name)}`
    ___ get(self, url, payload_ N..
        __ payload __ N..
            # List of all User objects
            r.. json.dumps(database)

        # List of User objects for <users> (sorted by name)
        payload = json.loads(payload)
        usernames = payload['users']
        r.. json.dumps({'users': get_users(usernames)})

    ___ post(self, url, payload_ N..
        __ payload __ N..
            r.. ValueError("Payload must not be None.")

        payload = json.loads(payload)
        __ url __ '/add':
            r.. add(payload)
        ____ url __ '/iou':
            r.. iou(payload)

    # Private methods

    # Description: Create user
    # HTTP method: POST
    # URL: /add
    # Payload format: `{"user":<name of new user (unique)>}`
    # Response without payload: N/A
    # Response with payload: `<User object for new user>`
    ___ add(self, payload):
        username = payload['user']

        create_user(username)
        r.. json.dumps(get_user(username))

    # Description: Create IOU
    # HTTP method: POST
    # URL: /iou
    # Payload format: `{"lender":<name of lender>,"borrower":<name of
    # borrower>,"amount":5.25}`
    # Response without payload: N/A
    # Response with payload: `{"users":<updated User objects for <lender> and
    # <borrower> (sorted by name)>}`
    ___ iou(self, payload):
        lender_username = payload['lender']
        borrower_username = payload['borrower']
        amount = payload['amount']

        lender = get_user(lender_username)
        borrower = get_user(borrower_username)

        execute_iou(lender, borrower, amount)

        users = get_users([lender_username, borrower_username])
        r.. json.dumps({'users': users})

    ___ execute_iou(self, lender, borrower, amount):
        update_balance(lender, borrower, amount)

        __ n.. lender_owes_borrower(lender, borrower):
            execute_borrow(lender, borrower, amount)
        ____:
            # if lender owes borrower, pay off debt first then execute a borrow
            # if necessary.
            remaining_amount_to_borrow = pay_debt(lender, borrower,
                                                       amount)
            __ remaining_amount_to_borrow != 0:
                execute_borrow(lender, borrower,
                                    remaining_amount_to_borrow)

    ___ execute_borrow(self, lender, borrower, amount):
        lender['owed_by'].setdefault(borrower['name'], 0)
        lender['owed_by'][borrower['name']] += amount

        borrower['owes'].setdefault(lender['name'], 0)
        borrower['owes'][lender['name']] += amount

    ___ lender_owes_borrower(self, lender, borrower):
        r.. lender['owes'].get(borrower['name'], 0) != 0

    ___ pay_debt(self, lender, borrower, amount):
        debt = lender['owes'][borrower['name']]

        __ amount < debt:
            # debt can not be fully paid off so no additional amount will be
            # borrowed.
            lender['owes'][borrower['name']] -= amount
            borrower['owed_by'][lender['name']] -= amount
            r.. 0
        ____:
            # debt can be fully paid off and remaining amount will be borrowed.
            del lender['owes'][borrower['name']]
            del borrower['owed_by'][lender['name']]
            remaining_amount = amount - debt
            r.. remaining_amount

    ___ update_balance(self, lender, borrower, amount):
        lender['balance'] += amount
        borrower['balance'] -= amount

    ___ create_user(self, username):
        new_user = {
            'name': username,
            'owes': {},
            'owed_by': {},
            'balance': 0,
        }

        database['users'].a..(new_user)

    ___ get_users(self, usernames):
        users = [get_user(username) ___ username __ usernames]
        r.. s..(users, key=l.... user: user['name'])

    ___ get_user(self, username):
        users = database['users']
        ___ user __ users:
            __ user['name'] __ username:
                r.. user
