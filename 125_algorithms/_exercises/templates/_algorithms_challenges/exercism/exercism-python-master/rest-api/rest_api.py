______ json
from collections ______ defaultdict

class RestAPI(object
    ___ __init__(self, database=None
        self.database = database

    ___ _select_username(self, username
        ___ user in self.database['users']:
            __ user['name'] __ username:
                r_ user
    
    ___ lend(self, borrower_name, lender_name, amount
        borrower = self._select_username(borrower_name)
        lender = self._select_username(lender_name)

        __ lender_name in borrower['owed_by']:
            __ amount < borrower['owed_by'][lender_name]:
                borrower['owed_by'][lender_name] -= amount
            ____
                __ amount != borrower['owed_by'][lender_name]:
                    borrower['owes'][lender_name] = amount - borrower['owed_by'][lender_name]
                del borrower['owed_by'][lender_name]
        ____
            borrower['owes'][lender_name] = borrower['owes'].get(lender_name, 0) + amount
        borrower['balance'] -= amount

        __ borrower_name in lender['owes']:
            __ amount < lender['owes'][borrower_name]:
                lender['owes'][borrower_name] -= amount
            ____
                __ amount != lender['owes'][borrower_name]:
                    lender['owed_by'][borrower_name] = amount - lender['owes'][borrower_name]
                del lender['owes'][borrower_name]
        ____
            lender['owed_by'][borrower_name] = lender['owed_by'].get(borrower_name, 0) + amount
        lender['balance'] += amount


        r_ { 'users': sorted([lender, borrower], key=lambda v: v['name'])}

    ___ get(self, url, payload=None
        data = json.loads(payload) __ payload else None
        __ url __ '/users':
            __ payload pa__ None:
                result = self.database
            ____
                result = { 'users' : 
                    [self._select_username(data['users'])] }
        r_ json.dumps(result)


    ___ post(self, url, payload=None
        data = json.loads(payload)
        result = {}
        __ url __ '/add':
            result = {
                'name': data['user'],
                'owes': {},
                'owed_by': {},
                'balance': 0} 
            self.database[data['user']] = result
        ____ url __ '/iou':
            result = self.lend(data['borrower'], data['lender'], data['amount'])
        r_ json.dumps(result)
