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
  @raises(RuntimeError)
  ___ test_invalid_arg1
    actual _ add(None,1)
  
  # 未実装
  @raises(RuntimeError)
  ___ test_invalid_arg2
    actual _ add(1,None)
 
  # test with assert
  ___ test_add_nums
    actual _ add(1,10)
    a.. actual __ 11
  
  
