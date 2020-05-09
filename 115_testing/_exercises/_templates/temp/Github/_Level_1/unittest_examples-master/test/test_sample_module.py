# from proj.sample_module ______ add2num
______ pytest

c_ Testadd2num:

	___ test_sum_2pos_num
		assert add2num(5,6) == 11

	___ test_sum_1pos_1neg_num
		assert add2num(-10,5) == -5

	___ test_using_raises
		with pytest.raises(TypeError):
			add2num(2, '3') == 5


a _ {'a':1, 'b':2}

for k,v in a.items():
	print(k)
	print(v)

print('c' in a)