#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# min heap
class BinaryHeap:
    # heapList[0] is not used, to keep calc easy
    def __init__(self):
        self.currentSize = 0
        self.heapList = []

    def __str__(self):
        strRet = "BinaryHeap is "
        for i in range(len(self.heapList)):
            strRet = strRet + " " + str(self.heapList[i])
        return strRet
    __repr__ = __str__

    def percUp(self, i):
        #parent is i // 2
        while i // 2 > 0:
            parent = i // 2
            if self.heapList[i] < self.heapList[parent]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[parent]
                self.heapList[parent] = temp
            i = parent

    def insert(self, k):
        self.heapList.append(k)
        self.percUp(self.currentSize)
        self.currentSize = self.currentSize + 1

    def percDown(self, i):
        #child is i*2 or i*2+1
        while i*2 <= self.currentSize: 
            minChild = self.minChild(i)
            if self.heapList[i] > self.heapList[minChild]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[minChild]
                self.heapList[minChild] = temp
            i = minChild

    def delMin(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.percDown(1)
        return retVal

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

if __name__ == "__main__":
    heap = BinaryHeap()
    heap.insert(9)
    heap.insert(8)
    heap.insert(7)
    heap.insert(6)
    heap.insert(5)
    heap.insert(4)
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    print(heap)
