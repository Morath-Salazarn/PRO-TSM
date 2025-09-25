import pygame
import random
import sys
# Respawn enemies when all are destroyed
def respawn_enemies_if_needed(enemies, rows, cols):
    if len(enemies) == 0:
        return create_enemies(rows, cols)
    return enemies
# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player settings
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 30
PLAYER_SPEED = 7

# Bullet settings
BULLET_WIDTH, BULLET_HEIGHT = 5, 15
BULLET_SPEED = 10

# Enemy settings
ENEMY_WIDTH, ENEMY_HEIGHT = 40, 30
ENEMY_SPEED = 2
ENEMY_DROP = 40

# FPS
FPS = 60
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(WIDTH//2 - PLAYER_WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, BULLET_WIDTH, BULLET_HEIGHT)

    def update(self):
        self.rect.y -= BULLET_SPEED
        if self.rect.bottom < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)

    def update(self, direction):
        self.rect.x += ENEMY_SPEED * direction

def create_enemies(rows, cols):
    enemies = pygame.sprite.Group()
    for row in range(rows):
        for col in range(cols):
            x = 60 + col * (ENEMY_WIDTH + 20)
            y = 60 + row * (ENEMY_HEIGHT + 20)
            enemies.add(Enemy(x, y))
    return enemies

def main():
    player = Player()
    player_group = pygame.sprite.Group(player)
    bullets = pygame.sprite.Group()
    enemies = create_enemies(4, 8)
    enemy_direction = 1
    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx - BULLET_WIDTH//2, player.rect.top)
                bullets.add(bullet)

        # Update player
        player.update(keys)

        # Update bullets
        bullets.update()

        # Update enemies
        move_down = False
        for enemy in enemies:
            enemy.update(enemy_direction)
            if enemy.rect.right >= WIDTH or enemy.rect.left <= 0:
                move_down = True
        if move_down:
            enemy_direction *= -1
            for enemy in enemies:
                enemy.rect.y += ENEMY_DROP

        # Bullet-enemy collision
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        score += len(hits)

        # Enemy-player collision or enemy reaches bottom
        for enemy in enemies:
            if enemy.rect.colliderect(player.rect) or enemy.rect.bottom >= HEIGHT:
                running = False

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, player.rect)
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet.rect)
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy.rect)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()