# Import the SQLite3 module
_____ ?

db _ ?.c..(':memory:')
c _ db.c..
script _ '''C.. T.. users(id IN.. P.. K.., name T..., phone T...);
            C.. T.. accounts(id IN.. P.. K.., description T...);

            INSERT INTO users(name, phone) VALUES ('John', '5557241'), 
             ('Adam', '5547874'), ('Jack', '5484522');'''
c.executescript(script)

# Print the results
c.e..('''SELECT * FROM users''')
___ row __ c:
    print(row)

db.c..
