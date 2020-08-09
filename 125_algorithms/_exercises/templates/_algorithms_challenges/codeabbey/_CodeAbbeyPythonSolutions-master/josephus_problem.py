___ get_safe_position(N,K
    safe_position = 0
    ___ i in range(1,N+1
        safe_position = (safe_position+K) % i
    r_ safe_position+1

N,K = map(int, input().split())

print(get_safe_position(N,K))