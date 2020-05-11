# -*- coding: utf-8 -*-

____ nose.tools ______ with_setup, raises
____ myfunc ______ add

c_ TestAdd:
  
  # once before test
  ??
  ___ setup_class(clazz
    p..
 
  # once after test
  ??
  ___ teardown_class(clazz
    p..

  # before test
  ___ setup
    p..
  
  # after test
  ___ teardown
    p..

  # @raise Error
  @raises(R..)
  ___ test_invalid_arg1
    actual _ add(N..,1)
  
  # 未実装
  @raises(R..)
  ___ test_invalid_arg2
    actual _ add(1,N..)
 
  # test with assert
  ___ test_add_nums
    actual _ add(1,10)
    a.. actual __ 11
  
  
