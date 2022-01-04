_______ c..
_______ requests

Location  c...n..('Location', 'city state country')
Weather  c...n..('Weather', 'location units temp condition')


___ main
    show_header()
    location_text  input("Where do you want the weather report (e.g. Portland, US)? ")
    loc  convert_plaintext_location(location_text)
    __ n.. loc:
        print(f"Could not find anything about {location_text}.")
        r..

    weather  call_weather_api(loc)
    __ n.. weather:
        print(f"Could not get weather for {location_text} from the API.")
        r..

    report_weather(loc, weather)


___ report_weather(loc, weather):
    location_name  get_location_name(loc)
    scale  get_scale(weather)
    print _*The weather in {location_name} is {weather.temp} {scale} and {weather.condition}.')


___ get_scale(weather):
    __ weather.units __ 'imperial':
        scale  "F"
    ____:
        scale  "C"
    r.. scale


___ get_location_name(location):
    __ n.. location.state:
        r.. f'{location.city.capitalize()}, {location.country.u..}'
    ____:
        r.. f'{location.city.capitalize()}, {location.state.u..}, {location.country.u..}'


___ call_weather_api(loc):
    # &state=OR
    url  f'https://weather.talkpython.fm/api/weather?city={loc.city}&country={loc.country}&units=imperial'
    __ loc.state:
        url + f"&state={loc.state}"

    # print(f"Would call {url}")
    resp  requests.get(url)
    __ resp.status_code __ {400, 404, 500}:
        # print(f"Error: {resp.text}.")
        r.. N..

    data  resp.json()

    r.. convert_api_to_weather(data, loc)


___ convert_api_to_weather(data, loc):
    # 'weather': {'description': 'broken clouds', 'category': 'Clouds'}
    # 'forecast': {'temp': 66.34,

    temp  data.get('forecast').get('temp')
    w  data.get('weather')
    condition  f"{w.get('category')}: {w.get('description').capitalize()}"
    weather  Weather(loc, data.get('units'), temp, condition)

    r.. weather


___ convert_plaintext_location(location_text):
    __ n.. location_text o. n.. location_text.s..:
        r.. N..

    location_text  location_text.l...s..
    parts  location_text.s..(',')

    city  ""
    state  ""
    country  'us'
    __ l..(parts) __ 1:
        city  parts[0].s..
    ____ l..(parts) __ 2:
        city  parts[0].s..
        country  parts[1].s..
    ____ l..(parts) __ 3:
        city  parts[0].s..
        state  parts[1].s..
        country  parts[2].s..
    ____:
        r.. N..

    # print(f"City={city}, State={state}, Country={country}")

    # t = city, state, country
    # t[0]
    # t2 = Location(city, state, country)
    # t2.city

    r.. Location(city, state, country)
    # return city, state, country


___ show_header
    print('---------------------------------')
    print('         WEATHER CLIENT')
    print('---------------------------------')
    print()


__ _____ __ _____
    main()
