# 1
___ count_vowels(txt):
  r.. s..([1 ___ x __ txt.l.. __ x __ 'aeiou'])
  
# 2
___ is_full_house(hand):
  r.. a..([hand.c.. i) > 2 ___ i __ hand])
  
# 3
class IceCream:
    ___ __init__(self, flavor, sprinkles):
        self.flavor  flavor
        self.sprinkles  sprinkles
        
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
class Pagination:
    
    ___ __init__(self, items[], page_size10):
        self.items  items
        self.page_size  page_size
        self.total_pages  1 __ n.. self.items ____ (l..(self.items) // self.page_size) + 1
        self.current_page  1
        
    ___ get_items(self):
        r.. self.items
    
    ___ get_page_size(self):
        r.. self.page_size
    
    ___ get_current_page(self):
        r.. self.current_page
    
    ___ prev_page(self):
        __ self.current_page __ 1:
            r.. self
        self.current_page-1
        r.. self
    
    ___ next_page(self):
        __ self.current_page __ self.total_pages:
            r.. self
        self.current_page+1
        r.. self
    
    ___ first_page(self):
        self.current_page  1
        r.. self
    
    ___ last_page(self):
        self.current_page  self.total_pages
        r.. self
    
    ___ go_to_page(self, page):
        __ page < 1:
            page  1 
        ____ page > self.total_pages:
            page  self.total_pages
        
        self.current_page  page
        r.. self
    
    ___ get_visible_items(self):
        start  (self.current_page - 1) * self.page_size
        end  start+self.page_size
        r.. self.items[start:end]