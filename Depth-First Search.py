from collections import defaultdict

def depth_first_search_recursive(graph, start_node, visited_nodes=None):
    if visited_nodes is None:
        visited_nodes = set()
    visited_nodes.add(start_node)
    print(f"Visited: {start_node}")
    for neighbor in graph[start_node]:
        if neighbor not in visited_nodes:
            depth_first_search_recursive(graph, neighbor, visited_nodes)
    return visited_nodes

def depth_first_search_iterative(graph, start_node):
    visited_nodes = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited_nodes:
            print(f"Visited: {current_node}")
            visited_nodes.add(current_node)
           
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited_nodes:
                    stack.append(neighbor)
    return visited_nodes

# Example 1: Road map graph
road_map = {
    'A': ['B', 'D'],
    'B': ['C'],
    'D': ['B'],
    'C': ['D'],
    'E': ['C', 'F'],
    'F': ['F']
}

# Example 2: Organizational hierarchy graph
hierarchy = {
    'CEO': ['CTO', 'CFO'],
    'CTO': ['Dev1', 'Dev2'],
    'CFO': ['Accountant1'],
    'Dev1': [],
    'Dev2': [],
    'Accountant1': []
}

print("Recursive DFS on Road Map Graph:")
visited_road_map_recursive = depth_first_search_recursive(road_map, 'A')
print()

print("Iterative DFS on Road Map Graph:")
visited_road_map_iterative = depth_first_search_iterative(road_map, 'A')
print()

print("Recursive DFS on Hierarchy Graph:")
visited_hierarchy_recursive = depth_first_search_recursive(hierarchy, 'CEO')
print()

print("Iterative DFS on Hierarchy Graph:")
visited_hierarchy_iterative = depth_first_search_iterative(hierarchy, 'CEO')
print()

# Expected results:
# Recursive DFS on Road Map Graph:
# Visited: A
# Visited: B
# Visited: C
# Visited: D

# Iterative DFS on Road Map Graph:
# Visited: A
# Visited: B
# Visited: C
# Visited: D

# Recursive DFS on Hierarchy Graph:
# Visited: CEO
# Visited: CTO
# Visited: Dev1
# Visited: Dev2
# Visited: CFO
# Visited: Accountant1

# Iterative DFS on Hierarchy Graph:
# Visited: CEO
# Visited: CTO
# Visited: Dev1
# Visited: Dev2
# Visited: CFO
# Visited: Accountant1
