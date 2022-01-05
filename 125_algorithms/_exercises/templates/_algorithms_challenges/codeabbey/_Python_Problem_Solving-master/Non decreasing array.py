c_ Solution:
    ___ checkPossibility  nums: List[i..]) __ bool:
                i = 0
                non_count = 0
                equals = F..
                w.... i!= l..(nums)-1:
                    ___
                        __ nums[i] > nums[i+1]:
                            __ i+1 __ l..(nums)-1:
                                nums[i+1] += (nums[i] - nums[i+1]) + 1
                               
                                non_count +=1
                                i = 0
                            ____:
                                __ nums[i+1] < nums[i+2]:
                                    __ equals __ T..:
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
                            equals = T..
                            i += 1
                        ____:
                            i += 1
                    ______:
                        p..
                    __ non_count >= 2:
                        break
                __ non_count <= 1:
                    r.. T..
                ____:
                    r.. F..