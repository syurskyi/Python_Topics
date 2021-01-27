class HuffmanNode:
    ___ __init__(self, freq, data, left, right
        self.freq = freq;
        self.data = data;
        self.left = left;
        self.right = right;

global charBinaryMapping, str
charBinaryMapping = {}
str = 'ABBCCCCGGGGDEAAAEDBBBDFAGG'


___ generate_tree(mapping

    keySet = mapping.keys()
    priorityQ = []

    ___ c __ keySet:
        node = HuffmanNode(mapping[c], c, None, None)
        priorityQ.append(node)
        priorityQ = sorted(priorityQ, key=lambda x: x.freq)

    while le_(priorityQ) > 1 :
        first = priorityQ.pop(0);
        second = priorityQ.pop(0);
        merge_node = HuffmanNode(first.freq + second.freq, '-', first, second)
        priorityQ.append(merge_node)
        priorityQ = sorted(priorityQ, key=lambda x: x.freq)

    r_ priorityQ.pop();


___ set_binary_code(node, str
    __ not node is None:
        __ node.left is None and node.right is None:
            charBinaryMapping[node.data] = str

        str += '0'
        set_binary_code(node.left, str)
        str = str[:-1]

        str += '1'
        set_binary_code(node.right, str)
        str = str[:-1]


___ encode(str
    mapping = {}
    ___ c __ str:
        __ not c __ mapping:
            mapping[c] = 1
        ____
            mapping[c] += 1

    print(mapping)
    root = generate_tree(mapping)

    set_binary_code(root, '')

    print(' Char | Huffman code ')
    print('----------------------')
    ___ char __ mapping:
        print(' %-4r |%12s' % (char, charBinaryMapping[char]))

    s = ''
    ___ c __ str:
        s += charBinaryMapping[c]
    r_ s


code = encode(str)
print(code)
