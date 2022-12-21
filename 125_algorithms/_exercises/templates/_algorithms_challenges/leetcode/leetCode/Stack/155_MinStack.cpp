/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-15 16:10:01
 */


c.. MinStack {
public:
    void push(int x) {
        data.push(x);
        __(min_n.empty() || x <= getMin()){
            min_n.push(x);
        }
    }

    void pop() {
        __(top() __ getMin()){
            min_n.pop();
        }
        data.pop();
    }

    int top() {
        r_ data.top();
    }

    int getMin() {
        r_ min_n.top();
    }
private:
    stack<int> data;
    stack<int> min_n;
};
