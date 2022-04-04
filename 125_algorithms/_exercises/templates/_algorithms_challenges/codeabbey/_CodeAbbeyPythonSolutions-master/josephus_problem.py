___ get_safe_position(N,K
    safe_position = 0
    ___ i __ r..(1,N+1
        safe_position = (safe_position+K) % i
    r.. safe_position+1

N,K = map(i.., input().s..

print(get_safe_position(N,K