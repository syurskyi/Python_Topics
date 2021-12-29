# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Score: 10


k = int(input())
room_number_list = l..(map(int, input().split()))
captain_room_number = (s..(set(room_number_list)) * k - s..(room_number_list)) // (k - 1)
print(captain_room_number)
