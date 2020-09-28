from collections import deque

def solution(n):
    tree = Tree(int(n))
    return(tree.get_depth(tree.find_1()))

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def create_children(self):
        if self.data % 2 == 0:
            self.children.append(Node(self.data/2, self))
        if self.parent is None:
            self.children.append(Node(self.data-1, self))
            self.children.append(Node(self.data+1, self))
        else:
            if self.data - 1 != self.parent.data:
                self.children.append(Node(self.data-1, self))
            if self.data + 1 != self.parent.data:
                self.children.append(Node(self.data+1, self))


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def find_1(self):
        curr_node = self.root
        q = deque()
        while True:
            curr_node.create_children()
            for child in curr_node.children:
                if child.data == 1:
                    return child
                q.append(child)
            curr_node = q[0]
            q.popleft()

    def get_depth(self, node):
        counter = 0
        while True:
            if node.data == self.root.data:
                return counter
            counter += 1
            node = node.parent

def test(n):
    for i in range(1,n+1):
        print(i,solution(i))
print(solution(12181))
