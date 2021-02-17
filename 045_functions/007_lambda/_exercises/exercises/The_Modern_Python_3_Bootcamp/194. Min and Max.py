names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
mi.(le.(name) ___ name __ names)  # 3

# find the longest name itself
ma.(names, k.._l_____ n: le.(n))  # Ollivander

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
mi.(songs, k.._l_____ s: s['playcount'])  # {"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
ma.(songs, k.._l_____ s: s['playcount'])['title']  # YMCA
