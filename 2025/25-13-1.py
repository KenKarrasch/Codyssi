
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
            graph[source][dest] = 1 #weight
            
            # Ensure all nodes are in the graph (even if they have no outgoing edges)
            if dest not in graph:
                graph[dest] = {}
    
    return graph


def dijkstra(graph, start):
    # Initialize distances: start node is 0, others are infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue: (distance, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if we've already found a better path
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

txt = []
for i in f:
    txt.append(i)

graph = parse_graph(f)

shortest_paths = dijkstra(graph, 'STT')

cl = []

for node, distance in shortest_paths.items():
    cl.append(distance)
    if distance != float('infinity'):
        print(f"STT -> {node}: {distance}")
    else:
        print(f"STT -> {node}: No path exists")
cl.sort()
print(cl[-3] * cl[-2] * cl[-1])
