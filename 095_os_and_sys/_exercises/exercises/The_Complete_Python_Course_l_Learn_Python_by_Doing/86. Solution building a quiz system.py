# read from questions.txt and append each line into a list
questions _ o..('questions.txt', 'r')  # read from questions.txt
question_list _ [line.strip() ___ line __
                 questions.readlines()]  # read all lines and get rid of line break for each line,
                                         # then append each stripped line to a list

questions.close()

score _ 0  # initialize score
total _ le.(question_list)  # set total score

___ line __ question_list:
    q, a _ line.split('=')  # split equation with `=` into question and answer
    ans _ input('@='.f..(q))  # print question and wait for user to input their answer
    __ a __ ans:  # if user input matches answer
        score +_ 1  # increase score

result _ o..('result.txt', 'w')  # open result.txt
result.w..('Your final score is @/@.'.f..(score, total))  # write final score to result.txt
result.close()