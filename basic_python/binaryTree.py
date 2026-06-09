class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

def preOrderTraversal(node):
  if node is None:
    return
  print(node.val, end=", ")
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)
  
def inorderTraversal(node):
    if node is None:
        return
    inorderTraversal(node.left)
    print(node.val, end=", ")
    inorderTraversal(node.left)

def postOrderTraversal(node):
  if node is None:
    return
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)
  print(node.val, end=", ")
  
      
print("Preorder Traversal")  
preOrderTraversal(root)

print("Inorder Traversal")  
inorderTraversal(root)


print("Postorder Traversal")  
postOrderTraversal(root)


# Test
# print("root.right.left.val:", root.right.left.val)
