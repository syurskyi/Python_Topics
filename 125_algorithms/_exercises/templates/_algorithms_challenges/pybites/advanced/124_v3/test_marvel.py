____ marvel _______ (characters,
                    most_popular_characters,
                    max_and_min_years_new_characters,
                    get_percentage_female_characters)

half_size = i..(l..(characters)/2)

half_characters = characters[:half_size]


___ test_most_popular_characters
    a.. = most_popular_characters()
    e.. =  'Spider-Man', 'Captain America', 'Wolverine',
                'Iron Man', 'Thor' 
    ... a.. __ e..


___ test_max_and_min_years_new_characters
    a.. = max_and_min_years_new_characters()
    e.. = ('1993', '1958')
    ... a.. __ e..


___ test_get_percentage_female_characters
    a.. = get_percentage_female_characters()
    e.. = 24.72
    ... a.. __ e..


___ test_most_popular_characters_smaller_data_set_and_top_2
    e.. =  'Spider-Man', 'Captain America' 
    a.. = most_popular_characters(half_characters, top=2)
    ... a.. __ e..


___ test_max_and_min_years_new_characters_smaller_data_set
    e.. = ('1992', '1959')
    a.. = max_and_min_years_new_characters(half_characters)
    ... a.. __ e..


___ test_get_percentage_female_characters_smaller_data_set
    a.. = get_percentage_female_characters(half_characters)
    e.. = 28.73
    ... a.. __ e..