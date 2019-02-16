#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key        = key
        self.payload    = val
        self.left_child = left
        self.right_child = right
        self.parent     = parent
   
    def __str__(self):
        return 'TreeNode key is ' + str(self.key) + str(self.payload)

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child
    
    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        succ = None
        #1.
        if self.has_right_child():
            succ = self.right_child_find_min()
        else:
            if succ.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    # 
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.righ_child = self
        return succ

    def right_child_find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    ## 把这个节点分割出去
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        # first node
        if (self.root == None):
            self.root = TreeNode(key, val)
            self.size = 1
        else:
            self._put(self.root, key, val)

    def _put(self, cur, key, val):
        # decide left or right child
        child = None
        if cur.key < key:
            if cur.has_right_child():
                child = cur.right_child
                # recursive insert
                self._put(child, key, val)
            else:
                cur.right_child = TreeNode(key, val, None, None, cur)
                self.size = self.size + 1
        else:
            if cur.has_left_child():
                child = cur.left_child
                # recursive insert
                self._put(child, key, val)
            else:
                cur.left_child = TreeNode(key, val, None, None, cur)
                self.size = self.size + 1  

    def _get_impl(self, cur_node, key):
            node = None
            if not cur_node:
                return None
            elif cur_node.key == key:
                return cur_node
            elif cur_node.key > key:
                 node = self._get_impl(cur_node.left_child, key) 
                 return node
            else:
                node = self._get_impl(cur_node.right_child, key)
                return node

    def get(self, key):
        if self.root:
            result = self._get_impl(self.root, key)
            if result:
                return result.payload
            else:
                return None
        else:
            return None

    def __contains__(self, key):
        if self._get(self.root, key):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get_impl(self.root, key)
            if node_to_remove:
                self._delete_impl(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            #delete root
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def __delitem(self, key):
        self.delete(key)

    def _delete_impl(self, node):
       #1. node has no children
       if node.is_leaf():
           if node.is_left_child():
               node.parent.left_child = None
           else:
               node.parent.right_child = None
       #2. node has 2 children
       elif node.has_both_children():
           self._delete_node_with_2_children(node)
       #3. node has 1 children 
       else:
           self._delete_node_with_1_children(node)

    def _delete_node_with_1_children(self, node):
        #3.1
        if node.is_left_child():
            if node.has_left_child():
                node.left_child.parent = node.parent
                node.parent.left_child = node.left_child
            else:
                node.right_child.parent = node.parent
                node.parent.left_child = node.righ_child
         #3.2
        elif node.is_right_child():
            if node.has_left_child():
                node.left_child.parent = node.parent
                node.parent.right_child = node.left_child
            else:
                node.right_child.parent = node.parent
                node.parent.right_child = node.right_child
         #3.3 root
        else:
            if node.has_left_child():
                node.replace_node_data(node.left_child.key, 
                                       node.left_child.payload,
                                       node.left_child.left_child,
                                       node.left_child.right_child)
            else:
                node.replace_node_data(node.right_child.key,
                                       node.right_child.payload,
                                       node.right_child.left_child,
                                       node.right_child.right_child)


    def _delete_node_with_2_children(self, node):
        succ = node.find_successor()
        succ.splice_out()
        node.key = succ.key
        node.payload = succ.payload

#test function
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put(6, "root")
    bst.put(4, "lv1_l")
    bst.put(8, "lv1_r")

    bst.put(3, "lv2_l_l")
    bst.put(5, "lv2_1_r")

    bst.put(7, "lv2_r_l")
    bst.put(9, "lv2_r_r")

    treeNode = bst.get(6)
    print treeNode
    bst.delete(8)
