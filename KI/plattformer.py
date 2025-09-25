import pygame
import sys

# Konstanten
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
GRAVITY = 0.5
JUMP_STRENGTH = -10
PLAYER_SPEED = 5

# Farben
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
BROWN = (139, 69, 19)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_STRENGTH

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect(topleft=(x, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mini Mario Plattformer")
    clock = pygame.time.Clock()

    player = Player(100, SCREEN_HEIGHT - 150)
    platforms = pygame.sprite.Group()
    # Boden
    platforms.add(Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
    # Beispiel-Plattformen
    platforms.add(Platform(200, 450, 120, 20))
    platforms.add(Platform(400, 350, 120, 20))
    platforms.add(Platform(600, 250, 120, 20))

    all_sprites = pygame.sprite.Group(player, *platforms)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.jump()

        player.update(platforms)

        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()