#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque
import sys
import getopt
     
def bfs_search(graph, root, visit_fn):
    search_queue = deque()
    search_queue += graph[root]
    searched = []

    while search_queue:
        item = search_queue.popleft()
        print item
        if item not in searched:
            if visit_fn(item):
                print item + " is wanted,bingo!"
                return True
            else:
                 search_queue += graph[item]
                 searched.append(item)

    #found nothing
    return False

def visit(item):
    if item[-1] == 's':
        return True
    else:
        return False

if __name__ == "__main__":
    #constructed a graph
    # you->alice->mike
   #             ->nohe
   #      ->bob->vivi
   #      ->john->steve
   #             ->googles
    #
    #
    #
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

    print bfs_search(graph, "you", visit)
