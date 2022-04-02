# Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Score: 20


___ climbingLeaderboard(leaderboard, aliceScores
    rankings = createRankings(leaderboard)
    i = l..(leaderboard) - 1
    ___ score __ aliceScores:
        flag = T..
        w.... flag:
            __ i __ -1:
                print(1)
                flag = F..
            ____ score < leaderboard[i]:
                print(rankings[i] + 1)
                flag = F..
            ____ score __ leaderboard[i]:
                print(rankings[i])
                flag = F..
            ____ score > leaderboard[i]:
                i -= 1
    r..


___ createRankings(leaderboard
    rankings = [1]
    rank = 1
    ___ i __ r..(1, l..(leaderboard)):
        __ leaderboard[i] < leaderboard[i - 1]:
            rank += 1
        rankings.a..(rank)
    r.. rankings


lenOfLeaderboard = i..(input())
leaderboard = l.. m..(i.., input().rstrip().s..()))
lenOfAliceScores = i..(input())
aliceScores = l.. m..(i.., input().rstrip().s..()))
climbingLeaderboard(leaderboard, aliceScores)
