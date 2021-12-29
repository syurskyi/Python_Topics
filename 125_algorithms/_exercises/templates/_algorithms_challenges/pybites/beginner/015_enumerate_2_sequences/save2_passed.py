names = 'Julian Bob PyBites Dante Martin Rodolfo'.s..
countries = 'Australia Spain Global Argentina USA Mexico'.s..


___ enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    i = 1
    ___ name, country __ zip(names, countries):
        print(str(i)+ ". {:<10} {}".format(name, country))
        i +=1