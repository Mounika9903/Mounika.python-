class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None  
 
 
def insertIntoBST(root, ele):
    if root == None:
        newBlock = TreeNode(ele)
        return newBlock 
 
    if root.data < ele:
        root.right = insertIntoBST(root.right, ele)
    else:
        root.left = insertIntoBST(root.left, ele)
    return root
 
def printInorderTraversal(root):
    if root == None:
        return 
 
    printInorderTraversal(root.left)
    print(root.data, end = " ")
    printInorderTraversal(root.right)
def searchInBST(root,target):
    if root==None:
        return False
    elif root.data==target:
        return True
    elif root.data<target:
        return searchInBST(root.right,target) 
    return searchInBST(root.left,target)            
 
 
nums = [18, 10, 25, 8, 15, 22, 28]

root = None 
for ele in nums:
    root = insertIntoBST(root, ele)
target1=250
if searchInBST(root,target1)==True:
    print(target1,"Found")
else:
    print(target1,"Not Found" )       
 

