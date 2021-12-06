_______ datetime
_______ r__
_______ t___
____ _______ _______ T...
____ typing _______ List


c_ Account:
    ___  -  balance=0):
        balance = balance


___ maing___
    accounts = create_accounts()
    total = sum(a.balance ___ a __ accounts)

    validate_bank(accounts, total)
    print("Starting transfers...")

    jobs = [
        T...(t.._do_bank_stuff, args=(accounts, total)),
        T...(t.._do_bank_stuff, args=(accounts, total)),
        T...(t.._do_bank_stuff, args=(accounts, total)),
        T...(t.._do_bank_stuff, args=(accounts, total)),
        T...(t.._do_bank_stuff, args=(accounts, total)),
    ]

    t0 = datetime.datetime.now()

    [j.s.. ___ j __ jobs]
    [j.j... ___ j __ jobs]

    dt = datetime.datetime.now() - t0

    print("Transfers complete ({:,.2f}) sec".format(dt.total_seconds()))
    validate_bank(accounts, total)


___ do_bank_stuff(accounts, total):
    ___ _ __ r..(1, 10000):
        a1, a2 = get_two_accounts(accounts)
        amount = r__.r..(1, 100)
        do_transfer(a1, a2, amount)
        validate_bank(accounts, total, quiet=T..)


___ create_accounts() -> List[Account]:
    r_ [
        Account(balance=5000),
        Account(balance=10000),
        Account(balance=7500),
        Account(balance=7000),
        Account(balance=6000),
        Account(balance=9000),
    ]


___ do_transfer(from_account: Account, to_account: Account, amount: int):
    __ from_account.balance < amount:
        r_

    from_account.balance -= amount
    t___.s(.000)
    to_account.balance += amount


___ validate_bank(accounts: List[Account], total: int, quiet=False):
    current = sum(a.balance ___ a __ accounts)
    __ current != total:
        print("ERROR: Inconsistent account balance: ${:,} vs ${:,}".format(
            current, total
        ), flush=T..)
    elif n.. quiet:
        print("All good: Consistent account balance: ${:,}".format(
            total), flush=T..)


___ get_two_accounts(accounts):
    a1 = r__.choice(accounts)
    a2 = a1
    w.... a2 == a1:
        a2 = r__.choice(accounts)

    r_ a1, a2


__ __name__ == '__main__':
    main()
