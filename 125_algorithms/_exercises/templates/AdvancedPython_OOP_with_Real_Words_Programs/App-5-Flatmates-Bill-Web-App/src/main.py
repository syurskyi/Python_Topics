____ flask.views _____ MethodView
____ wtforms _____ Form, StringField, SubmitField
____ flask _____ Flask, render_template, request
____ flatmates_bill _____ flat

app = Flask(__name__)

c_ HomePage(MethodView):

    ___ get _
        r_ render_template('index.html')


c_ BillFormPage(MethodView):

    ___ get _
        bill_form = BillForm()
        r_ render_template('bill_form_page.html',
                               billform=bill_form)


c_ ResultsPage(MethodView):

    ___ post _
        billform = BillForm(request.form)

        the_bill = flat.Bill(f__(billform.amount.data), billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, f__(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, f__(billform.days_in_house2.data))


        r_ render_template('results.html',
                               name1=flatmate1.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(the_bill, flatmate1))


c_ BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="December 2020")

    name1 = StringField("Name: ", default="John")
    days_in_house1 = StringField("Days in the house: ", default=20)

    name2 = StringField("Name: ", default="Marry")
    days_in_house2 = StringField("Days in the house: ", default=12)

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form',
                 view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results',
                 view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)