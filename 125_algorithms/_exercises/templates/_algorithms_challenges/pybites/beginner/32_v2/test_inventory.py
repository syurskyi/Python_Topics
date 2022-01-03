# ____ i.. _______ i.. d..
#
#
# ___ test_change_copy_only
#     items_copy ? ?
#     ... items __ ?
#
#     # modify the copy
#     i.. 0 'name' 'macbook'
#     i.. 1 'id' 4
#     i.. 2 'value' 30
#
#     # only copy should have been updated, check original items values
#     ... ? 0 'name' __ 'laptop'
#     ... ? 1 'id' __ 2
#     ... ? 2 'value' __ 20