my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    },
    'brother': {
    	'name': 'Kevin',
    	'age': 900
    },
    'cousin': {
    	'name': 'Dragons',
    	'age': 6
    }
}

new_family = {str(v['name']) + ' is my ' + k +' and is ' + str(v['age']) for (k,v) in my_family.items()}
print(new_family)