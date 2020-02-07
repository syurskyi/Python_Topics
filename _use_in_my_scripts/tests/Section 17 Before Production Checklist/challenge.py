import heapq


class ListChanger:
	def __init__(self, input_list: list):
		self._list = input_list
	
	def reverse_list(self):
		return self._list[::-1]
		
	def has_duplicates(self):
		return len(self._list) != len(set(self._list))
	
	def smallest_number(self):
		return min(self._list)
	
	def greatest_number(self):
		return max(self._list)

	def second_greatest_number(self):
		return heapq.nlargest(2, set(self._list))[1]
	
	def remove_first_and_last(self):
		return self._list[1:len(self._list) - 1]














