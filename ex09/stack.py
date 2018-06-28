from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, data):
        if self.top == None:
            self.top = Node(data)
        else:
            self.top = Node(data, self.top)
        self.height = self.height + 1

    def pop(self):
        if self.top:
            tempNode = self.top
            self.top = self.top.next
            self.height = self.height - 1
            return tempNode
        else:
            return None

    def peek(self):
        return self.top

    def size(self):
        return self.height

    def __str__(self):
        tempString = ""
        tempNode = self.top
        while tempNode:
            tempString = tempString + str(tempNode.data) + " "
            tempNode = tempNode.next
        return tempString
