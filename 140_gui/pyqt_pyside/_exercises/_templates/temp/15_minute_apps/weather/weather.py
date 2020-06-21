____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *

____ MainWindow ______ Ui_MainWindow

____ d_t_ ______ d_t_
______ ____
______ __
______ ___
______ requests
____ urllib.parse ______ urlencode

OPENWEATHERMAP_API_KEY _ __.environ.g..('OPENWEATHERMAP_API_KEY')

"""
Get an API key from https://openweathermap.org/ to use with this
application.

"""


___ from_ts_to_time_of_day(ts):
    dt _ d_t_.fromtimestamp(ts)
    r_ dt.strftime("%I%p").lstrip("0")


c_ WorkerSignals(?O..):
    '''
    Defines the signals available from a running worker thread.
    '''
    finished _ pS..()
    error _ pS.. st.
    result _ pS..(dict, dict)

c_ WeatherWorker(QRunnable):
    '''
    Worker thread for weather updates.
    '''
    signals _ WorkerSignals()
    is_interrupted _ F..

    ___  -   location):
        s__(WeatherWorker, self). - ()
        location _ location

    @pyqtSlot()
    ___ run 
        ___
            params _ dict(
                q_self.location,
                appid_OPENWEATHERMAP_API_KEY
            )

            url _ 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(params)
            r _ requests.g..(url)
            weather _ ____.loads(r.t__)

            # Check if we had a failure (the forecast will fail in the same way).
            __ weather['cod'] !_ 200:
                r_ E..(weather['message'])

            url _ 'http://api.openweathermap.org/data/2.5/forecast?%s&units=metric' % urlencode(params)
            r _ requests.g..(url)
            forecast _ ____.loads(r.t__)

            signals.result.e..(weather, forecast)

        _____ E.. __ e:
            signals.error.e..(st.(e))

        signals.finished.e..()



c_ MainWindow(?MW.., Ui_MainWindow):

    ___  -   $ $$
        s__(MainWindow, self). - ($ $$)
        setupUi

        pushButton.pressed.c..(update_weather)

        threadpool _ ?TP..()

        s..


    ___ alert  message):
        alert _ ?MB...w..  "Warning", message)

    ___ update_weather 
        worker _ WeatherWorker(lineEdit.t__())
        worker.signals.result.c..(weather_result)
        worker.signals.error.c..(alert)
        threadpool.start(worker)

    ___ weather_result  weather, forecasts):
        latitudeLabel.sT..("%.2f °" % weather['coord']['lat'])
        longitudeLabel.sT..("%.2f °" % weather['coord']['lon'])

        windLabel.sT..("%.2f m/s" % weather['wind']['speed'])

        temperatureLabel.sT..("%.1f °C" % weather['main']['temp'])
        pressureLabel.sT..("%d" % weather['main']['pressure'])
        humidityLabel.sT..("%d" % weather['main']['humidity'])

        sunriseLabel.sT..(from_ts_to_time_of_day(weather['sys']['sunrise']))

        weatherLabel.sT..("%s (%s)" % (
            weather['weather'][0]['main'],
            weather['weather'][0]['description']
        )
                                  )

        set_weather_icon(weatherIcon, weather['weather'])

        ___ n, forecast __ en..(forecasts['list'][:5], 1):
            getattr  'forecastTime%d' % n).sT..(from_ts_to_time_of_day(forecast['dt']))
            set_weather_icon(getattr  'forecastIcon%d' % n), forecast['weather'])
            getattr  'forecastTemp%d' % n).sT..("%.1f °C" % forecast['main']['temp'])

    ___ set_weather_icon  label, weather):
        label.sP..(
            ?P..(__.p__ .join('images', "%s.png" %
                                 weather[0]['icon']
                                 )
                    )

        )


__ ______ __ ______

    app _ ?
    window _ MainWindow()
    app.e..