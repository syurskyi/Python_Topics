# -*- coding: utf-8 -*-

____ nose.tools ______ with_setup, raises
____ myfunc ______ add

# test with assert
___ test_add_nums(
  actual _ add(1,10)
  assert actual == 11

# before test
___ setup_func(
  pass

# after test
___ teardown_func(
  pass

# @with_setup
@with_setup(setup_func,teardown_func)
___ test_add_Numbers(
  actual _ add(-1,1)
  assert actual == 0

# @raise Error
@raises(RuntimeError)
___ test_invalid_arg1(
  actual _ add(None,1)

# 未実装
@raises(RuntimeError)
___ test_invalid_arg2(
  actual _ add(1,None)


