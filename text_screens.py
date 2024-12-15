from pygame.time import get_ticks
from space_invaders import SpaceInvadersObject
from config import (
    WINDOW_HEIGHT,
    GAME_OVER_TYPING_TIME_SPAN,
    SCORE_TABLE_TYPING_TIME_SPAN
)

import scene

class GameOverScreen:
    def __init__(self):
        self.displayed_characters = 0
        self.last_character_display = 0
    
    def update(self):
        if self.displayed_characters < len(scene.game_over_text.characters):
            if get_ticks() - self.last_character_display >= GAME_OVER_TYPING_TIME_SPAN:
                self.displayed_characters += 1
                self.last_character_display = get_ticks()
        
        for i in range(0, self.displayed_characters):
            scene.game_over_text.characters[i].update()

class AdvancedPointsTableScreen:
    def __init__(self):
        self.displayed_objects = 0
        self.last_object_display = 0

        self.objects : list[SpaceInvadersObject] = []

        self.objects.extend(
            scene.play_text.characters +
            scene.space_invaders_text.characters +
            scene.score_table_text.characters +
            [scene.mystery_alien_dummy] +
            scene.mystery_alien_points_text.characters +
            [scene.jellyfish_alien_dummy] +
            scene.jellyfish_alien_points_text.characters +
            [scene.android_alien_dummy] +
            scene.android_alien_points_text.characters +
            [scene.skull_alien_dummy] +
            scene.skull_alien_points_text.characters
        )

        self.__center_vertically()
    
    def __center_vertically(self):
        first = self.objects[0]
        last = self.objects[len(self.objects) - 1]

        total_height = last.rect.y + last.rect.width - first.rect.y

        start_y = WINDOW_HEIGHT // 2 - total_height // 2
        sub = first.rect.y

        for obj in self.objects:
            obj.rect.y = start_y + obj.rect.y - sub

    def update(self):
        if self.displayed_objects < len(self.objects):
            if get_ticks() - self.last_object_display >= SCORE_TABLE_TYPING_TIME_SPAN:
                self.displayed_objects += 1
                self.last_object_display = get_ticks()
        
        for i in range(0, self.displayed_objects):
            self.objects[i].update()