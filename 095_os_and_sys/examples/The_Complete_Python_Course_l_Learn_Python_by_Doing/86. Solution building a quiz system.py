# read from questions.txt and append each line into a list
questions = open('questions.txt', 'r')  # read from questions.txt
question_list = [line.strip() for line in
                 questions.readlines()]  # read all lines and get rid of line break for each line,
                                         # then append each stripped line to a list

questions.close()

score = 0  # initialize score
total = len(question_list)  # set total score

for line in question_list:
    q, a = line.split('=')  # split equation with `=` into question and answer
    ans = input('{}='.format(q))  # print question and wait for user to input their answer
    if a == ans:  # if user input matches answer
        score += 1  # increase score

result = open('result.txt', 'w')  # open result.txt
result.write('Your final score is {}/{}.'.format(score, total))  # write final score to result.txt
result.close()