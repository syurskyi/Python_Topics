# Restore IP Addresses
# Question: Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# For example: Given "25525511135",
# Return ["255.255.11.135", "255.255.111.35"]. (Order does not matter).
# Solutions:


class Solution:
    # @param s, a string
    # @return a list of strings
    ___ restoreIpAddresses(self, s):
        solution =   # list
        self.restoreIpAddressesRec(s,0,0,  # list,solution)
        r_ solution

    ___ restoreIpAddressesRec(self, s, index, octets, tempSolution, solution):
        if len(s)-index<4-octets:
            r_
        if len(s)-index>3*(4-octets):
            r_
        if octets==4:
            if index== len(s):
                tempSolution.pop()
                solution.append("".join(tempSolution))
                tempSolution.append('.')
            r_
        ___ size __ ra..(1,4):
            if s[index]=='0' and size>1:
                break
            if int(s[index:index+size])>255:
                break
            tempSolution.append(s[index:index+size])
            tempSolution.append('.')
            self.restoreIpAddressesRec(s,index+size,octets+1,tempSolution, solution)
            tempSolution.pop()
            tempSolution.pop()


Solution().restoreIpAddresses("25525511135")