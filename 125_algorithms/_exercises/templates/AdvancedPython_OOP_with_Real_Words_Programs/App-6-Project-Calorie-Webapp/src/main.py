____ flask.views _____ MethodView
____ wtforms _____ Form, StringField, SubmitField
____ flask _____ Flask, render_template, request
____ calorie _____ Calorie
____ temperature _____ Temperature

app = Flask(__name__)


c_ HomePage(MethodView):

    ___ get _
        r_ render_template('index.html')


c_ CaloriesFormPage(MethodView):

    ___ get _
        calories_form = CaloriesForm()

        r_ render_template('calories_form_page.html',
                               caloriesform=calories_form)

    ___ post _
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(country=calories_form.country.data,
                                  city=calories_form.city.data).get()

        calorie = Calorie(weight=f__(calories_form.weight.data),
                          height=f__(calories_form.height.data),
                          age=f__(calories_form.age.data),
                          temperature=temperature)

        calories = calorie.calculate()

        r_ render_template('calories_form_page.html',
                               caloriesform=calories_form,
                               calories=calories,
                               result=True)


c_ CaloriesForm(Form):
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ", default=175)
    age = StringField("Age: ", default=32)
    country = StringField("Country: ", default='USA')
    city = StringField("City: ", default="San Francisco")
    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)
