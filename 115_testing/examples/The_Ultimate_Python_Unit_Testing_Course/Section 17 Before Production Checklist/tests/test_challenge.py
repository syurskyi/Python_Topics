import unittest
from challenge import ListChanger


class TestListChanger(unittest.TestCase):

	def setUp(self):
		self._list_changer_obj_1 = ListChanger([1, 2, 3, 4, 5, 6, 6])
		self._list_changer_obj_2 = ListChanger(["CA", "FL", "MC", "NY"])
		self._list_changer_obj_3 = ListChanger([True, False, True, False])
		
	def test_reverse_list(self):
		result = self._list_changer_obj_1.reverse_list()
		self.assertEqual(result, [6, 6, 5, 4, 3, 2, 1])
		
		result = self._list_changer_obj_2.reverse_list()
		self.assertEqual(result, ["NY", "MC", "FL", "CA"])
		
		result = self._list_changer_obj_3.reverse_list()
		self.assertEqual(result, [False, True, False, True])

	def test_has_duplicates(self):
		result = self._list_changer_obj_1.has_duplicates()
		self.assertEqual(result, True)
		
		result = self._list_changer_obj_2.has_duplicates()
		self.assertEqual(result, False)
		
		result = self._list_changer_obj_3.has_duplicates()
		self.assertEqual(result, True)

	def test_smallest_number(self):
		result = self._list_changer_obj_1.smallest_number()
		self.assertEqual(result, 1)
	
	def test_greatest_number(self):
		result = self._list_changer_obj_1.greatest_number()
		self.assertEqual(result, 6)
	
	def test_second_greatest_number(self):
		result = self._list_changer_obj_1.second_greatest_number()
		self.assertEqual(result, 5)
	
	def test_remove_first_and_last(self):
		result = self._list_changer_obj_1.remove_first_and_last()
		self.assertEqual(result, [2, 3, 4, 5, 6])

		result = self._list_changer_obj_2.remove_first_and_last()
		self.assertEqual(result, ["FL", "MC"])
		
		result = self._list_changer_obj_3.remove_first_and_last()
		self.assertEqual(result, [False, True])

	def tearDown(self):
		self._list_changer_obj_1 = None
		self._list_changer_obj_2 = None
		self._list_changer_obj_3 = None
