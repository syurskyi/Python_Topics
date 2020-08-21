def linear_search(main_list, item):
	print("Starting Linear Search Algorithm")
	for i in range(len(main_list)):
		print(f'============ Iteration #{i} ============')
		print("Current list item:", main_list[i])
		print("Item searched:", item)
		print("Is the current item equal to the item searched?", main_list[i] == item)
		if main_list[i] == item:
			print(f'Item found! at index, {i}')
			return i
		print("This is not the item")
	print("The item is not in the list")
	return -1


main_list = [["Jack", "456-342", 56], ("Emily", "231-523", 15), "Nora", [True, False]]
print(main_list)

item = "456-342"

# result = linear_search(main_list, item)

# result

([("Rose", 45, 5.6), [1, 2, 3]], ("a", "b", "c"), "Puppy", [4, 7, 8])


# <var>[<start>:<end>:<step>]



["Kelly", "Gino", "Katherine", "James", "Lulu"]

#
#
# ___ linear_search main_list item
# 	print("Starting Linear Search Algorithm")
# 	___ i __ ra.. le. ?
# 		print _*============ Iteration #|? ============
# 		print("Current list item id:" ?|?
# 		print("Target id:" ?
# 		print("Is the current item id equal to the id searched?" ?|? __ ?
# 		__ ?|?.id_num __ ?
# 			print _*ID found! at index |?
# 			r_ ?
# 		print("This is not the id")
# 	print("The object is not in the list")
# 	r_ -1


