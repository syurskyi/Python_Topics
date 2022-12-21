/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-23 14:30:18
 */

c.. Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        size_t days = prices.size();
        __(k__0 || days<2){
            r_ 0;
        }

        __(k>prices.size()/2){
            r_ solve_quickly(prices);
        }

        vector<vector<int>> dp(k+1, vector<int>(days, 0));
        ___(int i=1; i<= k; i++){
            int max_buy = -prices[0];
            ___(int j=1; j<days; j++){
                dp[i][j] = m..(dp[i][j-1], max_buy+prices[j]);
                max_buy = m..(max_buy, dp[i-1][j-1]-prices[j]);
            }
        }
        r_ dp[k][days-1];
    }

    int solve_quickly(vector<int> &prices){
        int max_profit = 0;
        ___(int i=1; i<prices.size(); i++){
            int diff = prices[i] - prices[i-1];
            max_profit += diff > 0 ? diff : 0;
        }
        r_ max_profit;
    }
};

/*
1
[8,5,3]
2
[1,8,3,2,7,12,7,15,16,17]
4
[1,8,3,2,7,12,7,15,16,17]
*/
