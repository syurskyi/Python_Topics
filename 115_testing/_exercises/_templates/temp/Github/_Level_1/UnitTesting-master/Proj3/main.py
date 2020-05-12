____ math ______ exp

c_ Interest:
    ___  - 
        p..

    ___ simple_interest  init_amt, rate, t___
        # Calculates total amount using simple interest formula and parameters
        __ (ty..(init_amt) no. __ [float, __.]) o. (ty..(rate) no. __ [float, __.]) o. (ty..(t___) no. __ [float, __.]
            r_ T..("Values must be type integer or float")
        __ init_amt < 0 o. rate < 0 o. rate > 1 o. t___ < 0:
            r_ V..("Please check and make sure the entered values are reasonable (rate needs to be a decimal)")
        r_ init_amt * (rate * t___ + 1)

    ___ compound_interest  init_amt, rate, t___, n
        # Calculates total amount using compound formula and parameters, n = number of times compounded per t
        __ (ty..(init_amt) no. __ [float, __.]) o. (ty..(rate) no. __ [float, __.]) o. (ty..(t___) no. __ [float, __.]) o. (ty..(n) no. __ [float, __.]
            r_ T..("Values must be type integer or float")
        __ init_amt < 0 o. rate < 0 o. rate > 1 o. t___ < 0 o. n < 0:
            r_ V..("Please check and make sure the entered values are reasonable (rate needs to be a decimal, n needs to be > 0)")
        r_ init_amt * (1 + rate / n)**(n * t___)

    ___ continously_compound_interest  init_amt, rate, t___
        # Calculates total amount using continously compounded formula and parameters
        __ (ty..(init_amt) no. __ [float, __.]) o. (ty..(rate) no. __ [float, __.]) o. (ty..(t___) no. __ [float, __.]
            r_ T..("Values must be type integer or float")
        __ init_amt < 0 o. rate < 0 o. rate > 1 o. t___ < 0:
            r_ V..("Please check and make sure the entered values are reasonable (rate needs to be a decimal)")
        r_ init_amt * exp(rate * t___)