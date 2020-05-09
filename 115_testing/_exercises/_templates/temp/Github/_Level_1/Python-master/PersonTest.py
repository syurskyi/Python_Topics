
______ u__

# This is the class we want to test. So, we need to ______ it
______ Person __ PersonClass


c_ Test?.?
    """
    The basic class that inherits unittest.TestCase
    """
    person _ PersonClass.Person()  # instantiate the Person Class
    user_id _ []  # variable that stores obtained user_id
    user_name _ []  # variable that stores person name

    # test case function to check the Person.set_name function
    ___ test_0_set_name
        print("Start set_name test\n")
        """
        Any method which starts with ``test_`` will considered as a test case.
        """
        for i in range(4
            # initialize a name
            name _ 'name' + st.(i)
            # store the name into the list variable
            user_name.append(name)
            # get the user id obtained from the function
            user_id _ person.set_name(name)
            # check if the obtained user id is null or not
            assertIsNotNone(user_id)  # null user id will fail the test
            # store the user id to the list
            user_id.append(user_id)
        print("user_id length = ", len(user_id))
        print(user_id)
        print("user_name length = ", len(user_name))
        print(user_name)
        print("\nFinish set_name test\n")

    # test case function to check the Person.get_name function
    ___ test_1_get_name
        print("\nStart get_name test\n")
        """
        Any method that starts with ``test_`` will be considered as a test case.
        """
        length _ len(user_id)  # total number of stored user information
        print("user_id length = ", length)
        print("user_name length = ", len(user_name))
        for i in range(6
            # if i not exceed total length then verify the returned name
            __ i < length:
                # if the two name not matches it will fail the test case
                aE..(user_name[i], person.get_name(user_id[i]))
            else:
                print("Testing for get_name no user test")
                # if length exceeds then check the 'no such user' type message
                aE..('There is no such user', person.get_name(i))
        print("\nFinish get_name test\n")


__ __name__ __ '__main__':
    # begin the unittest.main()
    ?.?