# Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Score: 20


___ climbingLeaderboard(leaderboard, aliceScores):
    rankings = createRankings(leaderboard)
    i = l..(leaderboard) - 1
    ___ score __ aliceScores:
        flag = True
        w.... flag:
            __ i __ -1:
                print(1)
                flag = False
            ____ score < leaderboard[i]:
                print(rankings[i] + 1)
                flag = False
            ____ score __ leaderboard[i]:
                print(rankings[i])
                flag = False
            ____ score > leaderboard[i]:
                i -= 1
    r..


___ createRankings(leaderboard):
    rankings = [1]
    rank = 1
    ___ i __ r..(1, l..(leaderboard)):
        __ leaderboard[i] < leaderboard[i - 1]:
            rank += 1
        rankings.a..(rank)
    r.. rankings


lenOfLeaderboard = int(input())
leaderboard = l..(map(int, input().rstrip().s..()))
lenOfAliceScores = int(input())
aliceScores = l..(map(int, input().rstrip().s..()))
climbingLeaderboard(leaderboard, aliceScores)
