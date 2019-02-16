#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import deque
import sys
import getopt
import traceback

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node  in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# global var use by two function
processed = []        
  
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        #1, constructed a graph
        graph = {}
        graph["start"] = {}

        graph["start"]["a"] = 6
        graph["start"]["b"] =2 

        graph["a"] = {}
        graph["a"]["fin"] = 1

        graph["b"] = {}
        graph["b"]["a"] = 3
        graph["b"]["fin"] = 5

        graph["fin"]= {}

        #2. cost, 从起点到节点花费
        infinity = float("inf")
        costs = {}
        costs["a"] = 6
        costs["b"] = 2
        costs["fin"] = infinity

        #3.parent，查找路径
        parents = {}
        parents["start"] = None
        parents["a"] = "start"
        parents["b"] = "start"
        parents["fin"] = None

        lowest_cost_node = None

        # main 
        node = find_lowest_cost_node(costs)
        while node is not None:
            cost = costs[node]
            neighbors = graph[node]
            for n  in neighbors.keys():
                new_cost = cost + neighbors[n]
                if new_cost < costs[n]: #经过当前节点到前往该邻居更近
                    costs[n] = new_cost
                    parents[n] = node
                    lowest_cost_node = node
            processed.append(node)
            node = find_lowest_cost_node(costs)

        #print lowest path
        node = parents["fin"]
        while node is not None:
            print node
            node = parents[node]


    except Exception, err:
        print err.message
        traceback.print_exc()

if __name__ == "__main__":
    main()


