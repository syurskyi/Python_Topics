/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-23 11:57:19
 */

c.. Solution {
public:
    /*
    Same as "max subarray problem" using Kadane's Algorithm

    Just need one scan through the array values,
    computing at each position the max profit ending at that position.

    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    */
    int maxProfit(vector<int>& prices) {
        __(prices.size() __ 0)  r_ 0;
        int min_buy = prices[0], max_pro = 0;
        ___(int i=1; i<prices.size(); i++){
            int cur_price = prices[i];
            min_buy = (min_buy <= cur_price ? min_buy : cur_price);
            max_pro = (max_pro >= cur_price - min_buy ? max_pro :cur_price-min_buy);
        }
        r_ max_pro;
    }
};

c.. Solution_2{
public:
    /*
    sell_1: The maximum if we've just sold 1nd stock so far.
    buy_1: The maximum if we've just buy 1st stock so far.

    Then we can update sell_1 if p + buy_1(sell now) get more than pre-sell_1.
    And update buy_1 if remain more money when we buy now than pre-buy_1.
    Here update sell_1 before buy_1 because we need to use pre_buy_1 to get sell_1.
    */
    int maxProfit(vector<int>& prices) {
        int sell_1 = 0, buy_1 = INT_MIN;
        ___(int p: prices){
            sell_1 = m..(sell_1, p+buy_1);
            buy_1 = m..(buy_1, -p);
        }
        r_ sell_1;
    }
};

/*
[]
[3,4,5,6,2,4]
[6,5,4,3,2,1]
[1,2,3,4,3,2,1,9,11,2,20]
*/
