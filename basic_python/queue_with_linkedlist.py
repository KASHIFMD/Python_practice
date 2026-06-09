class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class QUEUE:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def enqueue(self, val):
        new_Node = Node(val)
        if not self.front:
            self.front = new_Node
            self.rear = new_Node
            self.size += 1
            return
        self.rear.next = new_Node
        self.rear = new_Node
        self.size += 1
        
    def isEmpty(self):
        return self.size==0
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        dequeue_val = self.front.val
        self.front = self.front.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return dequeue_val
        
    def peek(self):
        if not self.isEmpty():
            return self.front.val
        return "Queue is empty"
        
    def queue_size(self):
        return self.size
        
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
    print()

# Create a queue
myQueue = QUEUE()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", end="")
myQueue.printQueue()
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", end="")
myQueue.printQueue()
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.queue_size())
