class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLinkedList(head):
    curr=head
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.next
    print()
def insertAtEndofTail(head,ele):
    newBlock=Node(ele)
    if head==None:
       return newBlock
    curr=head
    while curr.next!=None:
         curr=curr.next
    curr.next=newBlock
    return head   
l=[11,22,33,44,55,66,77,88,99,110]
head=None
for ele in l:
    head=insertAtEndofTail(head,ele)
printLinkedList(head)    

