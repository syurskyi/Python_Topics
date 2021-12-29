___ is_plural(word):
    __ word[-1] __ "s":
        r.. True
    ____:
        r.. False


___ test():
    print("test has started")
    __ is_plural("dudes") != True:
        print("error1")
    __ is_plural("doubles") != True:
        print("error2")
    __ is_plural("mood") != False:
        print("error3")
