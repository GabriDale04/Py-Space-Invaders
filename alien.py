from random import randint
from pygame.time import get_ticks
from space_invaders import SpaceInvadersObject
from shooting import Projectile

from config import (
    MAP_LEFT_BOUND,
    MAP_RIGHT_BOUND,

    ALIEN_JELLYFISH_SPRITES,
    ALIEN_ANDROID_SPRITES,
    ALIEN_SKULL_SPRITES,
    ALIEN_JELLYFISH_WIDTH,
    ALIEN_JELLYFISH_HEIGHT,
    ALIEN_ANDROID_WIDTH,
    ALIEN_ANDROID_HEIGHT,
    ALIEN_SKULL_WIDTH,
    ALIEN_SKULL_HEIGHT,
    ALIEN_COLOR,
    ALIEN_KIND_JELLYFISH,
    ALIEN_KIND_ANDROID,
    ALIEN_KIND_SKULL,
    ALIEN_JELLYFISH_POP_REWARD,
    ALIEN_ANDROID_POP_REWARD,
    ALIEN_SKULL_POP_REWARD,
    ALIEN_SPEED,

    ALIEN_UFO_SPRITES,
    ALIEN_UFO_WIDTH,
    ALIEN_UFO_HEIGHT,
    ALIEN_UFO_COLOR,
    ALIEN_KIND_UFO,
    ALIEN_UFO_BASE_POP_REWARD,
    ALIEN_UFO_SPEED,
    ALIEN_UFO_TOP_OFFSET,
    ALIEN_UFO_LEFT_LIMIT,
    ALIEN_UFO_RIGHT_LIMIT,
    ALIEN_UFO_SPAWN_FREQUENCY,

    ALIEN_POP_SPRITES,
    ALIEN_POP_WIDTH,
    ALIEN_POP_HEIGHT,
    ALIEN_POP_COLOR,  
    ALIEN_POP_DURATION,
  
    ALIEN_STORM_COLOR,
    ALIEN_STORM_CELL_WIDTH,
    ALIEN_STORM_CELL_HEIGHT,
    ALIEN_STORM_GAP,
    ALIENS_ROWS,
    ALIENS_PER_ROW,
    ALIENS_BASE_MOVE_TIME_SPAN,
    ALIEN_STORM_MINIMUM_Y,

    PROJECTILE_KIND_HAMMER,
    PROJECTILE_KIND_LIGHTNING,
    PROJECTILE_KIND_SPRING,

    LEFT,
    RIGHT,
    DOWN,

    DEBUG_DONT_SPAWN_ALIENS,
    DEBUG_DONT_SPAWN_UFOS
)

class Alien(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int,
            alien_kind : str,
        ):

        sprites = None
        width = 0
        height = 0
        pop_reward = 0
        projectile_kind = None

        if alien_kind == ALIEN_KIND_JELLYFISH:
            sprites = ALIEN_JELLYFISH_SPRITES
            width = ALIEN_JELLYFISH_WIDTH
            height = ALIEN_JELLYFISH_HEIGHT
            pop_reward = ALIEN_JELLYFISH_POP_REWARD
            projectile_kind = PROJECTILE_KIND_LIGHTNING
        elif alien_kind == ALIEN_KIND_ANDROID:
            sprites = ALIEN_ANDROID_SPRITES
            width = ALIEN_ANDROID_WIDTH
            height = ALIEN_ANDROID_HEIGHT
            pop_reward = ALIEN_ANDROID_POP_REWARD
            projectile_kind = PROJECTILE_KIND_SPRING
        elif alien_kind == ALIEN_KIND_SKULL:
            sprites = ALIEN_SKULL_SPRITES
            width = ALIEN_SKULL_WIDTH
            height = ALIEN_SKULL_HEIGHT
            pop_reward = ALIEN_SKULL_POP_REWARD
            projectile_kind = PROJECTILE_KIND_HAMMER

        super().__init__(
            context = context,
            width = width,
            height = height,
            x = x,
            y = y,
            color = ALIEN_COLOR,
            animations = sprites
        )
        
        self.projectile : Projectile = None
        self.projectile_kind = projectile_kind
        self.pop_reward = pop_reward
    
    def update(self):
        super().update()

        if self.projectile != None and self.projectile.destroyed:
            self.projectile = None

    def move(self, move_direction : str):
        if move_direction == LEFT:
            self.rect.x -= ALIEN_SPEED
        elif move_direction == RIGHT:
            self.rect.x += ALIEN_SPEED
        elif move_direction == DOWN:
            self.rect.y += ALIEN_SPEED
        
        self.animate()

    def shoot(self):
        self.projectile = Projectile(self.context, self.rect.x + self.rect.width // 2, self.rect.y, self.projectile_kind, DOWN)

    def pop(self) -> int:
        AlienPop(self.context, self.rect.x, self.rect.y, get_ticks())
        self.destroy()
        return self.pop_reward

class AlienPop(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int,
            start_time : int
        ):
    
        super().__init__(
            context = context,
            width = ALIEN_POP_WIDTH,
            height = ALIEN_POP_HEIGHT,
            x = x,
            y = y,
            color = ALIEN_POP_COLOR,
            animations = ALIEN_POP_SPRITES
        )

        self.start_time = start_time
    
    def update(self):
        super().update()

        if get_ticks() - self.start_time >= ALIEN_POP_DURATION:
            self.destroy()

class AlienStorm(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int,
        ):

        super().__init__(
            context = context,
            width = ALIEN_STORM_CELL_WIDTH * ALIENS_PER_ROW + (ALIENS_PER_ROW - 1) * ALIEN_STORM_GAP,
            height = ALIEN_STORM_CELL_HEIGHT * ALIENS_ROWS + (ALIENS_ROWS - 1) * ALIEN_STORM_GAP,
            x = x,
            y = y,
            color = ALIEN_STORM_COLOR
        )

        self.aliens : list[list[Alien]] = [] 

        if not DEBUG_DONT_SPAWN_ALIENS:
            self.aliens = self.invade()

        self.shooter_alien : Alien = None
        self.frozen = False
        self.move_direction = RIGHT
        self.last_move_time = 0

    def update(self):
        super().update()
        self.compress_wave()

        if not self.frozen:
            if get_ticks() - self.last_move_time >= ALIENS_BASE_MOVE_TIME_SPAN:
                self.move()
                self.last_move_time = get_ticks()

            if self.shooter_alien == None or self.shooter_alien != None and self.shooter_alien.projectile == None or self.shooter_alien.projectile.destroyed:
                self.shooter_alien = self.pick_shooter()

                if self.shooter_alien != None:
                    self.shooter_alien.shoot()

    def invade(self) -> list[list[Alien]]:
        aliens : list[list[Alien]] = []

        pos_x = self.rect.x
        pos_y = self.rect.y

        for y in range(0, ALIENS_ROWS):
            aliens.append([])
            
            alien_kind = "jellyfish" if y == 0 else "skull" if y >= ALIENS_ROWS - 2 else "android"

            for x in range(0, ALIENS_PER_ROW):
                aliens[y].append(Alien(self.context, pos_x, pos_y, alien_kind))

                pos_x += ALIEN_STORM_CELL_WIDTH + ALIEN_STORM_GAP
            
            pos_x = self.rect.x
            pos_y += ALIEN_STORM_CELL_HEIGHT + ALIEN_STORM_GAP
        
        return aliens
    
    def move(self):
        move_direction = self.move_direction

        if self.move_direction == RIGHT and self.rect.x + self.rect.width + ALIEN_SPEED >= MAP_RIGHT_BOUND:
            move_direction = DOWN
            self.move_direction = LEFT
        elif self.move_direction == LEFT and self.rect.x + ALIEN_SPEED <= MAP_LEFT_BOUND:
            move_direction = DOWN
            self.move_direction = RIGHT

        if move_direction == LEFT:
            self.rect.x -= ALIEN_SPEED
        elif move_direction == RIGHT:
            self.rect.x += ALIEN_SPEED
        elif move_direction == DOWN:
            self.rect.y += ALIEN_SPEED

        for alien in self.get_aliens_alive():
            alien.move(move_direction)

    def pick_shooter(self) -> Alien:
        ready_aliens : list[Alien] = []

        for x in range(0, ALIENS_PER_ROW):
            ready_alien : Alien = None

            for y in range(0, len(self.aliens)):
                alien = self.aliens[y][x]
                if alien != None and not alien.destroyed:
                    ready_alien = alien
                else:
                    self.aliens[y][x] = None
        
            if ready_alien != None:
                ready_aliens.append(ready_alien)

        if len(ready_aliens) > 0:
            return ready_aliens[randint(0, len(ready_aliens) - 1)]

    def compress_wave(self):
        if len(self.aliens) == 0:
            return

        for x in range(0, ALIENS_PER_ROW):
            if self.aliens[len(self.aliens) - 1][x] != None:
                return
            
        self.aliens.pop()
        self.rect.height = ALIEN_STORM_CELL_WIDTH * len(self.aliens) + (len(self.aliens) - 1) * ALIEN_STORM_GAP

    def has_invaded(self) -> bool:
        if self.rect.y + self.rect.height >= ALIEN_STORM_MINIMUM_Y:
            return True

        return False

    def get_aliens_alive(self) -> list[Alien]:
        aliens_alive : list[Alien] = []

        for row in self.aliens:
            aliens_alive.extend([alien for alien in row if alien != None and not alien.destroyed])
        
        return aliens_alive

class AlienDummy(SpaceInvadersObject):
    def __init__(
            self, 
            context,
            x : int,
            y : int,
            alien_kind : str
        ):

        sprites = None
        width = 0
        height = 0

        if alien_kind == ALIEN_KIND_JELLYFISH:
            sprites = ALIEN_JELLYFISH_SPRITES
            width = ALIEN_JELLYFISH_WIDTH
            height = ALIEN_JELLYFISH_HEIGHT
        elif alien_kind == ALIEN_KIND_ANDROID:
            sprites = ALIEN_ANDROID_SPRITES
            width = ALIEN_ANDROID_WIDTH
            height = ALIEN_ANDROID_HEIGHT
        elif alien_kind == ALIEN_KIND_SKULL:
            sprites = ALIEN_SKULL_SPRITES
            width = ALIEN_SKULL_WIDTH
            height = ALIEN_SKULL_HEIGHT
        elif alien_kind == ALIEN_KIND_UFO:
            sprites = ALIEN_UFO_SPRITES
            width = ALIEN_UFO_WIDTH
            height = ALIEN_UFO_HEIGHT
        
        super().__init__(
            context = context,
            width = width,
            height = height,
            x = x,
            y = y,
            color = ALIEN_UFO_COLOR if alien_kind == "ufo" else ALIEN_COLOR,
            animations = sprites
        )

class UFOSpawner:
    def __init__(
            self,
            context
        ):

        self.context = context
        self.last_spawn = -1
        self.direction = RIGHT
        self.pop_reward = ALIEN_UFO_BASE_POP_REWARD

        self.ufo : UFO = None
    
    def try_spawn_ufo(self):
        if not DEBUG_DONT_SPAWN_UFOS:
            if self.ufo != None and self.ufo.destroyed:
                self.ufo = None

            if self.ufo == None and get_ticks() - self.last_spawn >= ALIEN_UFO_SPAWN_FREQUENCY:
                spawn_pos = ALIEN_UFO_LEFT_LIMIT if self.direction == RIGHT else ALIEN_UFO_RIGHT_LIMIT

                self.ufo = UFO(self.context, spawn_pos, ALIEN_UFO_TOP_OFFSET, self.direction, self.pop_reward)
                self.direction = RIGHT if self.direction == LEFT else LEFT
                self.last_spawn = get_ticks()

                self.pop_reward += 5

class UFO(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int,
            direction : str,
            pop_reward : int
        ):

        super().__init__(
            context = context,
            width = ALIEN_UFO_WIDTH,
            height = ALIEN_UFO_HEIGHT,
            x = x,
            y = y,
            color = ALIEN_UFO_COLOR,
            animations = ALIEN_UFO_SPRITES
        )

        self.direction = direction
        self.pop_reward = pop_reward
    
    def update(self):
        super().update()
        self.move()
    
    def move(self):
        if self.direction == LEFT:
            if self.rect.x - ALIEN_UFO_SPEED <= MAP_LEFT_BOUND:
                self.destroy()
            else:
                self.rect.x -= ALIEN_UFO_SPEED
        elif self.direction == RIGHT:
            if self.rect.x + ALIEN_UFO_SPEED + self.rect.width >= MAP_RIGHT_BOUND:
                self.destroy()
            else:
                self.rect.x += ALIEN_UFO_SPEED
    
    def pop(self) -> int:
        self.destroy()
        return self.pop_reward