import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Queens Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (255, 0, 0)  # Red for invalid placements

# Board Settings
N = 8  # 8x8 board for N-Queens
SQUARE_SIZE = WIDTH // N
QUEENS = []  # List to store queens' positions (row, col)

# Load Queen Image
queen_image = pygame.image.load('queen.png')  # You need to download a queen image and name it 'queen.png'
queen_image = pygame.transform.scale(queen_image, (SQUARE_SIZE, SQUARE_SIZE))

# Game Settings
LEVEL = 2  # Level 1: 1 queen, Level 2: 2 queens, Level 3: 3 queens, etc.
TIMER_DURATION = 60  # Timer for 1 minute
start_time = None
time_left = TIMER_DURATION

# Function to draw the board
def draw_board():
    for row in range(N):
        for col in range(N):
            # Alternating colors for chessboard
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(SCREEN, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            # Draw grid lines
            pygame.draw.rect(SCREEN, (200, 200, 200), (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

# Function to check if placing a queen causes a conflict
def is_conflict(row, col):
    for q_row, q_col in QUEENS:
        # Check if the queen is in the same row, column, or diagonal
        if q_col == col or q_row == row or abs(q_row - row) == abs(q_col - col):
            return True
    return False

# Function to draw queens
def draw_queens():
    for row, col in QUEENS:
        SCREEN.blit(queen_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))  # Draw the queen at the specified location

# Function to highlight invalid placements
def highlight_invalid_placement(row, col):
    pygame.draw.rect(SCREEN, HIGHLIGHT_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

# Function to draw the timer
def draw_timer():
    font = pygame.font.SysFont(None, 36)
    timer_text = font.render(f"Time Left: {time_left}s", True, (255, 0, 0))
    SCREEN.blit(timer_text, (10, 10))

# Function to start the game timer
def start_game_timer():
    global start_time, time_left
    if start_time is None:
        start_time = time.time()  # Start the timer when the game begins

    # Calculate the time left
    elapsed_time = int(time.time() - start_time)
    time_left = max(TIMER_DURATION - elapsed_time, 0)

# Function to generate the initial level
def generate_level(level):
    QUEENS.clear()
    for _ in range(level):
        row = random.randint(0, N-1)
        col = random.randint(0, N-1)
        while is_conflict(row, col):
            row = random.randint(0, N-1)
            col = random.randint(0, N-1)
        QUEENS.append((row, col))

# Game loop
def main():
    running = True
    global start_time, time_left

    # Initialize the game
    generate_level(LEVEL)

    while running:
        SCREEN.fill((0, 0, 0))  # Fill screen with black
        draw_board()  # Draw the board
        draw_queens()  # Draw the placed queens
        draw_timer()  # Draw the timer

        # Check for conflicts and highlight invalid placements
        for row, col in QUEENS:
            if is_conflict(row, col):
                highlight_invalid_placement(row, col)  # Highlight invalid placements

        # Start the game timer
        start_game_timer()

        # Check if the user clicked anywhere on the grid
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // SQUARE_SIZE
                row = mouse_y // SQUARE_SIZE

                # Toggle queen placement
                if (row, col) in QUEENS:
                    QUEENS.remove((row, col))  # Remove queen if already placed
                else:
                    if not is_conflict(row, col):
                        QUEENS.append((row, col))  # Place queen if no conflict

        # Display the "win" message if all queens are placed correctly
        if len(QUEENS) == N and all(not is_conflict(row, col) for row, col in QUEENS):
            font = pygame.font.SysFont(None, 48)
            text = font.render("You Win!", True, (0, 255, 0))  # Green text
            SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        # Display the "game over" message if the time runs out
        if time_left == 0 and len(QUEENS) != N:
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over!", True, (255, 0, 0))  # Red text
            SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
