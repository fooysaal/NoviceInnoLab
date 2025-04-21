import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Define constants
CELL_SIZE = 40
MAZE_WIDTH = 15
MAZE_HEIGHT = 15
WINDOW_WIDTH = MAZE_WIDTH * CELL_SIZE
WINDOW_HEIGHT = MAZE_HEIGHT * CELL_SIZE + 100  # Extra space for controls
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

# Define colors
colors = {
    "wall": BLACK,
    "path": WHITE,
    "start": GREEN,
    "end": RED,
    "solution": BLUE,
    "current": (255, 165, 0)  # Orange for the current step in path
}

# Function to check if a position is valid
def is_valid_move(maze, visited, row, col):
    return (0 <= row < len(maze)) and (0 <= col < len(maze[0])) and maze[row][col] == 0 and not visited[row][col]

# BFS function to find the shortest path
def bfs(maze, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    queue = deque([(start, [start])])
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    visited[start[0]][start[1]] = True
    
    while queue:
        (current_row, current_col), path = queue.popleft()
        
        if (current_row, current_col) == end:
            return path
        
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            if is_valid_move(maze, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    return None

# DFS function to find a path
def dfs(maze, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    stack = [(start, [start])]
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    visited[start[0]][start[1]] = True
    
    while stack:
        (current_row, current_col), path = stack.pop()
        
        if (current_row, current_col) == end:
            return path
        
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            if is_valid_move(maze, visited, new_row, new_col):
                visited[new_row][new_col] = True
                stack.append(((new_row, new_col), path + [(new_row, new_col)]))
    return None

# Function to draw the maze on the screen
def draw_maze(screen, maze, path=None, current_step=None):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = colors["wall"] if maze[row][col] == 1 else colors["path"]
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)  # Draw borders

    if path:
        # Show the current step
        if current_step:
            row, col = current_step
            pygame.draw.rect(screen, colors["current"], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Draw the full solution path after showing steps
        for (row, col) in path:
            pygame.draw.rect(screen, colors["solution"], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to generate a random maze
def generate_maze():
    maze = [[1 if random.random() < 0.3 else 0 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]
    maze[0][0] = 0  # Start
    maze[MAZE_HEIGHT-1][MAZE_WIDTH-1] = 0  # End
    return maze

# Function to get the cell under the mouse cursor
def get_cell_from_mouse(pos):
    x, y = pos
    return y // CELL_SIZE, x // CELL_SIZE

# Function to display buttons and messages
def draw_buttons_and_messages(screen, algorithm, message=""):
    font = pygame.font.SysFont("Arial", 18)
    
    # Draw Algorithm selection buttons
    pygame.draw.rect(screen, LIGHT_GRAY, (0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 100))  # Background for buttons
    pygame.draw.rect(screen, BLACK, (50, WINDOW_HEIGHT - 80, 100, 40))  # BFS button
    pygame.draw.rect(screen, BLACK, (200, WINDOW_HEIGHT - 80, 100, 40))  # DFS button
    pygame.draw.rect(screen, BLACK, (350, WINDOW_HEIGHT - 80, 100, 40))  # Start button
    pygame.draw.rect(screen, BLACK, (500, WINDOW_HEIGHT - 80, 100, 40))  # Reset button

    bfs_button_text = font.render("BFS", True, WHITE)
    dfs_button_text = font.render("DFS", True, WHITE)
    start_button_text = font.render("Start", True, WHITE)
    reset_button_text = font.render("Reset", True, WHITE)

    screen.blit(bfs_button_text, (75, WINDOW_HEIGHT - 70))
    screen.blit(dfs_button_text, (225, WINDOW_HEIGHT - 70))
    screen.blit(start_button_text, (375, WINDOW_HEIGHT - 70))
    screen.blit(reset_button_text, (525, WINDOW_HEIGHT - 70))
    
    # Display the selected algorithm
    algorithm_text = font.render(f"Algorithm: {algorithm}", True, WHITE)
    screen.blit(algorithm_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT - 30))
    
    # Display message (No path found, etc.)
    if message:
        message_font = pygame.font.SysFont("Arial", 22)
        message_text = message_font.render(message, True, YELLOW)
        screen.blit(message_text, (WINDOW_WIDTH // 2 - 120, 10))  # Display at the top of the screen

# Main function to run the game
def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Maze Solver")

    # Create a random maze
    maze = generate_maze()
    start = (0, 0)  # Top-left corner
    end = (MAZE_HEIGHT - 1, MAZE_WIDTH - 1)  # Bottom-right corner
    solving = False
    path = []
    algorithm = "BFS"  # Default algorithm
    message = ""  # Message to show no path found

    # Run the game loop
    running = True
    current_step_index = 0  # This will keep track of the current step index
    current_step = None
    while running:
        screen.fill(WHITE)
        draw_buttons_and_messages(screen, algorithm, message)  # Draw the control panel and messages

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_cell_from_mouse(event.pos)
                if event.button == 1:  # Left click to set start
                    start = (row, col)
                elif event.button == 3:  # Right click to set end
                    end = (row, col)
                # Check if buttons are clicked
                if 50 <= event.pos[0] <= 150 and WINDOW_HEIGHT - 80 <= event.pos[1] <= WINDOW_HEIGHT - 40:
                    algorithm = "BFS"  # Select BFS
                    message = ""  # Reset message
                elif 200 <= event.pos[0] <= 300 and WINDOW_HEIGHT - 80 <= event.pos[1] <= WINDOW_HEIGHT - 40:
                    algorithm = "DFS"  # Select DFS
                    message = ""  # Reset message
                elif 350 <= event.pos[0] <= 450 and WINDOW_HEIGHT - 80 <= event.pos[1] <= WINDOW_HEIGHT - 40:
                    solving = True
                    # Run selected algorithm
                    if algorithm == "BFS":
                        path = bfs(maze, start, end)
                    elif algorithm == "DFS":
                        path = dfs(maze, start, end)
                    if not path:
                        message = "No path available"  # If no path found
                elif 500 <= event.pos[0] <= 600 and WINDOW_HEIGHT - 80 <= event.pos[1] <= WINDOW_HEIGHT - 40:
                    # Reset maze
                    maze = generate_maze()
                    start = (0, 0)
                    end = (MAZE_HEIGHT - 1, MAZE_WIDTH - 1)
                    solving = False
                    path = []
                    current_step_index = 0
                    current_step = None
                    message = ""  # Reset message

        # Draw the maze and the solution path
        draw_maze(screen, maze, path, current_step)

        # Mark start and end
        pygame.draw.rect(screen, colors["start"], (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, colors["end"], (end[1] * CELL_SIZE, end[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Step through the path slowly if solving
        if solving and path:
            if current_step_index < len(path):
                current_step = path[current_step_index]
                current_step_index += 1
            pygame.time.delay(100)  # Delay between steps for visualization

        # Update the display
        pygame.display.flip()

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()