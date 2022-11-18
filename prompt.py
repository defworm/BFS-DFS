# Given a binary tree, write a program to find out the largest value in each row of a given binary tree.

# Input: [5, 3, 8, 2, 4, null, 9] Result: [5, 8, 9]

from collections import deque


class Node:  # Tree Node
    def __init__(self, key):
        if key == "null":
            self.data = None
        else:
            self.data = key
        self.left = None
        self.right = None

def levelMax(root):


    Q = deque()  # we're using the deque Q as a queue.
    V = []
    M = set()
    bigs = []

    Q.appendleft(root)

    while len(Q) != 0:
        big = 0
        for _ in range(len(Q)):
            cur = Q.pop()
            V.append(cur)
            if cur.data > big:
                big = cur.data
            for child in [cur.left, cur.right]:
                if child not in M and child != None:
                    Q.appendleft(child)
                    M.add(child)
        bigs.append(big)
    return bigs

def max_levels(lst):
    levels = 0
    for i in range(10):
        if len(lst) == 2**i - 1:
            levels = i + 1  # number of levels is not 0-indexed
            break


    root = Node(lst[0])
    root.left = Node(lst[1])
    root.right = Node(lst[2])
    root.left.left = Node(lst[3])
    root.left.right = Node(lst[4])
    # root.right.left = Node(lst[5]) (skipped to prevent problems)
    root.right.right = Node(lst[6])

    print(levelMax(root))

max_levels([5, 3, 8, 2, 4, 'null', 9])
