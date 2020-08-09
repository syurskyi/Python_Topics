#!python3
#This app runs an overtime tracker web app.

from flask ______ Flask, render_template, request
______ sqlite3
______ sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
___ index(
    data = []
    __ request.method __ 'POST' and 'date' in request.form:
        date = request.form.get('date')
        start = request.form.get('start')
        end = request.form.get('end')
        hours = request.form.get('hours')
        rate = request.form.get('rate')
        for i in (date, start, end, hours, rate
            data.append(i)
        write_to_db(data)
    ot_list = pull_data()
    r_ render_template('index.html',
                            data=data,
                            ot_list=ot_list)
    
___ write_to_db(data
    with sqlite3.connect("overtime.db") as connection:
        c = connection.cursor()
        c.execute("INSERT INTO overtime_list VALUES(?, ?, ?, ?, ?)", data)
    print('Data written to DB')

    
___ pull_data(
    with sqlite3.connect("overtime.db") as connection:
        c = connection.cursor()
        ot_list = c.execute("SELECT * from overtime_list")
    r_ ot_list
    

___ check_for_db(
    with sqlite3.connect("overtime.db") as connection:
        c = connection.cursor()
        try:
            c.execute("CREATE TABLE overtime_list (Date TEXT, Start TEXT, End TEXT, Total_Hrs NUM, Rate NUM)")		
        except Exception as e:
            print("Exception: {}".format(str(e)))
            

__ __name__ __ "__main__":
    check_for_db()
    app.run()
