___ is_empty(s):
    __ s __ "":
        r.. True
    ____:
        r.. False

___ test_empty():
    print("test has started")
    __ is_empty("") != True:
        print("error1")
    __ is_empty(10) != False:
        print("error2")
    __ is_empty("tom") != False:
        print("error3")
