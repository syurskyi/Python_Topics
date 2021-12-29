___ min_max(nums):
    nums.sort()
    r.. [nums[0],nums[-1]]


___ test():
    print("test has started")
    a_list = [14, 35, 6, 1, 34, 54]
    __ min_max(a_list) != [1,54]:
        print("error1")
    b_list = [1.346, 1.6532, 1.8734, 1.8723]
    __ min_max(b_list) != [1.346, 1.8734]:
        print("error2")
