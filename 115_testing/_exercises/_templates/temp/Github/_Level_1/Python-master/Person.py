
c_ Person:
    name _ []

    ___ set_name  user_name):
        name.append(user_name)
        r_ len(name) - 1

    ___ get_name  user_id):
        if user_id >_ len(name):
            r_ 'There is no such user'
        else:
            r_ name[user_id]


if __name__ == '__main__':
    person _ Person()
    print('User Abbas has been added with id ', person.set_name('Abbas'))
    print('User associated with id 0 is ', person.get_name(0))