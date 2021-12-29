
# What happens if I add a duplicate key to a dictionary?

country_capitals = {'Sweden': 'Stockholm', 'Germany':'Berlin'}

print(country_capitals)

country_capitals['Poland'] = 'Warsaw'

print(country_capitals)

# Reverse using dictionary comprehension

rr = {capital:  country for country, capital in country_capitals.items()}

