___ pagination_text(page_number, page_size, total_products
	start = 1 + (page_number - 1) * page_size
	end = page_size * (page_number) __ (start + page_size) <= total_products ____ total_products
	r.. 'Showing ' + s..(start) + ' to ' + s..(end) + ' of ' + s..(total_products) + ' Products.'