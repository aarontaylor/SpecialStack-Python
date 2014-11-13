'''
Checks if a binary tree is a binary search tree
Uses the property of a BST being sorted in order to tell
Linear complexity O(n)
'''

previous = -1

def isBST(root):
    # Assumes all tree values are positive
    previous = -1
    return isBST_rec(root)

def isBST_rec(root):
    global previous

    if root == None:
        return True

    if isBST_rec(root.left) == False:
        return False

    if previous > root.data and previous != -1:
        return False

    previous = root.data

    if isBST_rec(root.right) == False:
        return False

    return True


