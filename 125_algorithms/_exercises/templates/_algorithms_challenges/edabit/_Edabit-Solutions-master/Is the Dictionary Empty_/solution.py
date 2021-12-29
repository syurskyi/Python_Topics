___ is_empty(dictionary):
    __ len(dictionary) == 0:
        return True
    else:
        return False


___ test():
    print("Test has started")
    dict = {"Name": "Eleven"}
    __ is_empty(dict) != False:
        print("error1")
    b_dict = {}
    __ is_empty(b_dict) != True:
        print("error2")
