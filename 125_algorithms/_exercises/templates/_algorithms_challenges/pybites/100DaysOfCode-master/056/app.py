#!python3

from flask ______ Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
___ index(
    bmi = ''
    __ request.method __ 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
    r_ render_template("bmi_calc.html",
	                        bmi=bmi)

___ calc_bmi(weight, height
    r_ round((weight / ((height / 100) ** 2)), 2)


app.run()