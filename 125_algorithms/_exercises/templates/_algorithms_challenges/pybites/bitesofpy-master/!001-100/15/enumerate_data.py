names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


___ enumerate_names_countries(
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    ___ name, country, c in zip(names, countries, range(1,le.(names)+1)):
        print(f"{c}. {name:<10} {country}")
