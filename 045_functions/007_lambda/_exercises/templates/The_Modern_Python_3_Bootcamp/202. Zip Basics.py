# midterms = [80, 91, 78]
# finals = [98, 89, 53]
# students = ['dan', 'ang', 'kate']
#
#
# # returns dict with {student:highest score} USING LIST COMP
# # {'dan': 98, 'ang': 91, 'kate': 78}
# final_grades = t|0 :ma.(t|1 t|2 ___ t __ z__ s.., m.. f..
#
#
# # returns dict with {student:highest score} USING MAP+LAMBDA
# # {'dan': 98, 'ang': 91, 'kate': 78}
# final_grades = d__
#     z__
#         s...
#         m__
#             l_____ pair ma. ?
#             z__ m.. f..
#         )
#     )
# )
#
# # returns dict with student:average score
# # {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
# avg_grades = d__
#     z__
#         s..
#         m__(
#             l_____ pair ? 0 + ? 1 /2
#             z__ m.. f..
#         )
#     )
# )
#
# # # r = dict(zip(students, midterms))
# # print(r)
#
# # r = {item[0]: max(item[1], item[2]) for item in zip(students,midterms, finals)}
# # print(r)
#
# # r = {item[0]: round((item[1] + item[2])/2) for item in zip(students,midterms, finals)}
# # print(r)
#
#
# # z = zip(
# # 	students,
# # 	map(
# # 		lambda pair: max(pair),
# # 		zip(midterms, finals)
# # 	)
# # )
#
