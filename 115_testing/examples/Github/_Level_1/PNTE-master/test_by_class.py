# -*- coding: utf-8 -*-

from nose.tools import with_setup, raises
from myfunc import add

class TestAdd:
  
  # once before test
  @classmethod
  def setup_class(clazz):
    pass
 
  # once after test
  @classmethod
  def teardown_class(clazz):
    pass

  # before test
  def setup(self):
    pass
  
  # after test
  def teardown(self):
    pass

  # @raise Error
  @raises(RuntimeError)
  def test_invalid_arg1(self):
    actual = add(None,1)
  
  # 未実装
  @raises(RuntimeError)
  def test_invalid_arg2(self):
    actual = add(1,None)
 
  # test with assert
  def test_add_nums(self):
    actual = add(1,10)
    assert actual == 11
  
  
