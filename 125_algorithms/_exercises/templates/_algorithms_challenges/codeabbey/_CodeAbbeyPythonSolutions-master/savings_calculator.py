amount_values = int(input())
results    # list

___ get_required_year(S,R,P,year):
    __(S > R):
        r.. year
    S += S*P/100
    r.. get_required_year(S,R,P, year+1)

___ i __ r..(amount_values):
    S,R,P = map(int, input().split())
    results.a..(get_required_year(S,R,P,0))

print(*results)
