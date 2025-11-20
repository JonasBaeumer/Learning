class MyCircularQueue:

    def __init__(self, k: int):
        # Need to create out internal DS (list) with size k
        # Initialize our pointers
        self.queue = [0] * k
        self.size = k
        self.front = -1
        self.rear = -1
        

    def enQueue(self, value: int) -> bool:
        # Check if queue is full or not 
        # If not full -> Move rear pointer ()
        # Insert element
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True
        
    def deQueue(self) -> bool:
        # Check if queue is empty 
        # If not -> Move the front pointer
        # Dont need to remove value here because we will just overwrite it when we need space on add
        if self.isEmpty():
            return False
        
        # If last element -> Yes, set the pointers to -1
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            return True
        
        self.front = (self.front + 1) % self.size
        return True
        

    def Front(self) -> int:
        # If empty -> return -1
        # Else return element at front pointer
        if self.front == -1:
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        # If full -> return -1 
        # Return rear pointer element
        if self.rear == -1:
            return -1 
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        # Check if front pointer -1
        return self.front == -1
        

    def isFull(self) -> bool:
        # If rear pointer right next to front pointer
        return (self.rear + 1) % self.size == self.front
