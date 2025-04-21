import random

# Directions for moving up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def generate_grid(N):
    """Generate a random N×N grid with obstacles (represented by 1) and free spaces (0)."""
    grid = [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]
    
    # Ensure the source and goal are free spaces
    grid[0][0] = 0  # Source is always at (0, 0)
    grid[N-1][N-1] = 0  # Goal is always at (N-1, N-1)
    
    return grid

def dfs(grid, start, goal):
    """Perform DFS to find a path from source to goal."""
    N = len(grid)
    stack = [start]
    parent = {start: None}  # To reconstruct the path
    visited = set()  # To keep track of visited nodes
    visited.add(start)
    topological_order = []  # To store nodes in the order they are visited

    while stack:
        current = stack.pop()
        topological_order.append(current)

        if current == goal:
            break

        for direction in DIRECTIONS:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < N and 0 <= neighbor[1] < N and grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    
    # Reconstruct the path from goal to source
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)  # Use .get() to avoid KeyError if node is not found
    path.reverse()

    # If the path does not include the start, return an empty path
    if path[0] != start:
        return [], topological_order

    return path, topological_order

def print_grid(grid, source, goal, path, topological_order):
    """Print the grid, source, goal, DFS path, and topological order of node traversal."""
    N = len(grid)
    
    print("Grid:")
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    
    print(f"\nSource: {source}")
    print(f"Goal: {goal}")
    
    print("\nDFS Path:")
    if path:
        for node in path:
            print(f"({node[0]}, {node[1]})", end=" -> ")
        print("Goal")
    else:
        print("No path found.")
    
    print("\nTopological Order of Node Traversal:")
    for node in topological_order:
        print(f"({node[0]}, {node[1]})", end=" -> ")
    print("End")

def main():
    # Randomly choose N between 4 and 7
    N = random.randint(4, 7)
    
    # Generate grid and define source and goal
    grid = generate_grid(N)
    source = (0, 0)
    goal = (N - 1, N - 1)

    # Perform DFS to find a path and topological order
    path, topological_order = dfs(grid, source, goal)

    # Print the results
    print_grid(grid, source, goal, path, topological_order)

if __name__ == "__main__":
    main()
