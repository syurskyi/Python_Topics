class Solution:
    ___ checkPossibility(self, nums: List[int]) -> bool:
                i = 0
                non_count = 0
                equals = False
                w.... i!= l..(nums)-1:
                    try:
                        __ nums[i] > nums[i+1]:
                            __ i+1 __ l..(nums)-1:
                                nums[i+1] += (nums[i] - nums[i+1]) + 1
                               
                                non_count +=1
                                i = 0
                            ____:
                                __ nums[i+1] < nums[i+2]:
                                    __ equals __ True:
                                        nums[i+1] = nums[i]
                                    ____:
                                        __ nums[i] < nums[i+2]:
                                            nums[i+1] = nums[i+2]
                                        ____:
                                            nums[i] = nums[i+1]
                                ____:
                                    nums[i] = (nums[i] - nums[i+1])
                                non_count += 1
                                i = 0
                        ____ nums[i] __ nums[i+1]:
                            equals = True
                            i += 1
                        ____:
                            i += 1
                    except:
                        pass
                    __ non_count >= 2:
                        break
                __ non_count <= 1:
                    r.. True
                ____:
                    r.. False