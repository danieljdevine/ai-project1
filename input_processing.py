import matplotlib.pyplot as plt
import networkx as nx

class Vertex:
    def __init__(self, name:str, neighbors=None):
        self.name = name
        if neighbors:
            self.neighbors = neighbors
        else:
            self.neighbors = []
    
    def add_neighbor(self, neighbor:tuple):
        self.neighbors.append(neighbor)

    def __str__(self):
        return f"{self.name}: {[n[0].name for n in self.neighbors]}"


class Edge:
    def __init__(self, start:str, end:str, weight:float):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return f"[{self.start}]---{self.weight}-->[{self.end}]"


class Graph:
    def __init__(self, vertices:list=[], edges:list=[]):
        self.vertices = {v.name: v for v in vertices}
        self.edges = edges
    
    def add_vertex(self, vertex_name:str):
        if vertex_name not in self.vertices.keys():
            new_vertex = Vertex(vertex_name)
            self.vertices[vertex_name] = new_vertex
    
    def add_edge(self, start_name:str, end_name:str, weight:str):
        self.add_vertex(start_name)
        self.add_vertex(end_name)

        new_edge = Edge(start_name, end_name, weight)
        self.edges.append(new_edge)

    def find_edge(self, start_name, end_name):
        for e in self.edges:
            if e.start == start_name and e.end == end_name:
                return e
        return None

    def update_node_neighbors(self):
        for edge in self.edges:
            n1 = self.vertices.get(edge.start)
            n2 = self.vertices.get(edge.end)

            n1.add_neighbor((n2, edge.weight))

    def visualize(self):
        G = nx.Graph()

        for e in self.edges:
            G.add_edge(e.start, e.end, weight=e.weight)

        pos = nx.spring_layout(G)

        nx.draw_networkx_nodes(G, pos, node_size=100)
        nx.draw_networkx_edges(G, pos, width=1)

        pos_higher = {}
        for k, v in pos.items():
            pos_higher[k] = (v[0], v[1]+0.02)
        nx.draw_networkx_labels(G, pos_higher, font_size=10, font_family='sans-serif')

        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis('off')
        plt.tight_layout()
        plt.show()


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
        
        self.graph.update_node_neighbors()

    def process_line(self, line:str):
        edge = line.split(' ')
        if len(edge) < 3:
            return -1
        try:
            distance = float(edge[2])
        except:
            return -1

        self.graph.add_edge(edge[0], edge[1], distance)
        self.graph.add_edge(edge[1], edge[0], distance)
        return 0


if __name__=='__main__':
    processor = InputProcessor()
    processor.process_file('inputs/input1.txt')
    processor.graph.visualize()
