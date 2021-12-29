___ findMeetup(meetups):
    answer    # list
    ___ meetup __ r..(meetups):
        data = raw_input().s..
        distance,speedA,speedB = int(data[0]),int(data[1]),int(data[2])
        ETA = (distance / float(speedA + speedB))
        solution = ETA * speedA
        answer.a..(str(solution))
    print(' '.join(answer))
findMeetup(input())
