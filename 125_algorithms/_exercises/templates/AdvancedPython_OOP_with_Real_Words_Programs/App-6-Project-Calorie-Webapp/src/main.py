____ flask.views _____ MethodView
____ wtforms _____ Form, StringField, SubmitField
____ flask _____ Flask, render_template, request
____ calorie _____ Calorie
____ temperature _____ Temperature

app  Flask(__name__)


c_ HomePage(MethodView):

    ___ get _
        r_ render_template('index.html')


c_ CaloriesFormPage(MethodView):

    ___ get _
        calories_form  CaloriesForm()

        r_ render_template('calories_form_page.html',
                               caloriesformcalories_form)

    ___ post _
        calories_form  CaloriesForm(request.form)

        temperature  Temperature(countrycalories_form.country.data,
                                  citycalories_form.city.data).get()

        calorie  Calorie(weightf__(calories_form.weight.data),
                          heightf__(calories_form.height.data),
                          agef__(calories_form.age.data),
                          temperaturetemperature)

        calories  calorie.calculate()

        r_ render_template('calories_form_page.html',
                               caloriesformcalories_form,
                               caloriescalories,
                               resultTrue)


c_ CaloriesForm(Form):
    weight  StringField("Weight: ", default70)
    height  StringField("Height: ", default175)
    age  StringField("Age: ", default32)
    country  StringField("Country: ", default'USA')
    city  StringField("City: ", default"San Francisco")
    button  SubmitField("Calculate")


app.add_url_rule('/',
                 view_funcHomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_funcCaloriesFormPage.as_view('calories_form_page'))

app.run(debugTrue)
