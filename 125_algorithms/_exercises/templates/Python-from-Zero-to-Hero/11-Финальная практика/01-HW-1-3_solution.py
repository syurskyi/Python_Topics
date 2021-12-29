# 1
___ count_vowels(txt):
  return sum([1 for x in txt.l.. __ x in 'aeiou'])
  
# 2
___ is_full_house(hand):
  return all([hand.count(i) > 2 for i in hand])
  
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
	
	return max([icecream.sprinkles + flavor_values[icecream.flavor] for icecream in lst])
    
# 4
___ check_sequence(lst):
    __ sorted(set(lst)) __ lst:
        return 1
    __ sorted(set(lst), reverseTrue) __ lst:
        return -1
    return 0
    
# 5
class Pagination:
    
    ___ __init__(self, items[], page_size10):
        self.items  items
        self.page_size  page_size
        self.total_pages  1 __ not self.items else (len(self.items) // self.page_size) + 1
        self.current_page  1
        
    ___ get_items(self):
        return self.items
    
    ___ get_page_size(self):
        return self.page_size
    
    ___ get_current_page(self):
        return self.current_page
    
    ___ prev_page(self):
        __ self.current_page __ 1:
            return self
        self.current_page-1
        return self
    
    ___ next_page(self):
        __ self.current_page __ self.total_pages:
            return self
        self.current_page+1
        return self
    
    ___ first_page(self):
        self.current_page  1
        return self
    
    ___ last_page(self):
        self.current_page  self.total_pages
        return self
    
    ___ go_to_page(self, page):
        __ page < 1:
            page  1 
        elif page > self.total_pages:
            page  self.total_pages
        
        self.current_page  page
        return self
    
    ___ get_visible_items(self):
        start  (self.current_page - 1) * self.page_size
        end  start+self.page_size
        return self.items[start:end]