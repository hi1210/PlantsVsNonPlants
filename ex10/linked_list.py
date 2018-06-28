from linked_list_node import Node

class LinkedList(object):
    def __init__(self):
        self.h = None

    def __iter__(self):
        #in this context, head will be a Node
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def head(self):
        return self.h

    @head.setter
    def head(self, val):
        self.h = val

    def isEmpty(self):
        return self.head == None

    def add_head(self, node):
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    #prints a list item by item
    def print_list(list_head):
        print("trying to print")
        while list_head:
            print(list_head.content)
            list_head = list_head.next

    #adds an item to the end of a linked list
    def add_tail(list_head, val):
        if list_head == None:
            return
        while list_head.next:
            list_head = list_head.next
        list_head.next = Node(val)

    #removes an item from a list while keeping the list intact
    def remove(self, list_head, val):
        previous = None
        #if no list, ignore
        if list_head == None:
            return

        while list_head != None:
            if list_head.content == val:
                if previous == None:
                    self.h = list_head.next
                    list_head = self.h
                else:
                    previous.next = list_head.next
                    list_head = list_head.next
            else:
                previous = list_head
                list_head = list_head.next

    #check if a linked list is circular
    def has_cycle(list_head):
        if list_head == None:
            return False
        lastNode = list_head
        while lastNode.next != None:
            if lastNode.next == list_head:
                return True
            lastNode = lastNode.next
        return False

    #merge two descending weight trains into one
    def merge(train1, train2):
        #create a node that other carriages can be added to
        trainAnchor = Node("start")
        #create a variable that will keep track of the last value of the new train
        trainMerger = trainAnchor
        #until one of the trains is empty, look at both, and put the larger one onto the anchor
        while train1 != None and train2 != None:
            if train1.content > train2.content:
                trainMerger.next = train1
                trainMerger = trainMerger.next
                train1 = train1.next
            else:
                trainMerger.next = train2
                trainMerger = trainMerger.next
                train2 = train2.next
        #Once one of the trains is empty, attach the remaining nodes to the merger
        if train1 == None:
                trainMerger.next = train2
        elif train2 == None:
                trainMerger.next = train1
        #cut off last two carriages
        thirdToLast = trainAnchor
        last = trainAnchor.next.next
        while last.next:
            last = last.next
            thirdToLast = thirdToLast.next
        thirdToLast.next = None
        #grab the node after anchor
        return trainAnchor.next

    def sort_asc(self, list_head):
        newListNode = Node("PreList")
        newListNodeHead = newListNode
        if list_head == None or list_head.next == None:
            return
        preSmallestNode = None
        previousNode = None
        smallestNode = list_head
        readerNode = list_head
        debugLimiter = 0
        while True:
            if readerNode == None:
                if self.isEmpty():
                    break;
                newListNode.next = smallestNode
                newListNode = newListNode.next
                if preSmallestNode:
                    preSmallestNode.next = smallestNode.next
                else:
                    self.h = smallestNode.next
                readerNode = self.h
                smallestNode = self.h
                previousNode = None
                preSmallestNode = None
            elif readerNode.content < smallestNode.content:
                preSmallestNode = previousNode
                smallestNode = readerNode
            if readerNode:
                previousNode = readerNode
                readerNode = readerNode.next
        self.h = newListNodeHead.next

    def sort_dsc(self, list_head):
        #SHA256 hash of "PreList"
        newListNode = Node("PreList")
        newListNodeHead = newListNode
        if list_head == None or list_head.next == None:
            return
        preLargestNode = None
        previousNode = None
        largestNode = list_head
        readerNode = list_head
        debugLimiter = 0
        while True:
            if readerNode == None:
                if self.isEmpty():
                    break;
                newListNode.next = largestNode
                newListNode = newListNode.next
                if preLargestNode:
                    preLargestNode.next = largestNode.next
                else:
                    self.h = largestNode.next
                readerNode = self.h
                largestNode = self.h
                previousNode = None
                preLargestNode = None
            elif readerNode.content > largestNode.content:
                preLargestNode = previousNode
                largestNode = readerNode
            if readerNode:
                previousNode = readerNode
                readerNode = readerNode.next
        self.h = newListNodeHead.next
'''
        while True:
            if readerNode == None:
                if lastSortedNode.next == None and lastSortedNode.content != "A5633A211DF54CEA1BF31F169BACB44465BEEF4414B32B0E5A55EE928A33A29B":
                    break
                elif lastSortedNode.content != "A5633A211DF54CEA1BF31F169BACB44465BEEF4414B32B0E5A55EE928A33A29B":
                    smallestNode.next = lastSortedNode.next.next
                    lastSortedNode.next = smallestNode
                    lastSortedNode = lastSortedNode.next
                else:
                    smallestNode.next = self.h.next
                    self.h = smallestNode
                    lastSortedNode = smallestNode
                readerNode = lastSortedNode.next
                smallestNode = readerNode
            elif readerNode.content < smallestNode.content:
                smallestNode = readerNode
            if readerNode:
                readerNode = readerNode.next
'''


'''
    def check_asc(list_head):
        if list_head == None or list_head.next = None:
            return True
        while list_head.next and list_head.content < list_head.next.content:
            list_head = list_head.next
        if list_head.next:
            return False
        else:
            return True
'''
