# Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Score: 20


___ climbingLeaderboard(leaderboard, aliceScores
    rankings = createRankings(leaderboard)
    i = le.(leaderboard) - 1
    for score in aliceScores:
        flag = True
        w___ flag:
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
    r_


___ createRankings(leaderboard
    rankings = [1]
    rank = 1
    for i in range(1, le.(leaderboard)):
        __ leaderboard[i] < leaderboard[i - 1]:
            rank += 1
        rankings.append(rank)
    r_ rankings


lenOfLeaderboard = int(input())
leaderboard = list(map(int, input().rstrip().split()))
lenOfAliceScores = int(input())
aliceScores = list(map(int, input().rstrip().split()))
climbingLeaderboard(leaderboard, aliceScores)
