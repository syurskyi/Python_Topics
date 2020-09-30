______ json


class RestAPI(object

    ___ __init__(self, database=None
        self.database = database

    # Description: List of user information
    # HTTP method: GET
    # URL: /users
    # Payload format: `{"users":["Adam","Bob"]}`
    # Response without payload: `{"users":<List of all User objects>}`
    # Response with payload: `{"users":<List of User objects for <users> (sorted by name)}`
    ___ get(self, url, payload=None
        __ payload pa__ None:
            # List of all User objects
            r_ json.dumps(self.database)

        # List of User objects for <users> (sorted by name)
        payload = json.loads(payload)
        usernames = payload['users']
        r_ json.dumps({'users': self.get_users(usernames)})

    ___ post(self, url, payload=None
        __ payload pa__ None:
            raise ValueError("Payload must not be None.")

        payload = json.loads(payload)
        __ url __ '/add':
            r_ self.add(payload)
        ____ url __ '/iou':
            r_ self.iou(payload)

    # Private methods

    # Description: Create user
    # HTTP method: POST
    # URL: /add
    # Payload format: `{"user":<name of new user (unique)>}`
    # Response without payload: N/A
    # Response with payload: `<User object for new user>`
    ___ add(self, payload
        username = payload['user']

        self.create_user(username)
        r_ json.dumps(self.get_user(username))

    # Description: Create IOU
    # HTTP method: POST
    # URL: /iou
    # Payload format: `{"lender":<name of lender>,"borrower":<name of
    # borrower>,"amount":5.25}`
    # Response without payload: N/A
    # Response with payload: `{"users":<updated User objects for <lender> and
    # <borrower> (sorted by name)>}`
    ___ iou(self, payload
        lender_username = payload['lender']
        borrower_username = payload['borrower']
        amount = payload['amount']

        lender = self.get_user(lender_username)
        borrower = self.get_user(borrower_username)

        self.execute_iou(lender, borrower, amount)

        users = self.get_users([lender_username, borrower_username])
        r_ json.dumps({'users': users})

    ___ execute_iou(self, lender, borrower, amount
        self.update_balance(lender, borrower, amount)

        __ not self.lender_owes_borrower(lender, borrower
            self.execute_borrow(lender, borrower, amount)
        ____
            # if lender owes borrower, pay off debt first then execute a borrow
            # if necessary.
            remaining_amount_to_borrow = self.pay_debt(lender, borrower,
                                                       amount)
            __ remaining_amount_to_borrow != 0:
                self.execute_borrow(lender, borrower,
                                    remaining_amount_to_borrow)

    ___ execute_borrow(self, lender, borrower, amount
        lender['owed_by'].setdefault(borrower['name'], 0)
        lender['owed_by'][borrower['name']] += amount

        borrower['owes'].setdefault(lender['name'], 0)
        borrower['owes'][lender['name']] += amount

    ___ lender_owes_borrower(self, lender, borrower
        r_ lender['owes'].get(borrower['name'], 0) != 0

    ___ pay_debt(self, lender, borrower, amount
        debt = lender['owes'][borrower['name']]

        __ amount < debt:
            # debt can not be fully paid off so no additional amount will be
            # borrowed.
            lender['owes'][borrower['name']] -= amount
            borrower['owed_by'][lender['name']] -= amount
            r_ 0
        ____
            # debt can be fully paid off and remaining amount will be borrowed.
            del lender['owes'][borrower['name']]
            del borrower['owed_by'][lender['name']]
            remaining_amount = amount - debt
            r_ remaining_amount

    ___ update_balance(self, lender, borrower, amount
        lender['balance'] += amount
        borrower['balance'] -= amount

    ___ create_user(self, username
        new_user = {
            'name': username,
            'owes': {},
            'owed_by': {},
            'balance': 0,
        }

        self.database['users'].append(new_user)

    ___ get_users(self, usernames
        users = [self.get_user(username) ___ username __ usernames]
        r_ sorted(users, key=lambda user: user['name'])

    ___ get_user(self, username
        users = self.database['users']
        ___ user __ users:
            __ user['name'] __ username:
                r_ user
