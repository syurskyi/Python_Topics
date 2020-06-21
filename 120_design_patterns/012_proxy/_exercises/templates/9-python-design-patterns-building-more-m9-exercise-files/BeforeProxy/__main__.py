# ____ t... ______ E.. A..
#
# ___ get_employee_info empids reqid
#     ___ empid __ e...
#         __ ? no. __ E...
#             c...
#         employee _ E...|e..
#         details _ 'Employee Id: @, Name: %s'    # digit  string
#         details _ ?  e___.em.. e__.n..
#
#         __ reqid __ A..
#             __ A...|? .c_s_p..
#                 d.. +_ (', BirthDate: @, Salary: @.2f'
#                             |e__.b.. e__.s..
#         print ?
#
# ?([3, 4], 3) # requestor may not see personal data
#
# ?([1, 2], 101) # requestor *may* see personal data
