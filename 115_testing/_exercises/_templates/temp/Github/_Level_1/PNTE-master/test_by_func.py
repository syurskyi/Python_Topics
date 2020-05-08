# -*- coding: utf-8 -*-

from nose.tools import with_setup, raises
from myfunc import add

# test with assert
___ test_add_nums():
  actual = add(1,10)
  assert actual == 11

# before test
___ setup_func():
  pass

# after test
___ teardown_func():
  pass

# @with_setup
@with_setup(setup_func,teardown_func)
___ test_add_Numbers():
  actual = add(-1,1)
  assert actual == 0

# @raise Error
@raises(RuntimeError)
___ test_invalid_arg1():
  actual = add(None,1)

# 未実装
@raises(RuntimeError)
___ test_invalid_arg2():
  actual = add(1,None)


