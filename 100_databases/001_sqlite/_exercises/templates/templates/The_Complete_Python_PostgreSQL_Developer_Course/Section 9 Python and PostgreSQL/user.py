from database _____ CursorFromConnectionPool

class User:
    ___ __init__(self, email, first_name, last_name, id_None):
        self.email _ email
        self.first_name _ first_name
        self.last_name _ last_name
        self.id _ id

    ___ __repr__(self):
        r_ "<User {}>".f..(self.email)

    ___ save_to_db(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() __ cursor:
            cursor.e..('I.. I.. users (email, first_name, last_name) V.. (%s, %s, %s)',
                            (self.email, self.first_name, self.last_name))

    @classmethod
    ___ load_from_db_by_email(cls, email):
        with CursorFromConnectionPool() __ cursor:
            # Note the (email,) to make it a tuple!
            cursor.e..('S.. * F.. users WHERE email=%s', (email,))
            user_data _ cursor.f_o..
            r_ cls(email_user_data[1], first_name_user_data[2], last_name_user_data[3], id_user_data[0])
