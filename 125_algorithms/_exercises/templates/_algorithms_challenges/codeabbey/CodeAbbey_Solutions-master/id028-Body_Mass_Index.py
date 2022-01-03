___ BMI(users):
        pairCount = 0
        answer    # list
        w.... pairCount < users:
                pair = raw_input()
                numbers = pair.s..(' ')
                weight = float(numbers[0])
                height = float(numbers[1])
                BMI = float(weight / (height * height))

                __ BMI < 18.5:
                        answer.a..(s..('under'))
                ____ BMI >= 18.5 a.. BMI < 25.0:
                        answer.a..(s..('normal'))
                ____ BMI >= 25.0 a.. BMI < 30.0:
                        answer.a..(s..('over'))
                ____ BMI >= 30.0:
                        answer.a..(s..('obese'))
                ____:
                        print("Error.")
                pairCount += 1
        print(' '.j..(answer))
BMI(input())
