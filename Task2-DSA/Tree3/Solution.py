def postOrder(root):
    #Write your code here
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info,end=" ")