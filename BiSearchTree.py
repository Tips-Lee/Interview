from collections import deque
import random


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


def broken_order(root):
    tmp1 = deque([root])
    tmp2 = deque()
    reverse = False
    ans = deque()
    while tmp1:
        sub_ans = deque()
        # 取出tmp1的值，并得到tmp2
        while tmp1:
            node = tmp1.popleft()
            sub_ans.append(node.data)
            if node.lchild:
                tmp2.append(node.lchild)
            if node.rchild:
                tmp2.append(node.rchild)
        if reverse:
            sub_ans.reverse()
        ans.extend(sub_ans)
        tmp1 = tmp2
        tmp2 = deque()
        reverse = not reverse
    print(''.join(ans))
    # return ans


def define_tree():
    A = BiTreeNode('A')
    B = BiTreeNode('B')
    C = BiTreeNode('C')
    D = BiTreeNode('D')
    E = BiTreeNode('E')
    F = BiTreeNode('F')
    G = BiTreeNode('G')
    E.lchild = A
    E.rchild = G
    A.rchild = C
    G.rchild = F
    C.lchild = B
    C.rchild = D
    return E


class BiSearchTree:
    def __init__(self, li):
        self.root = None
        if li:
            for val in li:
                self.insert_without_rec(val)

    def pre_order(self, root):
        if root:
            print(root.data, end='')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=' ')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end='')

    def level_order(self, root):
        q = deque()
        # q = []
        q.appendleft(root)
        while q:
            node = q.pop()
            print(node.data, end='')
            if node.lchild:
                q.appendleft(node.lchild)
            if node.rchild:
                q.appendleft(node.rchild)

    def insert_without_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def query(self, node, val):
        if not node:
            return
        if node.data > val:
            return self.query(node.lchild, val)
        elif node.data < val:
            return self.query(node.rchild, val)
        else:
            return node

    def query_without_rec(self, val):
        p = self.root
        if not p:
            return
        while p:
            if p.data > val:
                p = p.lchild
            elif p.data < val:
                p = p.rchild
            else:
                return p
        return

    def __remove_node_1(self, node):
        # node 是叶子节点
        if not node.parent:
            self.root = None
        elif node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    def __remove_node_21(self, node):
        # node 只有一个左节点
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # node 只有一个右节点
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def __remove_node_3(self, node):
        min_node = node.rchild
        while min_node.lchild:
            min_node = min_node.lchild
        node.data = min_node.data
        if not min_node.rchild:
            self.__remove_node_1(min_node)
        else:
            self.__remove_node_22(min_node)

    def delete_node(self, val):
        node = self.query_without_rec(val)
        if not node:
            raise KeyError('No val')
        if not node.lchild and not node.rchild:
            self.__remove_node_1(node)
        elif not node.rchild:
            self.__remove_node_21(node)
        elif not node.lchild:
            self.__remove_node_22(node)
        else:
            self.__remove_node_3(node)


if __name__ == '__main__':
    random.seed(2)
    root = define_tree()
    # pre_order(root)
    # print('\n' + '==' * 20)
    # in_order(root)
    # print('\n' + '==' * 20)
    # post_order(root)
    # print('\n' + '==' * 20)
    # level_order(root)
    # print('\n' + '==' * 20)
    # broken_order(root)
    li = list(range(10))
    random.shuffle(li)
    bst = BiSearchTree(li)
    # bst.level_order(bst.root)
    print(li)
    bst.in_order(bst.root)
    bst.delete_node(2)
    print('')
    bst.in_order(bst.root)
    # print(bst.query(bst.root, 3))
    # print(bst.query_without_rec(3))
