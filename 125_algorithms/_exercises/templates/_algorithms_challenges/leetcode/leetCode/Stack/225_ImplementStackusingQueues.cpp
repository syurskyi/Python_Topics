/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-24 13:24:37
 */

c.. Stack {
public:
    // Push element x onto stack.
    // then rotating the queue until the new element is at the front
    void push(int x) {
        q.push(x);
        ___(int i=0;i<q.size()-1;i++){
            q.push(q.front());
            q.pop();
        }
    }

    // Removes the element on top of the stack.
    void pop() {
        q.pop();
    }

    // Get the top element.
    int top() {
        r_ q.front();
    }

    // Return whether the stack is empty.
    bool empty() {
        r_ q.empty();
    }
private:
    queue<int> q{};
};
