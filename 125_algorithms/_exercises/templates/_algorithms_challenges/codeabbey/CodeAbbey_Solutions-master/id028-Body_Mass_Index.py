___ BMI(users):
        pairCount = 0
        answer    # list
        while pairCount < users:
                pair = raw_input()
                numbers = pair.split(' ')
                weight = float(numbers[0])
                height = float(numbers[1])
                BMI = float(weight / (height * height))

                __ BMI < 18.5:
                        answer.a..(str('under'))
                ____ BMI >= 18.5 and BMI < 25.0:
                        answer.a..(str('normal'))
                ____ BMI >= 25.0 and BMI < 30.0:
                        answer.a..(str('over'))
                ____ BMI >= 30.0:
                        answer.a..(str('obese'))
                ____:
                        print("Error.")
                pairCount += 1
        print(' '.join(answer))
BMI(input())
