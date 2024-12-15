from pygame.time import get_ticks
from space_invaders import SpaceInvadersObject

from config import (
    MAP_TOP_BOUND,
    MAP_BOTTOM_BOUND,

    PROJECTILE_PEW_SPRITES,
    PROJECTILE_HAMMER_SPRITES,
    PROJECTILE_LIGHTNING_SPRITES,
    PROJECTILE_SPRING_SPRITES,

    PROJECTILE_PEW_WIDTH,
    PROJECTILE_PEW_HEIGHT,
    PROJECTILE_HAMMER_WIDTH,
    PROJECTILE_HAMMER_HEIGHT,
    PROJECTILE_LIGHTNING_WIDTH,
    PROJECTILE_LIGHTNING_HEIGHT,
    PROJECTILE_SPRING_WIDTH,
    PROJECTILE_SPRING_HEIGHT,

    PROJECTILE_COLOR,

    PROJECTILE_KIND_PEW,
    PROJECTILE_KIND_HAMMER,
    PROJECTILE_KIND_LIGHTNING,
    PROJECTILE_KIND_SPRING,

    PROJECTILE_PEW_SPEED,
    PROJECTILE_HAMMER_SPEED,
    PROJECTILE_LIGHTNING_SPEED,
    PROJECTILE_SPRING_SPEED,

    PROJECTILE_ANIMATION_DURATION,

    PROJECTILE_CRASH_ROOF,
    PROJECTILE_CRASH_FLOOR,

    PROJECTILE_CRASH_ROOF_WIDTH,
    PROJECTILE_CRASH_ROOF_HEIGHT,
    PROJECTILE_CRASH_FLOOR_WIDTH,
    PROJECTILE_CRASH_FLOOR_HEIGHT,

    PROJECTILE_CRASH_COLOR,

    PROJECTILE_CRASH_KIND_ROOF,
    PROJECTILE_CRASH_KIND_FLOOR,

    PROJECTILE_CRASH_DURATION,

    UP,
    DOWN
)

class Projectile(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int,
            projectile_kind : str,
            direction : str
        ):
        
        sprites = None
        width = 0
        height = 0

        if projectile_kind == PROJECTILE_KIND_PEW:
            sprites = PROJECTILE_PEW_SPRITES
            width = PROJECTILE_PEW_WIDTH
            height = PROJECTILE_PEW_HEIGHT
            speed = PROJECTILE_PEW_SPEED
        elif projectile_kind == PROJECTILE_KIND_HAMMER:
            sprites = PROJECTILE_HAMMER_SPRITES
            width = PROJECTILE_HAMMER_WIDTH
            height = PROJECTILE_HAMMER_HEIGHT
            speed = PROJECTILE_HAMMER_SPEED
        elif projectile_kind == PROJECTILE_KIND_LIGHTNING:
            sprites = PROJECTILE_LIGHTNING_SPRITES
            width = PROJECTILE_LIGHTNING_WIDTH
            height = PROJECTILE_LIGHTNING_HEIGHT
            speed = PROJECTILE_LIGHTNING_SPEED
        elif projectile_kind == PROJECTILE_KIND_SPRING:
            sprites = PROJECTILE_SPRING_SPRITES
            width = PROJECTILE_SPRING_WIDTH
            height = PROJECTILE_SPRING_HEIGHT
            speed = PROJECTILE_SPRING_SPEED

        super().__init__(
            context = context,
            width = width,
            height = height,
            x = x,
            y = y,
            color = PROJECTILE_COLOR,
            animations = sprites
        )

        self.speed = speed
        self.direction = direction

        self.animation_start_time = get_ticks()
    
    def update(self):
        super().update()

        if get_ticks() - self.animation_start_time >= PROJECTILE_ANIMATION_DURATION:
            self.animate()
            self.animation_start_time = get_ticks()

        self.move()
    
    def move(self):
        if self.direction == UP:
            if self.rect.y <= MAP_TOP_BOUND:
                ProjectileCrash(self.context, self.rect.x - PROJECTILE_CRASH_ROOF_WIDTH // 2, self.rect.y, PROJECTILE_CRASH_KIND_ROOF, get_ticks())
                self.destroy()
            else:
                self.rect.y -= self.speed
        elif self.direction == DOWN:
            if self.rect.y + self.rect.height >= MAP_BOTTOM_BOUND:
                ProjectileCrash(self.context, self.rect.x - PROJECTILE_CRASH_FLOOR_WIDTH // 2, self.rect.y, PROJECTILE_CRASH_KIND_FLOOR, get_ticks())
                self.destroy()
            else:
                self.rect.y += self.speed  

class ProjectileCrash(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int,
            projectile_crash_kind : str,
            start_time : int
        ):
    
        sprites = None
        width = 0
        height = 0

        if projectile_crash_kind == PROJECTILE_CRASH_KIND_ROOF:
            sprites = PROJECTILE_CRASH_ROOF
            width = PROJECTILE_CRASH_ROOF_WIDTH
            height = PROJECTILE_CRASH_ROOF_HEIGHT
        elif projectile_crash_kind == PROJECTILE_CRASH_KIND_FLOOR:
            sprites = PROJECTILE_CRASH_FLOOR
            width = PROJECTILE_CRASH_FLOOR_WIDTH
            height = PROJECTILE_CRASH_FLOOR_HEIGHT

        super().__init__(
            context = context,
            width = width,
            height = height,
            x = x,
            y = y,
            color = PROJECTILE_CRASH_COLOR,
            animations = sprites
        )

        self.start_time = start_time
    
    def update(self):
        super().update()

        if get_ticks() - self.start_time >= PROJECTILE_CRASH_DURATION:
            self.destroy()