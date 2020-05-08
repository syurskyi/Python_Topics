# -*- coding: utf-8 -*-

from nose.tools import with_setup, raises
from myfunc import add

c_ TestAdd:
  
  # once before test
  @classmethod
  ___ setup_class(clazz):
    pass
 
  # once after test
  @classmethod
  ___ teardown_class(clazz):
    pass

  # before test
  ___ setup(self):
    pass
  
  # after test
  ___ teardown(self):
    pass

  # @raise Error
  @raises(RuntimeError)
  ___ test_invalid_arg1(self):
    actual = add(None,1)
  
  # 未実装
  @raises(RuntimeError)
  ___ test_invalid_arg2(self):
    actual = add(1,None)
 
  # test with assert
  ___ test_add_nums(self):
    actual = add(1,10)
    assert actual == 11
  
  
