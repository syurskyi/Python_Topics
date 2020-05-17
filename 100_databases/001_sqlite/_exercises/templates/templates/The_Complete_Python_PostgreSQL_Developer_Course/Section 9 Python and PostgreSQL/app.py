from user _____ User
from database _____ Database

Database.initialise(database_"learning", user_"syurskyi", password_"1234", host_"localhost")

user _ User('jose@schoolofcode.me', 'Jose', 'Salvatierra')

user.save_to_db()

user_from_db _ User.load_from_db_by_email('jose@schoolofcode.me')

print(user_from_db)
