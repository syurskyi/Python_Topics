c.. Solution {
public:
    int longestValidParentheses(string s) {
        /*
        According to:
        https://leetcode.com/discuss/7609/my-o-n-solution-using-a-stack

        If current character is '(', push its index to the stack.
        If current character is ')':
        1. top of stack is '(', just find a matching pair so pop from the stack.
        2. Otherwise, we push the index of ')' to the stack.

        Finally the stack will only contain the indices of characters which cannot be matched.
        Then the substring between adjacent indices should be valid parentheses.
        */
        stack<int> stk;
        int longest = 0;
        ___ (int i=0; i<s.size();i++){
            __(s[i] __ '('){
                stk.push(i);
            }
            else{
                __ (!stk.empty() a.. s[stk.top()] __ '('){
                    stk.pop();
                    __ (!stk.empty()) longest = longest > i-stk.top() ? longest : i-stk.top();
                    else              longest = longest > i+1 ? longest : i+1;
                }
                else{
                    stk.push(i);
                }
            }
        }
        r_ longest;
    }
};

/*
""
")"
"()"
"))"
"(((()()()))("
"(((()()()))())"
*/
