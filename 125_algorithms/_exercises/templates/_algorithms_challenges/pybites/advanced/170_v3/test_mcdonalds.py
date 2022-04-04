____ Previous.mcdonalds _______ (df,
                                get_food_most_calories,
                                get_bodybuilder_friendly_foods)

ASSERT_ERROR = ("One or more expected foods not in "
                "get_bodybuilder_friendly_foods's return value")


___ test_get_food_most_calories
    a.. = get_food_most_calories()
    e.. = 'Chicken McNuggets (40 piece)'
    ... a.. __ e..


___ test_get_food_most_calories_smaller_population
    """Extra test to prevent hardcoding the return value"""
    df_breakfast = df[df 'Category'  __ 'Breakfast'

    a.. = get_food_most_calories(df_breakfast)
    e.. = 'Big Breakfast with Hotcakes (Large Biscuit)'
    ... a.. __ e..


___ test_get_bodybuilder_friendly_foods
    actual_with_drinks = l..(get_bodybuilder_friendly_foods
    e.. =  'Premium Bacon Ranch Salad with Grilled Chicken',
                'Nonfat Latte (Small)',
                'Nonfat Latte (Large)',
                'Premium Southwest Salad with Grilled Chicken',
                'Nonfat Latte (Medium)'
    ... a..(food __ actual_with_drinks ___ food __ e..), ASSERT_ERROR


___ test_get_bodybuilder_friendly_foods_excluding_liquid_food
    actual_wo_drinks = l..(get_bodybuilder_friendly_foods(excl_drinks=T..
    e.. =  'Premium Bacon Ranch Salad with Grilled Chicken',
                'Premium Southwest Salad with Grilled Chicken',
                'Premium Grilled Chicken Classic Sandwich',
                'Premium Grilled Chicken Ranch BLT Sandwich',
                'Premium Grilled Chicken Club Sandwich'
    ... a..(food __ actual_wo_drinks ___ food __ e..), ASSERT_ERROR