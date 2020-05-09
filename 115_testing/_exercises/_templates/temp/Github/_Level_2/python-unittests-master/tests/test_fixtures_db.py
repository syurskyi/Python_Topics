______ sqlite3
______ u__

____ app ______ app_with_db


c_ AppWithDBTests?.?

    ___ setUp
        conn _ sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE blog (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, text TEXT)")

    ___ tearDown
        conn.close()

    ___ test_entry_creation
        app_with_db.create_blog_entry(db_conn, title_"pytest", text_"Pytest is awesome!")
