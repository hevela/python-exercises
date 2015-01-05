# -*- coding: utf-8 -*-


class Node(object):
    next = None
    data = None

    def __init__(self, data):
        self.data = data

    def append_tail(self, data):
        end = Node(data)
        node = self
        while node.next:
            node = node.next
        node.next = end

    def __str__(self):
        node = self
        strng = str(node.data)
        while node.next:
            node = node.next
            strng += '->' + str(node.data)
        return strng


def delete_node(head, data):
    """
    Deletes a node containing data and moves the head
    :param head: the head node
    :type head: Node
    :param data: the content of the node to delete
    :return:
    """
    node = head
    if node.data == data:
        #returns the nex node (moves the head)
        return head.next
    while node.next:
        if node.next.data == data:
            #inner node removed, skipps the matched node
            node.next = node.next.next
            return head
        node = node.next


def remove_node(head, node):
    if head == node:
        return head.next
    h = head
    while h.next:
        if node == h.next:
            h.next = h.next.next
            return head
        h = h.next


def remove_duplicated(head):
    if not isinstance(head, Node):
        raise Exception("Node object expected")
    table = dict()
    node = head
    while node:
        if str(node.data) in table.keys():
            delete_node(head, node.data)
        else:
            table[str(node.data)] = str(node.data)
        node = node.next


def remove_duplicated_wb(head):
    node = head
    while node:
        temp = head
        cont = 0
        while temp:
            if temp.data == node.data:
                cont += 1
            if cont == 2:
                delete_node(head, node.data)
                break
            temp = temp.next
        node = node.next


def find_nth_to_last(head, nth):
    node = head
    list_ = list()
    while node:
        list_.append(node)
        node = node.next
    return list_[-1*nth]