# Day 3 -Assignment
# Cloning  a linked list with next and random pointer

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def clone_list(head):
    if not head:
        return None

    # Step 1: Create copy nodes and store mapping
    old_to_new = {}
    curr = head

    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Step 2: Assign next and random pointers
    curr = head
    while curr:
        copy_node = old_to_new[curr]

        # next pointer
        if curr.next:
            copy_node.next = old_to_new[curr.next]

        # random pointer
        if curr.random:
            copy_node.random = old_to_new[curr.random]

        curr = curr.next

    return old_to_new[head]