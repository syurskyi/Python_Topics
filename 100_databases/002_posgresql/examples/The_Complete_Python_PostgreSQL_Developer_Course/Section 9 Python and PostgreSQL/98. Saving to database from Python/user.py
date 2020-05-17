import psycopg2


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}".format(self.email)

    def save_to_db(self):
        connection = psycopg2.connect(user='syurskyi', password='1234', database='learning', host='localhost')
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
            (self.email, self.first_name, self.last_name))
        connection.commit()
        connection.close()

