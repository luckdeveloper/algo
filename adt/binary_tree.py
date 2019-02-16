#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    #insert from root    
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else: #downgrade orginal leftChild
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        return self.leftChild
    
    #insert from root
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else: #downgrade orginal leftChild
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
        return self.rightChild

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def preorderVisit(tree, visit_fn):
    if tree:
        visit_fn(tree.getRootVal())
        preorderVisit(tree.getLeftChild(), visit_fn)
        preorderVisit(tree.getRightChild(), visit_fn)
                      
def inorderVisit(tree, visit_fn):
    if tree:
        inorderVisit(tree.getLeftChild(), visit_fn)
        visit_fn(tree.getRootVal())
        inorderVisit(tree.getRightChild(), visit_fn)

def postorderVisit(tree, visit_fn):
    if tree:
        postorderVisit(tree.getLeftChild(), visit_fn)
        postorderVisit(tree.getRightChild(), visit_fn)
        visit_fn(tree.getRootVal())

def visit(aVal):
    print aVal

if __name__ == "__main__":
    r = BinaryTree('root')
    l1 = r.insertLeft("l1")
    r1 = r.insertRight("r1")
    l1l2 = l1.insertLeft("l1l2")
    l1r2 = l1.insertRight("l1r2")
    r1l2 = r1.insertLeft('r1l2')
    r1r2 = r1.insertRight('r1r2')
    
    print("preorder: ")
    preorderVisit(r, visit)
    print("inorder: ")
    inorderVisit(r, visit)
    print("postorder: ")
    postorderVisit(r, visit)

