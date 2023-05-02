
class Edge:
    def __init__(self, start:str, end:str, distance:float, directed:bool=False):
        self.start = start
        self.end = end
        self.distance = distance
        self.directed = directed

    def __str__(self):
        if self.directed:
            return f"[{self.start}]---{self.distance}-->[{self.end}]"
        else:
            return f"[{self.start}]---{self.distance}---[{self.end}]"

class Graph:
    def __init__(self, nodes:list=[], edges:list=[]):
        self.nodes = nodes
        self.edges = edges
    
    def add_node(self, node:str):
        if node not in self.nodes:
            self.nodes.append(node)
    
    def add_edge(self, edge:Edge):
        if edge.start not in self.nodes:
            self.nodes.append(edge.start)
        if edge.end not in self.nodes:
            self.nodes.append(edge.end)

        self.edges.append(edge)

class InputProcessor:
    def __init__(self):
        self.graph = Graph()

    def process_file(self, filepath:str):

        with open(filepath, 'r') as file:
            lines = file.readlines()
            lines = [l.replace('\n', '') for l in lines]

        for line in lines:
            if line == "END OF INPUT":
                break
            if self.process_line(line) == -1:
                print("Invalid file format. Unable to process file.")
                return

    def process_line(self, line:str):
        edge = line.split(' ')
        if len(edge) < 3:
            return -1
        try:
            distance = float(edge[2])
        except:
            return -1

        edge = Edge(edge[0], edge[1], distance)
        self.graph.add_edge(edge)
        return 0
