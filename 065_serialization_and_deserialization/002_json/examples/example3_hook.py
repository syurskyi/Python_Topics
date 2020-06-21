import datetime
import json


class DateFormatEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'value': obj.strftime('%d/%m/%Y %H:%M:%S'),
                '__datetime__': True
            }
        elif isinstance(obj, datetime.date):
            return {
                'value': obj.strftime('%d/%m/%Y'),
                '__date__': True
            }
        return json.JSONEncoder.default(self, obj)


data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'birthday': datetime.date(1986, 9, 29),
    'hired_at': datetime.datetime(2006, 9, 29, 12, 30, 5),
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

json_data = json.dumps(data, cls=DateFormatEncoder, indent=4)
print(json_data)

with open('data/output.json', 'w') as f:
    json.dump(data, f, cls=DateFormatEncoder)


def as_date_datetime(dct):
    print(dct)
    if '__datetime__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y %H:%M:%S')
    if '__date__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y').date()
    return dct


with open('data/output.json', 'r') as f:
    data = json.load(f, object_hook=as_date_datetime)
    print(data)
