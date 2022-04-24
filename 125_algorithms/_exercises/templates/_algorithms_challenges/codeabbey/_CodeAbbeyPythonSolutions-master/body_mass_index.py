amount_values i..(input
results    # list

___ get_bmi(weight, height
    r.. weight/height**2

___ i __ r..(amount_values
    weight, height m.. f__, i.. ).s..
    bmi get_bmi(weight, height)
    __(bmi < 18.5
        results.a..("under")
    ____(bmi >_ 18.5 a.. bmi < 25
        results.a..("normal")
    ____(bmi >_ 25 a.. bmi < 30
        results.a..("over")
    ____
        results.a..("obese")

print(*results)
