#!/usr/bin/env python3

import sys
from input_processing import Edge, InputProcessor


class PriorityQueue:
    def __init__(self, initial_state=[]):
        self._queue = initial_state
        if self._queue:
            self._order_queue()
    
    def _order_queue(self):
        self._queue.sort(key=lambda x: x.cost)

    def push(self, node):
        self._queue.append(node)
        self._order_queue()

    def pop(self):
        smallest_element = self._queue[0]
        self._queue = self._queue[1:]
        return smallest_element

    def clear(self):
        self._queue = []

    def empty(self):
        if self._queue:
            return False
        return True


class Node:
    def __init__(self, vertex_name, cost=0, depth=0, parent=None):
        self.vertex_name = vertex_name
        self.cost = cost
        self.depth = depth
        self.parent = parent


class UCIDAlgorithm:
    # Combine the concepts of uniform cost and iterative deepening for memory efficiency

    def __init__(self, graph, start, goal, max_depth=None):
        self.graph = graph
        self.fringe = PriorityQueue()
        self.path = None

        self.start = start
        self.goal = goal
        
        if max_depth:
            self.max_depth = max_depth
        else:
            self.max_depth = len(graph.vertices)

    def run_iterative_deepening(self):
        if self.start == self.goal:
            self.path = [Edge(self.start, self.goal, 0.)]
            return
        
        for depth_limit in range(self.max_depth):
            result = self.depth_limited_search(depth_limit)
            if result is not None:
                result.reverse()
                self.path = result
                return
        
        self.path = None

    def depth_limited_search(self, depth_limit):
        start_node = Node(self.start)
        self.fringe.push(start_node)

        while not self.fringe.empty():
            node = self.fringe.pop()

            if node.vertex_name == self.goal:
                return self.get_path(node)

            if node.depth > depth_limit:
                continue

            vertex = self.graph.vertices.get(node.vertex_name)
            if not vertex: continue
            
            names_added = []
            for neighbor, edge_weight in vertex.neighbors:
                new_node = Node(neighbor.name, cost=node.cost+edge_weight, depth=node.depth+1, parent=node)
                self.fringe.push(new_node)
                names_added.append(new_node.vertex_name)

        return None
    
    def get_path(self, node):
        path = []
        prev_node = node
        while node.parent is not None:
            node = node.parent
            
            edge = self.graph.find_edge(node.vertex_name, prev_node.vertex_name)
            if edge is None:
                print("INVALID PATH: " + node.vertex_name + "---->" + prev_node.vertex_name)
                return None
            path.append(edge)
            prev_node = node

        return path

    def print_output(self):
        if self.path is None:
            print("distance: infinity\nroute:\nnone")
        else:
            print(f"distance: {int(sum([e.weight for e in self.path]))} km")
            print("route:")
            for e in self.path:
                print(f"{e.start} to {e.end}, {int(e.weight)} km")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("INVALID AMOUNT OF ARGUMENTS")
    
    file_path = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]

    input_processor = InputProcessor()
    input_processor.process_file(file_path)
    graph = input_processor.graph

    algorithm = UCIDAlgorithm(graph, start, end)
    algorithm.run_iterative_deepening()
    algorithm.print_output()