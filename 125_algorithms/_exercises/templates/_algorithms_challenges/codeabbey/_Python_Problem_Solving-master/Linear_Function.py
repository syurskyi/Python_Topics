_______ numpy __ np
f = o.. 'input.txt')
res    # list

T = i..(f.readline().strip

boards    # list
___ i __ r..(0,T
    boards.a..(f.readline().s...s..(' '))

___ i __ r..(T
    a = [i..(j) ___ j __ boards[i]]
    A = np.array([[a[0],1],[a[2],1]])
  
    b = np.array([a[1],a[3]])
    z = np.linalg.solve(A,b)
    __ n.. z[1].is_integer
        z[1] = z[1] + 0.5
    __ z[1] - i..(z[1]) < 0:
        z[1] = r..(z[1] - 0.5)
        
    __ n.. z[0].is_integer
        z[0] = z[0] + 0.5
    __ z[0] - i..(z[0]) < 0:
        z[0] = r..(z[0]  - 0.5)
    s__ = '('+s..(i..(z[0]))+' '+s..(i..(z[1]))+')'
    res.a..(s__)
                                  
final = ' '.j..(s..(e) ___ e __ res)
print(final)