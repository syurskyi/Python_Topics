
c_ Person:
    name = []

    ___ set_name  user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    ___ get_name  user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]


if __name__ == '__main__':
    person = Person()
    print('User Abbas has been added with id ', person.set_name('Abbas'))
    print('User associated with id 0 is ', person.get_name(0))