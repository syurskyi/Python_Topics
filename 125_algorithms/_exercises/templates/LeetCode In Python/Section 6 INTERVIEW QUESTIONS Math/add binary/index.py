c_ Solution(object
    ___ addBinary(, a, b
        result _ []
        carry _ 0
        i _ le.(a)-1
        j _ le.(b)-1

        w___ i >_ 0 or j >_ 0 or carry:
            total _ carry

            __ i >_ 0:
                total +_ int(a[i])
                i -_ 1
            __ j >_ 0:
                total +_ int(b[j])
                j -_ 1

            result.append(str(total % 2))
            carry _ total//2

        r_ ''.join(reversed(result))
