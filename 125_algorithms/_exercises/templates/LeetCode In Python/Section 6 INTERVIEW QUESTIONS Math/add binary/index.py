class Solution(object
    ___ addBinary(self, a, b
        result = []
        carry = 0
        i = le.(a)-1
        j = le.(b)-1

        w___ i >= 0 or j >= 0 or carry:
            total = carry

            __ i >= 0:
                total += int(a[i])
                i -= 1
            __ j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total//2

        r_ ''.join(reversed(result))
