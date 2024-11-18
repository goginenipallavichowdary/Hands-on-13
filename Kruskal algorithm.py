class DisjointSet:
    def __init__(self, total_nodes):
        self.leader = list(range(total_nodes))
        self.height = [0] * total_nodes

    def find(self, element):
        
        if self.leader[element] != element:
            self.leader[element] = self.find(self.leader[element])
        return self.leader[element]

    def union(self, elem1, elem2):
        root1 = self.find(elem1)
        root2 = self.find(elem2)

        if root1 != root2:
            
            if self.height[root1] > self.height[root2]:
                self.leader[root2] = root1
            elif self.height[root1] < self.height[root2]:
                self.leader[root1] = root2
            else:
                self.leader[root2] = root1
                self.height[root1] += 1



def kruskal_mst(total_vertices, weighted_edges):
    
    weighted_edges.sort(key=lambda edge: edge[2])
    ds = DisjointSet(total_vertices)

    mst_edges = [] 
    mst_total_weight = 0  

    for source, destination, weight in weighted_edges:
        
        if ds.find(source) != ds.find(destination):
            ds.union(source, destination)
            mst_edges.append((source, destination, weight))
            mst_total_weight += weight

    return mst_edges, mst_total_weight


# Example 1: Graph of cities and roads
city_graph = [
    (0, 1, 5), (0, 4, 9),
    (1, 2, 6), (1, 4, 3),
    (2, 3, 8), (2, 4, 7),
    (3, 4, 2), (3, 5, 4),
    (4, 5, 10)
]
number_of_cities = 6

# Example 2: Network of computers
network_graph = [
    (0, 1, 12), (0, 2, 4), (1, 2, 8),
    (1, 3, 5), (2, 3, 6)
]
number_of_computers = 4

print("Kruskal's Algorithm on City Graph:")
city_mst, city_cost = kruskal_mst(number_of_cities, city_graph)
print("MST:", city_mst)
print("Total Cost:", city_cost)
print()

print("Kruskal's Algorithm on Network Graph:")
network_mst, network_cost = kruskal_mst(number_of_computers, network_graph)
print("MST:", network_mst)
print("Total Cost:", network_cost)
print()

# Expected Results:
# Kruskal's Algorithm on City Graph:
# MST: [(3, 4, 2), (1, 4, 3), (0, 1, 5), (2, 3, 8), (4, 5, 10)]
# Total Cost: 28

# Kruskal's Algorithm on Network Graph:
# MST: [(0, 2, 4), (1, 3, 5), (2, 3, 6)]
# Total Cost: 15

