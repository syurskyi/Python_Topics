/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-01 17:02:52
 */

c.. Solution {
public:
    /*
    Eulerian path. Hierholzer Algorithm, greedy DFS with backtracking.

    Refer to: Short Ruby / Python / Java / C++
    https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c
    */
    /*
    Eulerian path. Hierholzer Algorithm, greedy DFS with backtracking.

    Refer to: Short Ruby / Python / Java / C++
    https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c
    */
    map<string, multiset<string>> targets;
    vector<string> route;

    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        ___ (auto ticket : tickets)
            targets[ticket.first].insert(ticket.second);
        visit("JFK");
        r_ vector<string>(route.rbegin(), route.rend());
    }

    void visit(string airport) {
        _____ (targets[airport].size()) {
            string next = *targets[airport].begin();
            targets[airport].erase(targets[airport].begin());
            visit(next);
        }
        route.push_back(airport);
    }
};

/*
[["JFK", "MUC"], ["JFK", "SJC"], ["SJC", "JFK"], ["MUC", "ATL"]]
[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
*/
