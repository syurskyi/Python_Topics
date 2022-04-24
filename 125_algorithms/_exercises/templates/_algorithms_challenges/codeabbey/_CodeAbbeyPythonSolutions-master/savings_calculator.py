amount_values i..(input
results    # list

___ get_required_year(S,R,P,year
    __(S > R
        r.. year
    S += S*P/100
    r.. get_required_year(S,R,P, year+1)

___ i __ r..(amount_values
    S,R,P m.. i.., i.. ).s..
    results.a..(get_required_year(S,R,P,0

print(*results)
