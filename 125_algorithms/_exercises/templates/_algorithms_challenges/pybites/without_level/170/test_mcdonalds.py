____ mcdonalds _______ (df,
                       get_food_most_calories,
                       get_bodybuilder_friendly_foods)

ASSERT_ERROR = ("One or more expected foods not in "
                "get_bodybuilder_friendly_foods's return value")


___ test_get_food_most_calories
    actual = get_food_most_calories()
    expected = 'Chicken McNuggets (40 piece)'
    ... actual __ expected


___ test_get_food_most_calories_smaller_population
    """Extra test to prevent hardcoding the return value"""
    df_breakfast = df[df 'Category'  __ 'Breakfast'

    actual = get_food_most_calories(df_breakfast)
    expected = 'Big Breakfast with Hotcakes (Large Biscuit)'
    ... actual __ expected


___ test_get_bodybuilder_friendly_foods
    actual_with_drinks = l..(get_bodybuilder_friendly_foods
    expected =  'Premium Bacon Ranch Salad with Grilled Chicken',
                'Nonfat Latte (Small)',
                'Nonfat Latte (Large)',
                'Premium Southwest Salad with Grilled Chicken',
                'Nonfat Latte (Medium)'
    ... a..(food __ actual_with_drinks ___ food __ expected), ASSERT_ERROR


___ test_get_bodybuilder_friendly_foods_excluding_liquid_food
    actual_wo_drinks = l..(get_bodybuilder_friendly_foods(excl_drinks=T..))
    expected =  'Premium Bacon Ranch Salad with Grilled Chicken',
                'Premium Southwest Salad with Grilled Chicken',
                'Premium Grilled Chicken Classic Sandwich',
                'Premium Grilled Chicken Ranch BLT Sandwich',
                'Premium Grilled Chicken Club Sandwich'
    ... a..(food __ actual_wo_drinks ___ food __ expected), ASSERT_ERROR