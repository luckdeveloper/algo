#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from adt.binary_tree import * 
from adt.stack import *

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
     
    eTree = BinaryTree("")
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft("")
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)


from os import sys, path
if __name__ == "__main__":
    buildParseTree("((10+5)*3)")

