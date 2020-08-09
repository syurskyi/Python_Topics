#!python3
#This is the application script for launching a Python Timezone List Flask Web App.

from flask ______ Flask, render_template, request
______ pendulum
______ pytz

app = Flask(__name__)

#Create the list to populate the pull-down menu
___ create_list(
    tz_list = []
    for tz in pytz.all_timezones:
        tz_list.append(tz)
    r_ tz_list


@app.route('/', methods=['GET', 'POST'])
___ index(
    tz_list = create_list()
    choice = ''
    tz_time = ''
    __ request.method __ 'POST' and 'tz_menu' in request.form:
        choice = request.form.get('tz_menu')
        tz_time = pendulum.now(choice).to_datetime_string()
    r_ render_template('index.html',
                            tz_list=tz_list,
                            choice=choice,
                            tz_time=tz_time)

    
__ __name__ __ "__main__":
    app.run()
    