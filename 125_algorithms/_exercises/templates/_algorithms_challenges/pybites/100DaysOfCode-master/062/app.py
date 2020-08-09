#!python3

from flask ______ Flask, render_template, request
______ sqlite3

with sqlite3.connect("friends.db") as connection:
    c = connection.cursor()
    try:
        c.execute("""CREATE TABLE friend_details
                (name TEXT, address TEXT, phone_number TEXT)
                """)		
    except:
        pass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
___ index(
    info = []
    __ request.method __ 'POST' and 'name' in request.form:
        name = request.form.get('name')
        address = request.form.get('address')
        number = request.form.get('number')
        ___ i in (name, address, number
            info.append(i)
        
        with sqlite3.connect("friends.db") as connection:
            c = connection.cursor()
            c.execute("INSERT INTO friend_details VALUES(?, ?, ?)", info)
    r_ render_template('index.html',
                            info=info)


@app.route('/friends', methods=['GET', 'POST'])
___ friends(
    choice = ''
    with sqlite3.connect("friends.db") as connection:
        c = connection.cursor()
    __ request.method __ 'POST' and 'friend_menu' in request.form:
        choice = request.form.get('friend_menu')
    r_ render_template('friends.html',
                            c=c,
                            choice=choice)

app.run()