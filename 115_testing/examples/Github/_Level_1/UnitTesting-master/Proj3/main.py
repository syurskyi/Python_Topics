from math import exp

class Interest:
    def __init__(self):
        pass

    def simple_interest(self, init_amt, rate, time): 
        # Calculates total amount using simple interest formula and parameters
        if (type(init_amt) not in [float, int]) or (type(rate) not in [float, int]) or (type(time) not in [float, int]):
            raise TypeError("Values must be type integer or float")
        if init_amt < 0 or rate < 0 or rate > 1 or time < 0:
            raise ValueError("Please check and make sure the entered values are reasonable (rate needs to be a decimal)")
        return init_amt * (rate * time + 1)

    def compound_interest(self, init_amt, rate, time, n): 
        # Calculates total amount using compound formula and parameters, n = number of times compounded per t
        if (type(init_amt) not in [float, int]) or (type(rate) not in [float, int]) or (type(time) not in [float, int]) or (type(n) not in [float, int]):
            raise TypeError("Values must be type integer or float")
        if init_amt < 0 or rate < 0 or rate > 1 or time < 0 or n < 0:
            raise ValueError("Please check and make sure the entered values are reasonable (rate needs to be a decimal, n needs to be > 0)")
        return init_amt * (1 + rate / n)**(n * time)

    def continously_compound_interest(self, init_amt, rate, time): 
        # Calculates total amount using continously compounded formula and parameters
        if (type(init_amt) not in [float, int]) or (type(rate) not in [float, int]) or (type(time) not in [float, int]):
            raise TypeError("Values must be type integer or float")
        if init_amt < 0 or rate < 0 or rate > 1 or time < 0:
            raise ValueError("Please check and make sure the entered values are reasonable (rate needs to be a decimal)")
        return init_amt * exp(rate * time)