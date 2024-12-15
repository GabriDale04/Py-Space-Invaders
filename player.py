from pygame.time import get_ticks
from space_invaders import SpaceInvadersObject
from shooting import Projectile
from text import Text

from config import (
    MAP_LEFT_BOUND,
    MAP_RIGHT_BOUND,

    PLAYER_SPRITES,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_COLOR,
    PLAYER_SPEED,

    PLAYER_EXPLOSION_TRIGGER_SPRITES,
    PLAYER_EXPLOSION_SPRITES,
    PLAYER_EXPLOSION_WIDTH,
    PLAYER_EXPLOSION_HEIGHT,
    PLAYER_EXPLOSION_COLOR,
    PLAYER_EXPLOSION_TRIGGER_DURATION,
    PLAYER_EXPLOSION_TOTAL_DURATION,
    PLAYER_EXPLOSION_ANIMATION_DURATION,

    PROJECTILE_KIND_PEW,

    FONT_CHAR_WIDTH,

    LIVES_LEFT_TEXT,
    LIVES_LEFT_TEXT_TOP_OFFSET,

    LEFT,
    RIGHT,
    UP
)

class Player(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int
        ):
        
        super().__init__(
            context = context,
            width = PLAYER_WIDTH,
            height = PLAYER_HEIGHT,
            x = x,
            y = y,
            color = PLAYER_COLOR,
            animations = PLAYER_SPRITES
        )

        self.points = 0

        self.projectile : Projectile = None
        self.player_explosion : PlayerExplosion = None
    
    def update(self):
        super().update()

        if self.projectile != None and self.projectile.destroyed:
            self.projectile = None
        
        if self.player_explosion != None and self.player_explosion.destroyed:
            self.disabled = False
            self.player_explosion = None

    def move(self, direction : str):
        if direction == LEFT:
            if self.rect.x - PLAYER_SPEED <= MAP_LEFT_BOUND:
                self.rect.x = MAP_LEFT_BOUND
            else:
                self.rect.x -= PLAYER_SPEED
        elif direction == RIGHT:
            if self.rect.x + PLAYER_WIDTH + PLAYER_SPEED >= MAP_RIGHT_BOUND:
                self.rect.x = MAP_RIGHT_BOUND - PLAYER_WIDTH
            else:
                self.rect.x += PLAYER_SPEED
    
    def shoot(self):
        if self.projectile == None:
            self.projectile = Projectile(self.context, self.rect.x + self.rect.width // 2, self.rect.y, PROJECTILE_KIND_PEW, UP)

    def explode(self):
        self.player_explosion = PlayerExplosion(self.context, self.rect.x, self.rect.y, get_ticks())
        self.disabled = True

class PlayerExplosion(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int,
            start_time : int
        ):

        super().__init__(
            context = context,
            width = PLAYER_EXPLOSION_WIDTH,
            height = PLAYER_EXPLOSION_HEIGHT,
            x = x,
            y = y,
            color = PLAYER_EXPLOSION_COLOR,
            animations = PLAYER_EXPLOSION_TRIGGER_SPRITES
        )

        self.trigger_finished = False
        self.start_time = start_time
        self.last_animation_time = 0
    
    def update(self):
        super().update()

        if not self.trigger_finished and get_ticks() - self.start_time >= PLAYER_EXPLOSION_TRIGGER_DURATION:
            self.trigger_finished = True
            self.animations = PLAYER_EXPLOSION_SPRITES
        elif get_ticks() - self.start_time >= PLAYER_EXPLOSION_TOTAL_DURATION:
            self.destroy()
        elif get_ticks() - self.last_animation_time >= PLAYER_EXPLOSION_ANIMATION_DURATION:
            self.animate()
            self.last_animation_time = get_ticks()

class PlayerLives:
    def __init__(
            self,
            context,
            x : int,
            y : int
        ):

        self.context = context

        self.__x = x
        self.__y = y

        self.lives_left_text = Text(context, MAP_LEFT_BOUND, LIVES_LEFT_TEXT_TOP_OFFSET, LIVES_LEFT_TEXT)
        self.lives : list[PlayerDummy] = []
    
    def get(self) -> int:
        return len(self.lives) + 1

    def set(self, value : int):
        for life in self.lives:
            life.destroy()
        
        self.lives = []

        self.lives_left_text.set_text(str(value))

        x = self.__x + self.lives_left_text.width + FONT_CHAR_WIDTH
        y = self.__y

        for i in range(0, value - 1):
            if i >= 16:
                break

            life = PlayerDummy(self.context, x, y)
            self.lives.append(life)

            x += life.rect.width + life.rect.width // 4

class PlayerDummy(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int
        ):

        super().__init__(
            context = context,
            width = PLAYER_WIDTH,
            height = PLAYER_HEIGHT,
            x = x,
            y = y,
            color = PLAYER_COLOR,
            animations = PLAYER_SPRITES
        )