# -*- coding: utf-8 -*-

from nose.tools import with_setup, raises
from myfunc import add

# test with assert
def test_add_nums():
  actual = add(1,10)
  assert actual == 11

# before test
def setup_func():
  pass

# after test
def teardown_func():
  pass

# @with_setup
@with_setup(setup_func,teardown_func)
def test_add_Numbers():
  actual = add(-1,1)
  assert actual == 0

# @raise Error
@raises(RuntimeError)
def test_invalid_arg1():
  actual = add(None,1)

# 未実装
@raises(RuntimeError)
def test_invalid_arg2():
  actual = add(1,None)


