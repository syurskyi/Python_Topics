# Gas Stations
# Question: There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
# Note: The solution is guaranteed to be unique.
# Solutions:


class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer

    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        diff = 0
        stationIndex = 0
        for i in range(n):
            if gas[i]+diff < cost[i]:
                stationIndex = i+1; diff = 0
            else:
                diff += gas[i]-cost[i]

        return stationIndex


Solution().canCompleteCircuit([1,2,3,4,5],[5,4,3,2,1])