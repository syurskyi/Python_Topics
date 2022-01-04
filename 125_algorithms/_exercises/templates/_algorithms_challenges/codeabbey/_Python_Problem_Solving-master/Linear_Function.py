_______ numpy __ np
f = open('input.txt')
res    # list

T = i..(f.readline().strip())

boards    # list
___ i __ r..(0,T):
    boards.a..(f.readline().s...s..(' '))

___ i __ r..(T):
    a = [i..(j) ___ j __ boards[i]]
    A = np.array([[a[0],1],[a[2],1]])
  
    b = np.array([a[1],a[3]])
    z = np.linalg.solve(A,b)
    __ n.. z[1].is_integer
        z[1] = z[1] + 0.5
    __ z[1] - i..(z[1]) < 0:
        z[1] = round(z[1] - 0.5)
        
    __ n.. z[0].is_integer
        z[0] = z[0] + 0.5
    __ z[0] - i..(z[0]) < 0:
        z[0] = round(z[0]  - 0.5)
    string = '('+s..(i..(z[0]))+' '+s..(i..(z[1]))+')'
    res.a..(string)
                                  
final = ' '.j..(s..(e) ___ e __ res)
print(final)