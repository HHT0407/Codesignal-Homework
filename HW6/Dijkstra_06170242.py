取用自 https://gist.github.com/econchick/4666413

from collections import defaultdict
import heapq
import math

  
class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]
                             for row in range(vertices)]
        self.dict = defaultdict(list)
        
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
    
    def Dijkstra(self, s):
        s = str(s)
        graph_dict = self.get_graph_dict()
        if not graph_dict:
            return

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path
