c_ HuffmanNode:
    ___  -   freq, data, left, right
        freq  freq;
        data  data;
        left  left;
        right  right;

global charBinaryMapping, st.
charBinaryMapping  {}
st.  'ABBCCCCGGGGDEAAAEDBBBDFAGG'


___ generate_tree(mapping

    keySet  mapping.keys()
    priorityQ  []

    ___ c __ keySet:
        node  HuffmanNode(mapping[c], c, N.., N..)
        priorityQ.ap..(node)
        priorityQ  s..(priorityQ, keylambda x: x.freq)

    w__ le_(priorityQ) > 1 :
        first  priorityQ.pop(0);
        second  priorityQ.pop(0);
        merge_node  HuffmanNode(first.freq + second.freq, '-', first, second)
        priorityQ.ap..(merge_node)
        priorityQ  s..(priorityQ, keylambda x: x.freq)

    r_ priorityQ.pop();


___ set_binary_code(node, st.
    __ no. node __ N..:
        __ node.left __ N.. a__ node.right __ N..:
            charBinaryMapping[node.data]  st.

        st. + '0'
        set_binary_code(node.left, st.)
        st.  st.[:-1]

        st. + '1'
        set_binary_code(node.right, st.)
        st.  st.[:-1]


___ encode(st.
    mapping  {}
    ___ c __ st.:
        __ no. c __ mapping:
            mapping[c]  1
        ____
            mapping[c] + 1

    print(mapping)
    root  generate_tree(mapping)

    set_binary_code(root, '')

    print(' Char | Huffman code ')
    print('----------------------')
    ___ char __ mapping:
        print(' %-4r |%12s' % (char, charBinaryMapping[char]))

    s  ''
    ___ c __ st.:
        s + charBinaryMapping[c]
    r_ s


code  encode(st.)
print(code)
