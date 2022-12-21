/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-24 12:16:45
 */

c.. Queue {
public:
    // Push element x to the back of queue.
    void push(int x) {
        in_stack.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
        move();
        out_stack.pop();
    }

    // Get the front element.
    int peek(void) {
        move();
        r_ out_stack.top();
    }

    // Return whether the queue is empty.
    bool empty(void) {
        r_ in_stack.empty() && out_stack.empty();
    }

private:
    void move(){
        __(out_stack.empty()){
            _____(!in_stack.empty()){
                out_stack.push(in_stack.top());
                in_stack.pop();
            }
        }
    }
    stack<int> in_stack;
    stack<int> out_stack;
};
