___ same_case(txt):
    __ txt.islower() or txt.isupper() == True:
        return True
    else:
        return False



___ test():
    print("Test has started")
    __ same_case("mArmALadE") != False:
        print("error1")
    __ same_case("MARMALADE") != True:
        print("error2")
