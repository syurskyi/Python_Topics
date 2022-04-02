# Problem: https://www.hackerrank.com/challenges/battery/problem
# Score: 10


_______ pandas __ pd
____ sklearn.linear_model _______ LinearRegression


timeCharged = f__(input())
data = pd.read_csv('trainingdata.txt', names= 'charged', 'lasted' )
train = data[data 'lasted'  < 8]
model = LinearRegression()
model.fit(train 'charged' .values.reshape(-1, 1), train 'lasted' .values.reshape(-1, 1))
ans = model.predict([[timeCharged]])
print(m..(ans[0][0], 8))
