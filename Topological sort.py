from collections import defaultdict

def perform_topological_sort(directed_graph):
    
    explored = set()
    
    result_stack = []

   
    def dfs_visit(node):
        if node not in explored:
            explored.add(node)
            
            for adjacent in directed_graph[node]:
                dfs_visit(adjacent)
            
            result_stack.append(node)

    
    for vertex in directed_graph:
        dfs_visit(vertex)

    
    return result_stack[::-1]


# Example 1: Clothing dependency graph
clothing_graph = {
    "underwear": ["trousers", "footwear"],
    "trousers": ["belt", "footwear"],
    "belt": ["coat"],
    "shirt": ["necktie", "belt"],
    "necktie": ["coat"],
    "coat": [],
    "socks": ["footwear"],
    "footwear": [],
    "accessory": []
}


clothing_order = perform_topological_sort(clothing_graph)

# Example 2: Custom dependency graph
dependency_graph = {
    "X": ["Z"],
    "Y": ["Z", "W"],
    "Z": ["V"],
    "W": ["U"],
    "V": ["T"],
    "U": ["T"],
    "M": ["X", "Y"],
    "T": []
}


dependency_order = perform_topological_sort(dependency_graph)

# Print the results
print("Topological Sort for Clothing Graph:", clothing_order)
print("\nTopological Sort for Custom Graph:", dependency_order)

# Expected Results:
# Topological Sort for Clothing Graph: ['accessory', 'socks', 'shirt', 'necktie', 'underwear', 'trousers', 'footwear', 'belt', 'coat']
# Topological Sort for Custom Graph: ['M', 'Y', 'W', 'U', 'X', 'Z', 'V', 'T']
