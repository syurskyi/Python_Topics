class Solution:
    ___ checkPossibility(self, nums: List[int]) -> bool:
                i = 0
                non_count = 0
                equals = False
                while i!= len(nums)-1:
                    try:
                        __ nums[i] > nums[i+1]:
                            __ i+1 == len(nums)-1:
                                nums[i+1] += (nums[i] - nums[i+1]) + 1
                               
                                non_count +=1
                                i = 0
                            else:    
                                __ nums[i+1] < nums[i+2]:
                                    __ equals == True:
                                        nums[i+1] = nums[i]
                                    else:
                                        __ nums[i] < nums[i+2]:
                                            nums[i+1] = nums[i+2]
                                        else:
                                            nums[i] = nums[i+1]
                                else:
                                    nums[i] = (nums[i] - nums[i+1])
                                non_count += 1
                                i = 0
                        elif nums[i] == nums[i+1]:
                            equals = True
                            i += 1
                        else:
                            i += 1
                    except:
                        pass
                    __ non_count >= 2:
                        break
                __ non_count <= 1:
                    return True
                else:
                    return False