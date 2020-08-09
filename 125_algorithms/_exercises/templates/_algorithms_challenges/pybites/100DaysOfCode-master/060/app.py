#!python3

from flask ______ Flask, render_template, request, session, redirect, url_for, escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
___ index(
    __ request.method __ 'POST' and 'wage' in request.form:
        session['wage'] = float(request.form.get('wage'))
        r_ redirect(url_for('pay_calc'))
    r_ render_template("index.html")

@app.route('/pay', methods=['GET', 'POST'])
___ pay_calc(
    pay = ''
    __ request.method __ 'POST' and 'hours' in request.form and 'wage' in session:
        hours = float(request.form.get('hours'))
        pay = calc_wage(session['wage'], hours)
        #pay = (session['wage'] * hours)
    r_ render_template("pay_calc.html",
                            pay=pay)
						   

___ calc_wage(wage, hours
    r_ (wage * hours)

app.secret_key = "Test_Secret_Key"
app.run()