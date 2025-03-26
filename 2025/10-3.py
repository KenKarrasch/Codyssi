import heapq

f = [[int(l) for l in k.split()] for k in open('25-10-1.txt').read().split('\n')]

cols = []
rows = []
for i in range(len(f)):
    col = 0
    row = 0
    for j in range(len(f[0])):
        #print(f[i][j])
        col += int(f[i][j])
        row += int(f[j][i])
    cols.append(col)
    rows.append(row)
print(min([min(cols),min(rows)]))


def shortest_path_in_grid(grid, start, end):

    start = (start[0]-1, start[1]-1)
    end = (end[0]-1, end[1]-1)
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Directions: up, down, left, right
    #directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    directions = [(1, 0), (0, 1)]
    
    # Priority queue: (total_cost, row, col)
    heap = []
    heapq.heappush(heap, (grid[start[0]][start[1]], start[0], start[1]))
    
    # To keep track of visited cells and their minimum cost
    cost_so_far = {start: grid[start[0]][start[1]]}
    
    # To reconstruct the path
    came_from = {start: None}
    
    while heap:
        current_cost, r, c = heapq.heappop(heap)
        
        # Check if we've reached the destination
        if (r, c) == end:
            break
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = current_cost + grid[nr][nc]
                if (nr, nc) not in cost_so_far or new_cost < cost_so_far[(nr, nc)]:
                    cost_so_far[(nr, nc)] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
                    came_from[(nr, nc)] = (r, c)
    
    # Reconstruct path if we found one
    if end not in came_from:
        return (float('inf'), [])  # No path found
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append((current[0]+1, current[1]+1))  # Convert back to 1-based
        current = came_from[current]
    path.reverse()
    
    return (cost_so_far.get(end, float('inf')), path)

# Example usage:

    # Create a sample 20x20 grid (replace with your actual data)
grid = f

# Find path from (1,1) to (15,15)
total_cost, path = shortest_path_in_grid(grid, (1, 1), (len(f), len(f)))

print(f"Total cost: {total_cost}")
print(f"Path length: {len(path)}")
print(f"Path: {path}")
