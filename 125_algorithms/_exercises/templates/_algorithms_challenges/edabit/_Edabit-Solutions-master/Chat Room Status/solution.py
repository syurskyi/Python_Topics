___ chatroom_status(users
    __ l..(users) __ 0:
        r.. "no one online"
    ____ l..(users) __ 1:
        r.. users[0] + " online"
    ____ l..(users) __ 2:
        r.. users[0] + " and " + users[1] + " online"
    ____:
        var = l..(users) - 2
        var_2 = users[0] + ", " + users[1] + " and " + s..(var) + " more online"
        # print(var_2)
        r.. var_2

___ test
    print("test has started")
    __ chatroom_status([]) != "no one online":
        print("error1")
    __ chatroom_status(["becky325"]) != "becky325 online":
        print("erro2")
    __ chatroom_status(["becky325", "malcolm888"]) != "becky325 and malcolm888 online":
        print("error3")
    __ chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])!= "pap_ier44, townieBOY and 4 more online":
        print("error4")
