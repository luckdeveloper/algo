#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque
import sys
import getopt

def dfs_search_recursive(graph, root, visit_fn):
    search_queue = deque()
    search_queue += graph[root]
    searched = []

    while search_queue:
        item = search_queue.popleft()
        #debug print
        print item
        if item not in searched:
            if visit_fn(item):
                print item + "is wanted"
                return True
            else:
                dfs_search_recursive(graph, item, visit_fn)

    #found nothing
    return False

def dfs_search_iterative(graph, root, visit_fn):
    search_stack = [root]
    searched = []

    while search_stack:
        vertex = search_stack.pop()
        print vertex
        if vertex not in searched:
            if visit_fn(vertex):
                print vertex + " is wanted, bingo!"
                return True
            else:
                searched.append(vertex)
                for neighbor in graph[vertex]:
                    search_stack.append(neighbor)

    #found nothing
    return False

def visit(item):
    if item[-1] == 's':
        return True
    else:
        return False

if __name__ == "__main__":
    #constructed a graph
    graph = {}
    graph["you"] = ["alice", "bob", "john"]

    graph["alice"] = ["mike", "nohe"]
    graph["mike"] = []
    graph["nohe"] = []

    graph["bob"] = ["vivi"]
    graph["vivi"] = []

    graph["john"] = ["steve", "googles"]
    graph["steve"] = []
    graph["googles"] = []

    print dfs_search_iterative(graph, "you", visit)
