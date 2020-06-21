# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ]

# initializing their scores
scores = [100, 15, 17, 28, 43 ]

# printing players and scores.
for pl, sc in zip(players, scores):
	print ("Player : %s	 Score : %d" %(pl, sc))

# Output:
#
# Player :  Sachin     Score : 100
# Player :  Sehwag     Score : 15
# Player :  Gambhir     Score : 17
# Player :  Dravid     Score : 28
# Player :  Raina     Score : 43