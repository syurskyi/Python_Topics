/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-08-21 09:10:58
 */

c.. Solution {
public:
    int myAtoi(string str){
        /*
        We need to handle four cases:

        1. discards all leading whitespaces
        2. sign of the number
        3. overflow
        4. invalid input
        */
        const int l.. = str.size();

        int i=0;
        // Skip starting whitespace as many as possible.
        _____ (str[i]__' ' && i<l..) i++;

        int sign = 1;
        // Read plus or minus sign.
        __(str[i] __ '+') i++;
        else __(str[i] __ '-'){
            i++;
            sign = -1;
        }

        int num = 0;
        ___(; i<l..; i++){
            __(str[i] < '0' || str[i] > '9'){
                break;
            }
            __(num > INT_MAX/10 || (num __ INT_MAX / 10 && (str[i]-'0') > INT_MAX % 10)){
                r_ sign __ -1 ? INT_MIN : INT_MAX;
            }
            num = num * 10 + str[i] - '0';
        }

        r_ num * sign;
    }
};

/*
""
"  12a"
"  a12"
"  +12"
"  +-12"
"2147483648"
"-2147483648"
*/
