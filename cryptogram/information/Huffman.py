class BTreeNode:

    def __init__(self, right=None, left=None, parent=None,
                 weight=0, char=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.weight = weight
        self.char = char


class Huffman:

    def __init__(self, code):

        self.nodes = []
        for e in code.keys():
            self.nodes.append(BTreeNode(weight=code[e], char=e))

        tree = Huffman.sort(self.nodes)

        while len(tree) != 1:
            a, b = tree[0], tree[1]
            new = BTreeNode(weight=a.weight + b.weight, left=a, right=b)
            a.parent, b.parent = new, new
            tree.remove(a), tree.remove(b)
            tree.append(new)
            tree = Huffman.sort(tree)

        self.root = tree[0]
        self.encode = {}
        self.coding()

    def coding(self):

        if self.encode != {}:
            return self.encode

        encode = {}

        for e in self.nodes:
            t = e
            encode.setdefault(e.char, "")
            while t != self.root:
                encode[e.char] = ["0", "1"][
                    t.parent.left == t] + encode[e.char]
                t = t.parent

        self.encode = encode

    def __str__(self):
        if self.encode == {}:
            self.coding()

        return str(self.encode)

    @staticmethod
    def sort(l):
        return sorted(l, key=lambda node: node.weight)


def main():
    code = {'a': 0.32, 'b': 0.22, 'c': 0.18,
            'd': 0.16, 'e': 0.08, 'f': 0.04}

    print Huffman(code).encode

if __name__ == '__main__':
    main()
