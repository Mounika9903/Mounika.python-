
 
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
 
# 1. objects creation (memory allocation) 
root = TreeNode(11)
# root:
# data = 15 
# left = None 
# right = None 
obj2 = TreeNode(7)
obj3 = TreeNode(5)
obj4 = TreeNode(3)
obj5 = TreeNode(9)
obj6 = TreeNode(8)
obj7 = TreeNode(10)
obj8 = TreeNode(15)
obj9 = TreeNode(13)
obj10= TreeNode(12)
obj11= TreeNode(14)
obj12= TreeNode(20)
obj13= TreeNode(18)
obj14= TreeNode(25)
 
#    18 
#   15  20 
# 25 30 45 80
 

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

printPostOrder(root) 

