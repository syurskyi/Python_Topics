____ typing _______ List


___ sum_indices(items: List[s..]) __ i..:
    duplicate_lookup    # dict
    running_total = 0
    ___ i __ r..(l..(items)):
        item = items[i]

        __ item n.. __ duplicate_lookup:
            duplicate_lookup[item] = [i]
            running_total += i
        ____:
            duplicate_lookup[item].a..(i)
            running_total += s..(duplicate_lookup[item])
    
    r.. running_total

        
# if __name__ == "__main__":
#     sum_indices(['a', 'b', 'b', 'c', 'a', 'b', 'a'])