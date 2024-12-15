from typing import Union

from pygame import (
    image,
    transform,
    draw,
    display,
    Rect,
    Surface
)

class window:
    screen : Surface = None

def init_window(width : int, height : int):
    window.screen = display.set_mode((width, height))

def display_window(title : str) -> None:
    display.set_caption(title)

class Context:
    def __init__(self):
        self.game_objects : list[GameObject] = []
    
    def update(self):
        for game_object in self.game_objects:
            game_object.update()

class Sprite:
    def __init__(
            self, 
            resource : Union[str, Surface],
            width : int = 0,
            height : int = 0
        ):

        if isinstance(resource, str):
            self.surface = image.load(resource)
            self.surface = transform.scale(self.surface, (width, height))
        elif isinstance(resource, Surface):
            self.surface = resource

class GameObject:
    @property
    def animations(self):
        return self._animations
    
    @animations.setter
    def animations(self, value : list[Sprite]):
        self._animations = value
        self.current_animation = 0

    def __init__(
            self,
            context : Context,
            width : int,
            height : int,
            x : int = 0,
            y : int = 0,
            color : tuple[int, int, int] = None,
            animations : list[Sprite] = None
        ):

        self.color = color if color != None else (0, 0, 0)

        self._animations = animations     
        self.current_animation = 0

        self.disabled = False
        self.destroyed = False

        self.rect = Rect(x, y, width, height)

        self.context = context

        context.game_objects.append(self)

    def update(self):
        if not self.disabled:
            if self._animations != None and len(self._animations) > 0:
                window.screen.blit(self._animations[self.current_animation].surface, self.rect)

    def draw_rect(self):
        if not self.disabled:
            draw.rect(window.screen, self.color, self.rect)

    def destroy(self):
        self.destroyed = True
        self.context.game_objects.remove(self)

    def animate(self):
        if len(self._animations) > 0:
            self.current_animation = (self.current_animation + 1) % len(self._animations)
        
    def collide(self, other : 'GameObject') -> bool:
        if not self.disabled:
            return self.rect.colliderect(other.rect)
        
        return False

class TextureAtlas:
    def __init__(
            self,
            texture_sprite : Sprite,
            textures_width : int,
            textures_height : int,
            textures_gap : int
        ):

        self.texture_sprite = texture_sprite
        self.textures_width = textures_width
        self.textures_height = textures_height
        self.textures_gap = textures_gap
    
    def get(self, x : int, y : int) -> Sprite:
        atlas = self.texture_sprite.surface.convert_alpha()

        sub_area = Rect(
            x * self.textures_width + x * self.textures_gap,
            y * self.textures_height + y * self.textures_gap,
            self.textures_width,
            self.textures_height
        )

        return Sprite(atlas.subsurface(sub_area))