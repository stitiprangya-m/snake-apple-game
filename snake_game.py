import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# ---------- FUNCTIONS ----------

def spawn_apple(snake):
    while True:
        apple = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))
        if apple not in snake:
            return apple

def game_over_screen(score):
    font = pygame.font.SysFont(None, 50)
    small_font = pygame.font.SysFont(None, 30)

    game_over_text = font.render("GAME OVER", True, RED)
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    restart_text = small_font.render("Press R to Restart or Q to Quit", True, WHITE)

    screen.fill(BLACK)
    screen.blit(game_over_text, (200, 120))
    screen.blit(score_text, (250, 180))
    screen.blit(restart_text, (140, 240))

    pygame.display.update()

def wait_for_restart():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

# ---------- GAME LOOP ----------

while True:

    # RESET GAME
    snake = [(100, 50), (90, 50), (80, 50)]
    direction = "RIGHT"
    apple = spawn_apple(snake)
    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # MOVE
        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= 10
        elif direction == "DOWN":
            head_y += 10
        elif direction == "LEFT":
            head_x -= 10
        elif direction == "RIGHT":
            head_x += 10

        new_head = (head_x, head_y)
        snake.insert(0, new_head)

        # APPLE
        if new_head == apple:
            score += 1
            apple = spawn_apple(snake)
        else:
            snake.pop()

        # COLLISION
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in snake[1:]
        ):
            running = False

        # DRAW
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 10, 10))

        pygame.draw.rect(screen, RED, (apple[0], apple[1], 10, 10))

        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(10)

    # GAME OVER
    game_over_screen(score)
    wait_for_restart()