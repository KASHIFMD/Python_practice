class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, val):
        new_Node = Node(val)
        if self.head:
            new_Node.next = self.head
        self.head = new_Node
        self.size+=1
    
    def isEmpty(self):
        if self.size==0:
            return True
        return False
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        pop_node = self.head
        self.head = self.head.next
        self.size-=1
        return pop_node.val
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.val
    
    def stackSize(self):
        return self.size
        
    def traverseAndPrint(self):
        curr_node = self.head
        while curr_node:
            print(f"{curr_node.val}->", end="")
            curr_node = curr_node.next
        print()
            

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
        
        

    