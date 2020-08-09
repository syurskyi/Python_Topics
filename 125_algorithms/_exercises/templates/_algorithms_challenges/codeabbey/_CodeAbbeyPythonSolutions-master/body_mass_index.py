amount_values = int(input())
results = []

___ get_bmi(weight, height
    r_ weight/height**2

___ i in range(amount_values
    weight, height = map(float, input().split())
    bmi = get_bmi(weight, height)
    __(bmi < 18.5
        results.append("under")
    ____(bmi >= 18.5 and bmi < 25
        results.append("normal")
    ____(bmi >= 25 and bmi < 30
        results.append("over")
    ____
        results.append("obese")

print(*results)
