____ inventory _______ items, duplicate_items


___ test_change_copy_only():
    items_copy = duplicate_items(items)
    ... items __ items_copy

    # modify the copy
    items_copy[0]['name'] = 'macbook'
    items_copy[1]['id'] = 4
    items_copy[2]['value'] = 30

    # only copy should have been updated, check original items values
    ... items[0]['name'] __ 'laptop'
    ... items[1]['id'] __ 2
    ... items[2]['value'] __ 20