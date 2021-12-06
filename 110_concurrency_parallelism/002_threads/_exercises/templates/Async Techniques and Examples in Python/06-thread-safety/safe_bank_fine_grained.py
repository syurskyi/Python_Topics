_______ d___
_______ r__
_______ t___
____ _______ _______ T..., RLock
____ typing _______ List


c_ Account:
    ___  -  balance=0):
        balance = balance
        lock = R..


___ maing___
    accounts = create_accounts()
    total = sum(a.balance ___ a __ accounts)

    validate_bank(accounts, total)
    print("Starting transfers...")

    jobs = [
        T...(t.._do_bank_stuff, a.._(accounts, total)),
        T...(t.._do_bank_stuff, a.._(accounts, total)),
        T...(t.._do_bank_stuff, a.._(accounts, total)),
        T...(t.._do_bank_stuff, a.._(accounts, total)),
        T...(t.._do_bank_stuff, a.._(accounts, total)),
    ]

    t0 = d___.d___.now()

    [j.s.. ___ j __ jobs]
    [j.j... ___ j __ jobs]

    dt = d___.d___.now() - t0

    print("Transfers complete ({:,.2f}) sec".format(dt.total_seconds()))
    validate_bank(accounts, total)


___ do_bank_stuff(accounts, total):
    ___ _ __ r..(1, 10_000):
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

    lock1, lock2 = (
        (from_account.lock, to_account.lock)
        __ id(from_account) < id(to_account)
        ____ (to_account.lock, from_account.lock)
    )

    w___ lock1:
        w___ lock2:
            from_account.balance -= amount
            t___.s(.000)
            to_account.balance += amount


transfer_lock = R..


___ do_transfer_global_style(
        from_account: Account, to_account: Account, amount: int):
    __ from_account.balance < amount:
        r_

    w___ transfer_lock:
        from_account.balance -= amount
        t___.s(.000)
        to_account.balance += amount


___ validate_bank(accounts: List[Account], total: int, quiet=F..):
    # with transfer_lock:
    #     current = sum(a.balance for a in accounts)

    [a.lock.a.. ___ a __ accounts]
    current = sum(a.balance ___ a __ accounts)
    [a.lock.r..) ___ a __ accounts]

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
