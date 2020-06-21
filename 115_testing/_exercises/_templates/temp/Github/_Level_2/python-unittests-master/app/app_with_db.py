___ create_blog_entry(db, title, text
    query _ "INSERT INTO blog (title, text) VALUES (?, ?)"
    values _ (title, text)
    db.execute(query, values)
