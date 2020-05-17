from database _____ CursorFromConnectionPool

class User:
    def __init__(self, email, first_name, last_name, id_None):
        self.email _ email
        self.first_name _ first_name
        self.last_name _ last_name
        self.id _ id

    def __repr__(self):
        return "<User {}>".f..(self.email)

    def save_to_db(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() as cursor:
            cursor.e..('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                            (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionPool() as cursor:
            # Note the (email,) to make it a tuple!
            cursor.e..('SELECT * FROM users WHERE email=%s', (email,))
            user_data _ cursor.fetchone()
            return cls(email_user_data[1], first_name_user_data[2], last_name_user_data[3], id_user_data[0])
