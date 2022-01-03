# 1
___ count_vowels(txt):
  r.. s..([1 ___ x __ txt.l.. __ x __ 'aeiou'])
  
# 2
___ is_full_house(hand):
  r.. a..([hand.c.. i) > 2 ___ i __ hand])
  
# 3
c_ IceCream:
    ___ - , flavor, sprinkles):
        flavor  flavor
        sprinkles  sprinkles
        
___ sweetest_icecream(lst):
	flavor_values  {
	'Plain' :	0,
	'Vanilla' :	5,
	'ChocolateChip' :	5,
	'Strawberry' : 10,
	'Chocolate'	: 10
	}
	
	r.. max([icecream.sprinkles + flavor_values[icecream.flavor] ___ icecream __ lst])
    
# 4
___ check_sequence(lst):
    __ s..(set(lst)) __ lst:
        r.. 1
    __ s..(set(lst), reverseTrue) __ lst:
        r.. -1
    r.. 0
    
# 5
c_ Pagination:
    
    ___ - , items[], page_size10):
        items  items
        page_size  page_size
        total_pages  1 __ n.. items ____ (l..(items) // page_size) + 1
        current_page  1
        
    ___ get_items
        r.. items
    
    ___ get_page_size
        r.. page_size
    
    ___ get_current_page
        r.. current_page
    
    ___ prev_page
        __ current_page __ 1:
            r.. self
        current_page-1
        r.. self
    
    ___ next_page
        __ current_page __ total_pages:
            r.. self
        current_page+1
        r.. self
    
    ___ first_page
        current_page  1
        r.. self
    
    ___ last_page
        current_page  total_pages
        r.. self
    
    ___ go_to_page(self, page):
        __ page < 1:
            page  1 
        ____ page > total_pages:
            page  total_pages
        
        current_page  page
        r.. self
    
    ___ get_visible_items
        start  (current_page - 1) * page_size
        end  start+page_size
        r.. items[start:end]