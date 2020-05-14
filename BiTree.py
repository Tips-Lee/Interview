from collections import deque

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


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
root = E


def pre_order(root):
    if root:
        print(root.data, end='')
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end='')
        in_order(root.rchild)


def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end='')


def level_order(root):
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


if __name__ == '__main__':
    pre_order(root)
    print('\n' + '==' * 20)
    in_order(root)
    print('\n' + '==' * 20)
    post_order(root)
    print('\n' + '==' * 20)
    level_order(root)
    print('\n' + '==' * 20)
    broken_order(root)
