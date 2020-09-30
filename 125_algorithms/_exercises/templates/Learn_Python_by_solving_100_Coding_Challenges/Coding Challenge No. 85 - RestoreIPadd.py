# Restore IP Addresses
# Question: Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# For example: Given "25525511135",
# Return ["255.255.11.135", "255.255.111.35"]. (Order does not matter).
# Solutions:


c_ Solution:
    # @param s, a string
    # @return a list of strings
    ___ restoreIpAddresses(self, s):
        solution _   # list
        restoreIpAddressesRec(s,0,0,  # list,solution)
        r_ solution

    ___ restoreIpAddressesRec(self, s, index, octets, tempSolution, solution):
        __ le.(s)-index<4-octets:
            r_
        __ le.(s)-index>3*(4-octets):
            r_
        __ octets__4:
            __ index__ le.(s):
                tempSolution.p..()
                solution.ap..("".join(tempSolution))
                tempSolution.ap..('.')
            r_
        ___ size __ ra..(1,4):
            __ s[index]__'0' an. size>1:
                break
            __ in.(s[index:index+size])>255:
                break
            tempSolution.ap..(s[index:index+size])
            tempSolution.ap..('.')
            restoreIpAddressesRec(s,index+size,octets+1,tempSolution, solution)
            tempSolution.p..()
            tempSolution.p..()


Solution().restoreIpAddresses("25525511135")