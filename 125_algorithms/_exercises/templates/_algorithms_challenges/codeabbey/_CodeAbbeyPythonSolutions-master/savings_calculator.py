amount_values = int(input())
results = []

___ get_required_year(S,R,P,year):
    __(S > R):
        return year
    S += S*P/100
    return get_required_year(S,R,P, year+1)

for i in range(amount_values):
    S,R,P = map(int, input().split())
    results.append(get_required_year(S,R,P,0))

print(*results)
