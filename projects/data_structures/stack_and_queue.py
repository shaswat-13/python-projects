class Stack:
    data = list()

    # check if the stack is empty or not
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False
    
    # give the size of the stack
    def size(self):
        return len(self.data)
    
    # peek the top element of the stack
    def peek(self):
        if self.isEmpty():
            return None
        return self.data[-1]
    
    # push element to the top of stack
    def push(self, num):
        self.data.append(num)
    
    # pop element from the top of stack
    def pop(self):
        if self.isEmpty():
            return None
        last_element = self.data[-1]
        self.data = self.data[:-1]
        return last_element
    
class Queue:
    data = list()

    # check if the queue is empty or not
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False

    # return the size of queue
    def size(self):
        return len(self.data)
    
    # peek at the first element of the queue
    def peek(self):
        if self.isEmpty():
            return None
        return self.data[0]
    
    # add an element to the queue
    def enqueue(self, num):
        self.data.append(num)
    
    # remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return None
        first_element = self.data[0]
        self.data = self.data[1:]
        return first_element
    
def main():
    # stack
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.data)  # [1, 2, 3]
    print(s.peek())  # 3
    print(s.pop())  # 3
    print(s.data)  # [1, 2]
    
    # queue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.data)  # [1, 2, 3]
    print(q.peek())  # 1
    print(q.dequeue())  # 1
    print(q.data)  # [2, 3]
if __name__ == "__main__":  
    main()