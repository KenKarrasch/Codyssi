
import heapq

f = open('25-13-1.txt').read()

def parse_graph(text):
    graph = {}
    lines = text.strip().split('\n')
    
    for line in lines:
        if '->' in line and '|' in line:
            # Split into parts: "source -> dest | weight"
            parts = line.split('->')
            source = parts[0].strip()
            rest = parts[1].split('|')
            dest = rest[0].strip()
            weight = int(rest[1].strip())
            
            # Add the edge to the graph
            if source not in graph:
                graph[source] = {}
            graph[source][dest] = weight
            
            # Ensure all nodes are in the graph (even if they have no outgoing edges)
            if dest not in graph:
                graph[dest] = {}
    
    return graph

def find_longest_circular_path(graph):
    max_length = 0
    best_path = []

    def backtrack(current_node, start_node, path, current_length):
        nonlocal max_length, best_path

        # Check if we've returned to the start node forming a cycle
        if current_node == start_node and len(path) > 1:
            if current_length > max_length:
                max_length = current_length
                best_path = path.copy()
            return

        # Explore all neighbors
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in path or (neighbor == start_node and len(path) > 1):
                path.append(neighbor)
                backtrack(neighbor, start_node, path, current_length + weight)
                path.pop()  # Backtrack

    # Iterate over each node as the potential start of the cycle
    for start_node in graph:
        backtrack(start_node, start_node, [start_node], 0)

    if max_length == 0:
        return "No circular path found."
    else:
        return {
            "path": best_path,
            "length": max_length
        }
    

txt = []
for i in f:
    txt.append(i)

graph = parse_graph(f)

result = find_longest_circular_path(graph)
print(result)
