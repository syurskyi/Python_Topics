# read from questions.txt and append each line into a list
questions = o..('questions.txt', 'r')  # read from questions.txt
question_list = [line.strip() ___ line __
                 questions.readlines()]  # read all lines and get rid of line break for each line,
                                         # then append each stripped line to a list

questions.close()

score = 0  # initialize score
total = len(question_list)  # set total score

___ line __ question_list:
    q, a = line.split('=')  # split equation with `=` into question and answer
    ans = input('{}='.f..(q))  # print question and wait for user to input their answer
    if a == ans:  # if user input matches answer
        score += 1  # increase score

result = o..('result.txt', 'w')  # open result.txt
result.w..('Your final score is {}/{}.'.f..(score, total))  # write final score to result.txt
result.close()