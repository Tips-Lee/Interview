from BiSearchTree import BiSearchTree, BiTreeNode
from random import shuffle

class AVLNode(BiTreeNode):
    def __init__(self, data):
        super(AVLNode, self).__init__(data)
        self.bf = 0


class AVLTree(BiSearchTree):
    def __init__(self, li):
        super(AVLTree, self).__init__(li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        c.parent = p.parent
        c.lchild = p
        p.parent = c
        p.rchild = s2
        if s2:
            s2.parent = p
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.rchild
        c.parent = p.parent
        c.rchild = p
        p.parent = c
        p.lchild = s2
        if s2:
            s2.parent = p
        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.lchild
        s2 = g.lchild
        s3 = g.rchild
        g.parent = p.parent
        g.lchild = p
        g.rchild = c
        p.rchild = s2
        p.parent = g
        c.lchild = s3
        c.parent = g
        if s2:
            s2.parent = p
        if s3:
            s3.parent = c
        if g.bf > 0:
            c.bf = 0
            p.bf = -1
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            p.bf = c.bf = 0
            g.bf = 0

        return g

    def rotate_left_right(self, p, c):
        g = c.rchild
        s2 = g.rchild
        s3 = g.lchild
        g.parent = p.parent
        g.rchild = p
        g.lchild = c
        p.lchild = s2
        p.parent = g
        c.rchild = s3
        c.parent = g
        if s2:
            s2.parent = p
        if s3:
            s3.parent = c
        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            c.bf = 0
            p.bf = 1
        else:
            p.bf = c.bf = 0
        g.bf = 0
        return g

    def insert_without_rec(self, val):
        p = self.root
        if not p:
            node = AVLNode(val)
            self.root = node
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    node = AVLNode(val)
                    p.lchild = node
                    p.lchild.parent = p
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    node = AVLNode(val)
                    p.rchild = node
                    p.rchild.parent = p
                    break
            else:
                raise Exception('inserted duplicated val')

        while node.parent:
            if node.parent.lchild == node:
                if node.parent.bf > 0:
                    node.parent.bf = 0
                    break
                elif node.parent.bf == 0:
                    node.parent.bf = -1
                    node = node.parent
                    continue
                else:
                    g = node.parent.parent
                    x = node.parent
                    node.parent.bf = -2
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
            else:
                if node.parent.bf > 0:
                    g = node.parent.parent
                    x = node.parent
                    node.parent.bf = 2
                    if node.bf > 0:
                        n = self.rotate_left(node.parent, node)
                    else:
                        n = self.rotate_right_left(node.parent, node)
                elif node.parent.bf == 0:
                    node.parent.bf = 1
                    node = node.parent
                    continue
                else:
                    node.parent.bf = 0
                    break
            # n.parent = g
            if g:
                if g.lchild == x:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


if __name__ == '__main__':
    li = list(range(20))
    shuffle(li)
    # node = AVLNode('A')
    tree = AVLTree(li)
    tree.in_order(tree.root)