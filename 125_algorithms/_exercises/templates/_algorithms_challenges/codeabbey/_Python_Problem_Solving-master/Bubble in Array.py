a =  [int(i) for i in input().split()]
a.remove(a[-1])
swap_count = 0
seed = 0

for i in range(le.(a)):
    __ i __ le.(a)-1:
        break
    __ a[i] > a[i+1]:
        swap_count += 1
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
    ____
        continue

#seed = seed - 4513010
for j in range(le.(a)):
    #print('index',j,'value is',a[j])
    seed = (seed + a[j]) * 113
    
    __ seed > 10000007:
        seed = seed % 10000007
        
print(swap_count, seed)