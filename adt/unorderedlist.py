#!/usr/bin/env python
# -*- coding: utf-8 -*-
# single list
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        current = self.head
        strRet = "Item in List is "
        while current != None:
            strRet = strRet + str(current.getData()) + ","
            current = current.getNext()
        return strRet
    __repr__ = __str__

    #add at head
    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def append(self, data):
        temp = Node(data)
        temp.setNext(None)
        current = self.head
        prev = None
        while current != None:
            prev = current
            current = current.getNext()
        
        if prev == None: # empty list, append first item
            self.head = temp
        else:
            prev.setNext(temp)

        
    def size(self):
        current = self.head
        count = 0

        while current != None:
            current = current.getNext()
            count = count + 1

        return count

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()

        return False

    def remove(self, item):
        curr = self.head
        prev = None
        found = False
        while curr != None:
            if curr.getData() == item:
                found = True
                break
            prev = curr
            curr = curr.getNext()
        #special deal with head item    
        if found == True:
            if prev == None:
                self.head = curr.getNext()
            else:                
                prev.setNext(curr.getNext())

if __name__ == "__main__":
    myList = UnorderedList()
    myList.add(10)
    myList.add(100)
    myList.add(150)
    print myList
    print myList.search(120)
    print myList.search(150)
    myList.remove(100)
    print myList
    myList.remove(150)
    print myList
    #myList.remove(100)
    print myList
