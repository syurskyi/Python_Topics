____ user _____ User
____ database _____ Database

Database.initialise(database_"learning", user_"syurskyi", password_"1234", host_"localhost")

user _ User('jose@schoolofcode.me', 'Jose', 'Salvatierra')

user.save_to_db()

user______db _ User.load______db_by_email('jose@schoolofcode.me')

print(user______db)
