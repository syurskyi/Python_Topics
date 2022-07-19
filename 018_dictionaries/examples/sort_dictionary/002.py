customers = ['Kaley Fernandez', 'Darius Rowland', 'Isaac Borthwick',  'Alexandria Kidd']
sorted_customers = sorted(customers)
print(sorted_customers)

# Sort in Descending Order

orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)

for i in sort_orders:
	print(i[0], i[1])

# Sort in Ascending Order

orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = sorted(orders.items(), key=lambda x: x[1])

for i in sort_orders:
	print(i[0], i[1])

# List Comprehension

orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

[print(key, value) for (key, value) in sorted(orders.items(), key=lambda x: x[1])]

