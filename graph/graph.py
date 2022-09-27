import numpy as np, networkx as nx, matplotlib.pyplot as plt 


class graph:
    def __init__(self):
        self.graph = dict()
    def add(self,node:str,connections:list):
        if node not in self.graph.keys(): self.graph[node] = connections
        for con in connections: 
            if con not in self.graph.keys(): self.graph[con] = [] 
        else:
            for con in connections:
                if con not in self.graph[node]: 
                    self.graph[node].append(con)
        return
    
    def get_matrix(self):
        elements = sorted(self.graph.keys())
        cols = rows = len(elements)
        adj_matrix = [[0 for x in range(rows)] for y in range(cols)]
        edges_list = []
        for k in elements:
            for conections in self.graph[k]:
                edges_list.append((k,conections))
        for edge in edges_list:
            index_1 = elements.index(edge[0])
            index_2 = elements.index(edge[1])
            adj_matrix[index_1][index_2] = 1
        return np.array(adj_matrix)
    
    def get_as_dict(self):return self.graph

    def visualize(self, dir =True):
        if dir == True: g = nx.DiGraph(self.graph)
        else: g = nx.Graph(self.graph)
        nx.draw_networkx(g)
        plt.show()
        plt.savefig('graph.png', format = 'PNG')

    def BFS_traversal(self):
        traversal = [] 
        for k in self.graph.keys():
            if k not in traversal: traversal.append(k)
            for v in self.graph[k]: 
                if v not in traversal: traversal.append(v)
        return traversal



g = graph()
g.add('A', ['B'])
g.add('B', ['D', 'E'])
g.add('D', ['C'])
g.add('C', ['E'])

print(g.get_as_dict())
print(g.get_matrix())
print(g.BFS_traversal())
g.visualize()