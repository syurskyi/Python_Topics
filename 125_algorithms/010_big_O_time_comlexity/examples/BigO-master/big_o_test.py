import nose.tools
import big_o
from random import randint

test_of_1 = big_o.BigO_of_1()
test_of_N = big_o.BigO_of_N()
test_of_N_Squared = big_o.BigO_of_N_Squared()
test_of_N_Cubed = big_o.BigO_of_N_Cubed()
test_of_N_Four = big_o.BigO_of_N_to_the_Fourth()
test_of_2_N = big_o.BigO_of_2_to_the_N()
test_of_N_log_N = big_o.BigO_of_N_log_N()

test_list = []
for i in range(0, 100):
    test_list.append(i)

random_test_list = []
for i in range(0, 100):
    random_test_list.append(randint(0,99))

one_hundred_factorial = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

def test_O_of_1_tells_truth():
    assert test_of_1.check_index_0_is_int(test_list) == True

def test_O_of_N_Doubles_lists():
    returned_list = test_of_N.double_values(test_list)
    assert returned_list[88] == 176

def test_O_of_2_N_Gives_the_right_factorial():
    result = test_of_2_N.get_factorial(100)
    assert result == one_hundred_factorial
 
def test_O_of_N_log_N():
    returned_list = test_of_N_log_N.sort_list(random_test_list)
    returned_boolean = True
    if returned_list[0] > returned_list[99]:
        returned_boolean = False
    if returned_list[55] > returned_list[56]:
        returned_boolean = False
    if returned_list[33] > returned_list[42]:
        returned_boolean = False
    if returned_list[76] > returned_list[88]:
        returned_boolean = False
    assert returned_boolean == True

def test_O_of_N_Squared_makes_a_spam_field():
    returned_list = test_of_N_Squared.create_spam_field(test_list)
    assert len(returned_list) == 100
    assert len(returned_list[88]) == 100
    assert returned_list[88][88] == 'spam'

def test_O_of_N_Cubed_makes_a_spam_space():
    returned_list = test_of_N_Cubed.create_spam_space(test_list)
    assert len(returned_list) == 100
    assert len(returned_list[88]) == 100
    assert len(returned_list[88][88]) == 100
    assert returned_list[88][88][88] == 'spam'

def test_O_of_N_Four_Makes_a_spam_hyperspace():
    returned_list = test_of_N_Four.create_spam_hyperspace(test_list)
    assert len(returned_list) == 100
    assert len(returned_list[88]) == 100
    assert len(returned_list[88][88]) == 100
    assert len(returned_list[88][88][88]) == 100
    assert returned_list[88][88][88][88] == 'spam'
