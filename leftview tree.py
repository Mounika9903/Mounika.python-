class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
 
def printPreOrder(root):
    if root == None:
        return
 
    # root, left_subtree, right_subtree 
    print(root.data, end = " ")
    printPreOrder(root.left)
    printPreOrder(root.right)
 
def printInOrder(root):
    if root == None:
        return
 
    # left_subtree, root, right_subtree 
 
    printInOrder(root.left)
    print(root.data, end = " ")
    printInOrder(root.right) 
 
def printPostOrder(root):
    if root == None:
        return
 
    # left_subtree, right_subtree, root
 
    printPostOrder(root.left)
    printPostOrder(root.right) 
    print(root.data, end = " ")
 
 

 
def printLevelOrder(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            subResult.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
        result.append(subResult)
 
    #print(result)
    for subLevel in result:
        print(*subLevel)
 
def printZigZagLevelOrder(root):
    result = []
    Q = [root]
    level = 0 
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            subResult.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
        if level % 2 == 1:
            subResult = subResult[::-1]
 
        result.append(subResult)
        level += 1 
 
    #print(result)
    for subLevel in result:
        print(*subLevel) 
 
 
def leftViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
 
    print(*result)
 
 
root=TreeNode(11)
obj2 = TreeNode(7)
obj3 = TreeNode(5)
obj4 = TreeNode(3)
obj5 = TreeNode(9)
obj6 = TreeNode(8)
obj7 = TreeNode(10)
obj8 = TreeNode(15)
obj9 = TreeNode(13)
obj10 = TreeNode(12)
obj11 = TreeNode(14)
obj12 = TreeNode(20)
obj13 = TreeNode(18)
obj14 = TreeNode(25)

root.left = obj2 
root.right = obj8 
 
obj2.left = obj3 
obj2.right = obj5 
 
obj3.left = obj4 

obj2.left = obj3 
obj2.right = obj5 
 
obj5.left = obj6 
obj5.right = obj7 
 
obj8.left = obj9 
obj8.right = obj12 
 
obj9.left = obj10
obj9.right = obj11


obj12.left = obj13 
obj12.right = obj14



leftViewOfBinaryTree(root)
