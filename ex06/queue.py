from node import Node

class Queue:
    def __init__(self):
        self.f = None
        self.r = None
        self.s = 0

    def isEmpty(self):
        if self.f == None:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.f == None:
            self.f = Node(data)
            self.r = self.f
        else:
            self.r = Node(data, self.r)
        self.s = self.s + 1

    def dequeue(self):
        if self.f == None:
            pass
        elif self.f == self.r:
            self.f = None
            self.r = None
        else:
            tempNode = self.r
            while tempNode.next != self.f:
                tempNode = tempNode.next
            self.f = tempNode
            self.f.next = None
        self.s = self.s - 1

    def front(self):
        return self.f

    def size(self):
        return self.s

    def __str__(self):
        tempString = ""
        tempNode = self.r
        while tempNode != None:
            tempString = tempString + str(tempNode.data) + " "
            tempNode = tempNode.next
        return tempString
