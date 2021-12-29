_______ numpy as np
f = open('input.txt')
res    # list

T = int(f.readline().strip())

boards    # list
___ i __ r..(0,T):
    boards.a..(f.readline().s...s..(' '))

___ i __ r..(T):
    a = [int(j) ___ j __ boards[i]]
    A = np.array([[a[0],1],[a[2],1]])
  
    b = np.array([a[1],a[3]])
    z = np.linalg.solve(A,b)
    __ n.. z[1].is_integer():
        z[1] = z[1] + 0.5
    __ z[1] - int(z[1]) < 0:
        z[1] = round(z[1] - 0.5)
        
    __ n.. z[0].is_integer():
        z[0] = z[0] + 0.5
    __ z[0] - int(z[0]) < 0:
        z[0] = round(z[0]  - 0.5)
    string = '('+s..(int(z[0]))+' '+s..(int(z[1]))+')'
    res.a..(string)
                                  
final = ' '.join(s..(e) ___ e __ res)
print(final)