from pizza import *
import pygame
import config

pygame.init()
clock = pygame.time.Clock()

init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
display_window(config.WINDOW_TITLE)

import sys
import scene
import text_screens

insert_coin = True
insert_coin_screen = text_screens.InsertCoinScreen()

score_table = False
score_table_screen = text_screens.AdvancedPointsTableScreen()

game_over = False
game_over_screen = text_screens.GameOverScreen()

scene.player_lives.set(3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                if insert_coin:
                    insert_coin = False
                    score_table = True
                elif score_table:
                    score_table = False

    keys = pygame.key.get_pressed()

    if scene.player != None and not scene.player.disabled and not scene.player.destroyed:
        if keys[pygame.K_LEFT]:
            scene.player.move(config.LEFT)
        elif keys[pygame.K_RIGHT]:
            scene.player.move(config.RIGHT)

        if keys[pygame.K_UP]:
            scene.player.shoot()

    window.screen.fill(config.WINDOW_COLOR)

    scene.static_hud_context.update()

    if not insert_coin and not score_table:
        scene.game_context.update()

    if insert_coin:
        insert_coin_screen.update()

    if score_table:
        score_table_screen.update()

    if game_over:
        game_over_screen.update()

    if scene.player.projectile != None and not scene.player.projectile.destroyed:
        for alien in scene.alien_storm.get_aliens_alive():
            if alien.collide(scene.player.projectile):
                scene.player.projectile.destroy()
                pop = alien.pop()
                scene.player.points += pop
                scene.score1_text.set_text(str(scene.player.points).zfill(4))
                break
    
    if scene.alien_storm.shooter_alien != None and scene.alien_storm.shooter_alien.projectile != None and not scene.alien_storm.shooter_alien.projectile.destroyed:
        if scene.player.collide(scene.alien_storm.shooter_alien.projectile):
            scene.player.explode()
            scene.alien_storm.shooter_alien.projectile.destroy()
            scene.alien_storm.frozen = True
    
    if not game_over and scene.alien_storm.frozen and scene.player.player_explosion == None:
        player_lives = scene.player_lives.get() - 1
        scene.player_lives.set(player_lives)

        if player_lives == 0:
            game_over = True
            scene.player.destroy()
        else:
            scene.alien_storm.frozen = False

    pygame.display.flip()

    clock.tick(60)