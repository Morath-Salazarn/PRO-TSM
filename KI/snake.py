import pygame
import sys
import random

# Einstellungen
WIDTH, HEIGHT = 1200, 800
CELL_SIZE = 20
FPS = 8

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

def draw_snake(surface, snake):
    for segment in snake:
        pygame.draw.rect(surface, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(surface, food):
    pygame.draw.rect(surface, RED, (*food, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (CELL_SIZE, 0)
    food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        # Snake bewegen
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Kollision mit Wand oder sich selbst
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake
        ):
            break  # Spielende

        snake.insert(0, new_head)

        # Essen
        if new_head == food:
            score += 1
            food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
            while food in snake:
                food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_snake(screen, snake)
        draw_food(screen, food)

        # Score anzeigen
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Game Over
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 24))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()

if __name__ == "__main__":
    main()