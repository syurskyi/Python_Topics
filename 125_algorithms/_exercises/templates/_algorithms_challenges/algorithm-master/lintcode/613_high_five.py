"""
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
"""
____ h__ _______ heappop, heappush


c_ Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    ___ highFive  results
        ans    # dict
        __ n.. results:
            r.. ans

        k 5
        top_k    # dict

        ___ r __ results:
            __ r.id n.. __ top_k:
                top_k[r.id]    # list

            heappush(top_k[r.id], r.score)

            __ l..(top_k[r.id]) > k:
                heappop(top_k[r.id])

        _sum 0
        ___ id, scores __ top_k.i..:
            _sum 0
            ___ score __ scores:
                _sum += score

            ans[id] _sum * 1.0 / k

        r.. ans
