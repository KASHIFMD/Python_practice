class QUEUE:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, val):
        self.queue.append(val)
        
    def isEmpty(self):
        return len(self.queue)==0
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
        
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        return "Queue is empty"
        
    def size(self):
        return len(self.queue)
        
myQueue = QUEUE()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())