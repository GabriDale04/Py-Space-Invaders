import pygame
import sys
import config
from pizza import *

pygame.init()
clock = pygame.time.Clock()

init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
display_window(config.WINDOW_TITLE)

import scene
import text_screens

scene.player_lives.set_lives(3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not scene.player.disabled:
        if keys[pygame.K_LEFT]:
            scene.player.move(config.LEFT)
        elif keys[pygame.K_RIGHT]:
            scene.player.move(config.RIGHT)

        if keys[pygame.K_UP]:
            scene.player.shoot()

    window.screen.fill(config.WINDOW_COLOR)

    scene.static_hud_context.update()
    scene.game_context.update()

    if scene.player.projectile != None and not scene.player.projectile.destroyed:
        for alien in scene.alien_storm.get_aliens_alive():
            if alien.collide(scene.player.projectile):
                scene.player.projectile.destroy()
                pop = alien.pop()
                scene.player.points += pop
                scene.score1_text.set_text(str(scene.player.points).zfill(4))
                break
    
    if scene.alien_storm.shooter_alien.projectile != None and not scene.alien_storm.shooter_alien.projectile.destroyed:
        if scene.player.collide(scene.alien_storm.shooter_alien.projectile):
            scene.player.explode()
            scene.alien_storm.shooter_alien.projectile.destroy()
            scene.alien_storm.frozen = True
    
    if scene.alien_storm.frozen and scene.player.player_explosion == None:
        scene.alien_storm.frozen = False

    pygame.display.flip()

    clock.tick(60)