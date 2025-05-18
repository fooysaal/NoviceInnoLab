import pygame
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Queens Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (255, 0, 0)

N = 8
SQUARE_SIZE = WIDTH // N
QUEENS = []

queen_image = pygame.image.load('queen.png')
queen_image = pygame.transform.scale(queen_image, (SQUARE_SIZE, SQUARE_SIZE))

LEVEL = 0
TIMER_DURATION = 60
start_time = None
time_left = TIMER_DURATION

def draw_board():
    for row in range(N):
        for col in range(N):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(SCREEN, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(SCREEN, (200, 200, 200), (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

def is_conflict(row, col):
    for q_row, q_col in QUEENS:
        if q_col == col or q_row == row or abs(q_row - row) == abs(q_col - col):
            return True
    return False

def draw_queens():
    for row, col in QUEENS:
        SCREEN.blit(queen_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def highlight_invalid_placement(row, col):
    pygame.draw.rect(SCREEN, HIGHLIGHT_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

def draw_timer():
    font = pygame.font.SysFont(None, 36)
    timer_text = font.render(f"Time Left: {time_left}s", True, (255, 0, 0))
    SCREEN.blit(timer_text, (10, 10))

def start_game_timer():
    global start_time, time_left
    if start_time is None:
        start_time = time.time()
    elapsed_time = int(time.time() - start_time)
    time_left = max(TIMER_DURATION - elapsed_time, 0)

def generate_level(level):
    QUEENS.clear()
    for _ in range(level):
        row = random.randint(0, N - 1)
        col = random.randint(0, N - 1)
        while is_conflict(row, col):
            row = random.randint(0, N - 1)
            col = random.randint(0, N - 1)
        QUEENS.append((row, col))

def draw_level_selection():
    SCREEN.fill((50, 50, 50))
    font = pygame.font.SysFont(None, 48)
    title = font.render("Choose Difficulty", True, WHITE)
    SCREEN.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    easy_btn = pygame.Rect(WIDTH // 2 - 100, 200, 200, 50)
    medium_btn = pygame.Rect(WIDTH // 2 - 100, 300, 200, 50)
    hard_btn = pygame.Rect(WIDTH // 2 - 100, 400, 200, 50)

    pygame.draw.rect(SCREEN, (0, 255, 0), easy_btn)
    pygame.draw.rect(SCREEN, (255, 165, 0), medium_btn)
    pygame.draw.rect(SCREEN, (255, 0, 0), hard_btn)

    font_small = pygame.font.SysFont(None, 36)
    SCREEN.blit(font_small.render("Easy", True, BLACK), (easy_btn.x + 70, easy_btn.y + 10))
    SCREEN.blit(font_small.render("Medium", True, BLACK), (medium_btn.x + 50, medium_btn.y + 10))
    SCREEN.blit(font_small.render("Hard", True, BLACK), (hard_btn.x + 70, hard_btn.y + 10))

    pygame.display.flip()

    return easy_btn, medium_btn, hard_btn

def level_selection_screen():
    while True:
        easy_btn, medium_btn, hard_btn = draw_level_selection()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_btn.collidepoint(mouse_pos):
                    return 2
                elif medium_btn.collidepoint(mouse_pos):
                    return 4
                elif hard_btn.collidepoint(mouse_pos):
                    return 6

def main():
    global LEVEL, start_time, time_left

    LEVEL = level_selection_screen()
    generate_level(LEVEL)

    running = True

    while running:
        SCREEN.fill((0, 0, 0))
        draw_board()
        draw_queens()
        draw_timer()

        for row, col in QUEENS:
            if is_conflict(row, col):
                highlight_invalid_placement(row, col)

        start_game_timer()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // SQUARE_SIZE
                row = mouse_y // SQUARE_SIZE

                if (row, col) in QUEENS:
                    QUEENS.remove((row, col))
                else:
                    if not is_conflict(row, col):
                        QUEENS.append((row, col))

        if len(QUEENS) == N and all(not is_conflict(row, col) for row, col in QUEENS):
            font = pygame.font.SysFont(None, 48)
            text = font.render("You Win!", True, (0, 255, 0))
            SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        if time_left == 0 and len(QUEENS) != N:
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over!", True, (255, 0, 0))
            SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
