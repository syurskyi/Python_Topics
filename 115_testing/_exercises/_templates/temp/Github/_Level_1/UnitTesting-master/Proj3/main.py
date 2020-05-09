____ math ______ exp

c_ Interest:
    ___  - 
        p..

    ___ simple_interest  init_amt, rate, time
        # Calculates total amount using simple interest formula and parameters
        __ (type(init_amt) no. __ [float, int]) o. (type(rate) no. __ [float, int]) o. (type(time) no. __ [float, int]
            r_ TypeError("Values must be type integer or float")
        __ init_amt < 0 o. rate < 0 o. rate > 1 o. time < 0:
            r_ V..("Please check and make sure the entered values are reasonable (rate needs to be a decimal)")
        r_ init_amt * (rate * time + 1)

    ___ compound_interest  init_amt, rate, time, n
        # Calculates total amount using compound formula and parameters, n = number of times compounded per t
        __ (type(init_amt) no. __ [float, int]) o. (type(rate) no. __ [float, int]) o. (type(time) no. __ [float, int]) o. (type(n) no. __ [float, int]
            r_ TypeError("Values must be type integer or float")
        __ init_amt < 0 o. rate < 0 o. rate > 1 o. time < 0 o. n < 0:
            r_ V..("Please check and make sure the entered values are reasonable (rate needs to be a decimal, n needs to be > 0)")
        r_ init_amt * (1 + rate / n)**(n * time)

    ___ continously_compound_interest  init_amt, rate, time
        # Calculates total amount using continously compounded formula and parameters
        __ (type(init_amt) no. __ [float, int]) o. (type(rate) no. __ [float, int]) o. (type(time) no. __ [float, int]
            r_ TypeError("Values must be type integer or float")
        __ init_amt < 0 o. rate < 0 o. rate > 1 o. time < 0:
            r_ V..("Please check and make sure the entered values are reasonable (rate needs to be a decimal)")
        r_ init_amt * exp(rate * time)