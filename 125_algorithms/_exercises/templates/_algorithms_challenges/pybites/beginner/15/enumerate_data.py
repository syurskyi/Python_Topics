names = 'Julian Bob PyBites Dante Martin Rodolfo'.s..
countries = 'Australia Spain Global Argentina USA Mexico'.s..


___ enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USAs
       6. Rodolfo    Mexico"""
    output = ""
    ___ count, name __ enumerate(names, start=1):
        __ count < 6:
            output += str(count) + ".".ljust(2) + name.ljust(11) + countries[count-1] + "\n"
        ____:
            output += str(count) + ".".ljust(2) + name.ljust(11) + countries[count-1]
    print(output)
