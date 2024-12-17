from pizza import *
import pygame
import config

pygame.init()
clock = pygame.time.Clock()

init_window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
display_window(config.WINDOW_TITLE)

from misc import short
import sys
import scene
import text_screens
import save

config.PLAYER_BASE_LIVES = 32767

score = 0

end_game = False
wave_clear = False
wave_clear_time = 0

insert_coin = True
insert_coin_screen = text_screens.InsertCoinScreen()

score_table = False
score_table_screen = text_screens.AdvancedPointsTableScreen()

game_over = False
game_over_screen = text_screens.GameOverScreen()

scene.score1_text.set_text(str(score).zfill(4))
scene.score2_text.set_text(str(0).zfill(4))
scene.hi_score_text.set_text(str(save.read_score()).zfill(4))
scene.player_lives.set(config.PLAYER_BASE_LIVES)

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

    if not (wave_clear or insert_coin or score_table):
        # Check collision with the player projectile and aliens
        if scene.player.projectile != None and not scene.player.projectile.destroyed:
            if scene.ufo_spawner.ufo != None and scene.ufo_spawner.ufo.collide(scene.player.projectile):
                scene.player.projectile.destroy()
                
                pop = scene.ufo_spawner.ufo.pop()
                score += pop
                scene.score1_text.set_text(str(short(score)).zfill(4))
            else:
                alive_aliens = scene.alien_storm.get_aliens_alive()

                for alien in alive_aliens:
                    if alien.collide(scene.player.projectile):
                        scene.player.projectile.destroy()

                        pop = alien.pop()
                        score += pop
                        scene.score1_text.set_text(str(short(score)).zfill(4))

                        if len(alive_aliens) == 1:
                            wave_clear = True
                            wave_clear_time = pygame.time.get_ticks()
                            scene.player.frozen = True

                        break
        
        if scene.ufo_spawner.last_spawn == -1:
            scene.ufo_spawner.last_spawn = pygame.time.get_ticks()
        else:
            scene.ufo_spawner.try_spawn_ufo()
        
        # Check collision with the alien projectile and player
        if scene.alien_storm.shooter_alien != None and scene.alien_storm.shooter_alien.projectile != None and not scene.alien_storm.shooter_alien.projectile.destroyed:
            if scene.player.collide(scene.alien_storm.shooter_alien.projectile):
                scene.player.explode()
                scene.alien_storm.shooter_alien.projectile.destroy()
                scene.alien_storm.frozen = True
    
        # Set 'end_game' to 'True' if the aliens get too close to the ground
        if scene.alien_storm.has_invaded() and not end_game:
            scene.alien_storm.frozen = True
            scene.player.explode()
            end_game = True
        
        # When the player explosion animation ends and 'end_game' is 'True', save the score and play the game over screen.
        if not scene.player.destroyed and scene.player.player_explosion == None and end_game:
            game_over = True
            scene.player.destroy()
            save.save_hi_score(score)
        
        # Once the player explosion animation ends, substract one life from the player. 
        # If the player has 0 lives, play the game over screen.
        if not game_over and scene.alien_storm.frozen and scene.player.player_explosion == None:
            player_lives = scene.player_lives.get() - 1
            scene.player_lives.set(player_lives)

            if player_lives == 0:
                game_over = True
                scene.player.destroy()
                save.save_hi_score(score)
            else:
                scene.alien_storm.frozen = False
    # Generate a new alien wave after it has been cleared
    elif wave_clear and pygame.time.get_ticks() - wave_clear_time >= config.WAVE_CLEAR_DURATION:
        wave_clear = False
        wave_clear_time = 0

        scene.alien_storm.destroy()
        scene.player.destroy()

        scene.alien_storm = scene.new_alien_storm()
        scene.player = scene.new_player()

        scene.ufo_spawner.last_spawn = pygame.time.get_ticks()

    pygame.display.flip()

    clock.tick(60)