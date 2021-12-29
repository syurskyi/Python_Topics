___ pagination_text(page_number, page_size, total_products):
	start = 1 + (page_number - 1) * page_size
	end = page_size * (page_number) __ (start + page_size) <= total_products ____ total_products
	r.. 'Showing ' + str(start) + ' to ' + str(end) + ' of ' + str(total_products) + ' Products.'