def create_blog_entry(db, title, text):
    query = "INSERT INTO blog (title, text) VALUES (?, ?)"
    values = (title, text)
    db.execute(query, values)
