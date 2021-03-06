import pygame
from Player import Player
from Enemy import Enemy
from Cloud import Cloud

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# https://realpython.com/pygame-a-primer/#images-and-rects

pygame.mixer.init()
pygame.init()

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("Assets/Audio/Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)
collision_sound = pygame.mixer.Sound("Assets/Audio/Collision.ogg")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY, 250)
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()

    screen.fill(pygame.Color('skyblue'))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

        collision_sound.play()

        running = False

    pygame.display.flip()

    clock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
