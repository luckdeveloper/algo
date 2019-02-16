#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


###########################################
#### palcheck
def pal_checker(aString):
    char_deque = Deque()
    for ch in aString:
        char_deque.addRear(ch)

    equal = True
    while char_deque.size() > 1:
        front = char_deque.removeFront()
        rear = char_deque.removeRear()
        if front != rear:
            equal = False
            break

    return equal

if __name__ == "__main__":
    testString = "abcdedcba"
    print testString, "is pal: ", pal_checker(testString)

    testString = "abcdedcbaa"
    print testString, "is pal: ", pal_checker(testString)

        
    

        
