___ check(lst, el):
    __ lst.count(el) > 0:
        return True
    else:
        return False


___ test():
    print("test has started")
    a_list = [4.6,4,7]
    __ check(a_list,4) != True:
        print("error")
    __ check(a_list,2) != False:
        print("erro2")

