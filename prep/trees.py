# -*- coding: utf-8 -*-


class TreeNode(object):
    left = None
    rigth = None
    data = None

    def __init__(self, data):
        self.data = int(data)

    def add_leaf(self, data):
        if data < self.data:
            #add to left brach
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.add_leaf(data)
        else:
            #add to rigth brach
            if self.rigth is None:
                self.rigth = TreeNode(data)
            else:
                self.rigth.add_leaf(data)

    def print_depth(self):
        if self.data:
            data = [self.data]
        else:
            data = []
        if self.left:
            data += self.left.print_depth()
        if self.rigth:
            data += self.rigth.print_depth()
        return data

    def print_breadth(self):
        data = []
        curr_level = [self]
        while curr_level:
            next_level = []
            for n in curr_level:
                data.append(n.data)
                if n.left:
                    next_level.append(n.left)
                if n.rigth:
                    next_level.append(n.rigth)
                curr_level = next_level
        return data

    def search_breadth(self, data):
        pass

    def search_depth(self, data):
        pass


def is_balanced(tree_node):
    def max_depth(node):
        if node is None:
            return 0
        else:
            return 1 + max((max_depth(node.left), max_depth(node.rigth)))

    def min_depth(node):
        if node is None:
            return 0
        else:
            return 1 + min((min_depth(node.left), min_depth(node.rigth)))
    return (max_depth(tree_node) - min_depth(tree_node)) <= 1