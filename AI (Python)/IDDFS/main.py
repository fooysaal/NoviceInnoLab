def is_valid_move(x, y, grid, visited):
    """ Check if the cell (x, y) is within bounds, is an empty space (0), and has not been visited. """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0 and not visited[x][y]

def dfs(x, y, target_x, target_y, grid, visited, path, depth, max_depth):
    """ Perform DFS with a given depth limit. """
    # If we've reached the target
    if (x, y) == (target_x, target_y):
        path.append((x, y))
        return True

    # If the depth exceeds the maximum allowed, stop searching.
    if depth == max_depth:
        return False

    # Mark the current cell as visited
    visited[x][y] = True
    path.append((x, y))

    # Explore all 4 possible directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y, grid, visited):
            if dfs(new_x, new_y, target_x, target_y, grid, visited, path, depth + 1, max_depth):
                return True

    # Backtrack: unmark the current cell and remove it from path
    visited[x][y] = False
    path.pop()
    return False

def iddfs(grid, start_x, start_y, target_x, target_y):
    """ Perform Iterative Deepening Depth First Search (IDDFS) to find a path. """
    max_depth = len(grid) * len(grid[0])  # The maximum possible depth
    for depth in range(max_depth + 1):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        path = []
        if dfs(start_x, start_y, target_x, target_y, grid, visited, path, 0, depth):
            print(f"Path found at depth {depth + 1} using IDDFS")
            print("Traversal Order:", path)
            return
    print(f"Path not found at max depth {max_depth} using IDDFS")

# Function to take grid input from the user
def get_input():
    # Read grid dimensions
    rows, cols = map(int, input("Enter the number of rows and columns: ").split())
    
    # Read the grid
    grid = []
    print("Enter the grid:")
    for i in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # Read the start and target positions
    start_x, start_y = map(int, input("Enter the start position (x y): ").split())
    target_x, target_y = map(int, input("Enter the target position (x y): ").split())
    
    return grid, start_x, start_y, target_x, target_y

# Main function to run the program
def main():
    grid, start_x, start_y, target_x, target_y = get_input()
    iddfs(grid, start_x, start_y, target_x, target_y)

if __name__ == "__main__":
    main()
