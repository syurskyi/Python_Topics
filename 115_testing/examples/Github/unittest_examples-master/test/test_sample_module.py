# from proj.sample_module import add2num
import pytest

class Testadd2num:

	def test_sum_2pos_num(self):
		assert add2num(5,6) == 11

	def test_sum_1pos_1neg_num(self):
		assert add2num(-10,5) == -5

	def test_using_raises(self):
		with pytest.raises(TypeError):
			add2num(2, '3') == 5


a = {'a':1, 'b':2}

for k,v in a.items():
	print(k)
	print(v)

print('c' in a)