    sum = 0
    index = 0
    w___ index < le.(change
        __ index __ 0:
            sum += change[index] * 0.25
        ____ index __ 1:
            sum += change[index] * 0.10
        ____ index __ 2:
            sum += change[index] * 0.05
        ____
            sum += change[index] * 0.01
        index += 1
    __ sum >= amount_due:
        r_ True
    ____
        r_ False
