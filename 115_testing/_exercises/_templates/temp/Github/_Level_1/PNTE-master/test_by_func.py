# -*- coding: utf-8 -*-

____ nose.tools ______ with_setup, raises
____ myfunc ______ add

# test with assert
___ test_add_nums(
  actual _ add(1,10)
  a.. actual __ 11

# before test
___ setup_func(
  p..

# after test
___ teardown_func(
  p..

# @with_setup
@with_setup(setup_func,teardown_func)
___ test_add_Numbers(
  actual _ add(-1,1)
  a.. actual __ 0

# @raise Error
@raises(R..)
___ test_invalid_arg1(
  actual _ add(N..,1)

# 未実装
@raises(R..)
___ test_invalid_arg2(
  actual _ add(1,N..)


