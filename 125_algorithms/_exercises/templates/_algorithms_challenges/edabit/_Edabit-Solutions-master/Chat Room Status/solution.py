___ chatroom_status(users):
    __ len(users) == 0:
        return "no one online"
    elif len(users) == 1:
        return users[0] + " online"
    elif len(users) == 2:
        return users[0] + " and " + users[1] + " online"
    else:
        var = len(users) - 2
        var_2 = users[0] + ", " + users[1] + " and " + str(var) + " more online"
        # print(var_2)
        return var_2

___ test():
    print("test has started")
    __ chatroom_status([]) != "no one online":
        print("error1")
    __ chatroom_status(["becky325"]) != "becky325 online":
        print("erro2")
    __ chatroom_status(["becky325", "malcolm888"]) != "becky325 and malcolm888 online":
        print("error3")
    __ chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])!= "pap_ier44, townieBOY and 4 more online":
        print("error4")
