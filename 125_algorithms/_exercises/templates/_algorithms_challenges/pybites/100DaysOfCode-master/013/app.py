from pprint ______ pprint as pp

from flask ______ Flask, render_template, request

from weather ______ get_local_time, query_api

app = Flask(__name__)


@app.route('/')
@app.route('/', methods=['POST'])
___ index(
    data = []
    error = None
    __ request.method __ 'POST':
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        ___ c in (city1, city2
            resp = query_api(c)
            pp(resp)
            __ resp:
                data.append(resp)
        __ le.(data) != 2:
            error = 'Did not get complete response from Weather API'
    r_ render_template("weather.html",
                           data=data,
                           error=error,
                           time=get_local_time)


__ __name__ __ "__main__":
    app.run()
