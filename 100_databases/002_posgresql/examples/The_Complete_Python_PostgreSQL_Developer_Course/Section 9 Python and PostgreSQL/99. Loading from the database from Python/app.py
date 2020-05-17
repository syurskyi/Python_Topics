from user import User

my_user = User.load_from_db_by_email('sergejyurskyj@me.com')

print(my_user)
