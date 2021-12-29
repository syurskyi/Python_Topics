import collections
import requests

Location  collections.namedtuple('Location', 'city state country')
Weather  collections.namedtuple('Weather', 'location units temp condition')


___ main():
    show_header()
    location_text  input("Where do you want the weather report (e.g. Portland, US)? ")
    loc  convert_plaintext_location(location_text)
    __ not loc:
        print(f"Could not find anything about {location_text}.")
        return

    weather  call_weather_api(loc)
    __ not weather:
        print(f"Could not get weather for {location_text} from the API.")
        return

    report_weather(loc, weather)


___ report_weather(loc, weather):
    location_name  get_location_name(loc)
    scale  get_scale(weather)
    print(f'The weather in {location_name} is {weather.temp} {scale} and {weather.condition}.')


___ get_scale(weather):
    __ weather.units __ 'imperial':
        scale  "F"
    else:
        scale  "C"
    return scale


___ get_location_name(location):
    __ not location.state:
        return f'{location.city.capitalize()}, {location.country.upper()}'
    else:
        return f'{location.city.capitalize()}, {location.state.upper()}, {location.country.upper()}'


___ call_weather_api(loc):
    # &state=OR
    url  f'https://weather.talkpython.fm/api/weather?city={loc.city}&country={loc.country}&units=imperial'
    __ loc.state:
        url + f"&state={loc.state}"

    # print(f"Would call {url}")
    resp  requests.get(url)
    __ resp.status_code in {400, 404, 500}:
        # print(f"Error: {resp.text}.")
        return N..

    data  resp.json()

    return convert_api_to_weather(data, loc)


___ convert_api_to_weather(data, loc):
    # 'weather': {'description': 'broken clouds', 'category': 'Clouds'}
    # 'forecast': {'temp': 66.34,

    temp  data.get('forecast').get('temp')
    w  data.get('weather')
    condition  f"{w.get('category')}: {w.get('description').capitalize()}"
    weather  Weather(loc, data.get('units'), temp, condition)

    return weather


___ convert_plaintext_location(location_text):
    __ not location_text or not location_text.strip():
        return N..

    location_text  location_text.l...strip()
    parts  location_text.split(',')

    city  ""
    state  ""
    country  'us'
    __ len(parts) __ 1:
        city  parts[0].strip()
    elif len(parts) __ 2:
        city  parts[0].strip()
        country  parts[1].strip()
    elif len(parts) __ 3:
        city  parts[0].strip()
        state  parts[1].strip()
        country  parts[2].strip()
    else:
        return N..

    # print(f"City={city}, State={state}, Country={country}")

    # t = city, state, country
    # t[0]
    # t2 = Location(city, state, country)
    # t2.city

    return Location(city, state, country)
    # return city, state, country


___ show_header():
    print('---------------------------------')
    print('         WEATHER CLIENT')
    print('---------------------------------')
    print()


__ __name__ __ '__main__':
    main()
