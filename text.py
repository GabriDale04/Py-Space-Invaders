from space_invaders import SpaceInvadersObject

from config import (
    FONT_CHAR_WIDTH,
    FONT_CHAR_HEIGHT,

    FONT_CHAR_COLOR,

    FONT_TEXTURE_ATLAS,

    FONT_CHAR_MAP,

    TEXT_CHARS_GAP
)

class TextChar(SpaceInvadersObject):
    def __init__(
            self,
            context,
            x : int,
            y : int,
            value : str,
            color : tuple[int, int, int] = (255, 255, 255)
        ):

        sprite_coords = FONT_CHAR_MAP.get(value.upper())
        sprite = FONT_TEXTURE_ATLAS.get(sprite_coords[0], sprite_coords[1])

        if color != (255, 255, 255):
            sprite.surface = sprite.surface.convert_alpha()

            for x in range(0, sprite.surface.get_width()):
                for y in range(0, sprite.surface.get_height()):
                    pixcol = sprite.surface.get_at((x, y))

                    if pixcol.a > 0:
                        pixcol.r = color[0]
                        pixcol.g = color[1]
                        pixcol.b = color[2]
                    
                    sprite.surface.set_at((x, y), pixcol)

        super().__init__(
            context = context,
            width = FONT_CHAR_WIDTH,
            height = FONT_CHAR_HEIGHT,
            x = x,
            y = y,
            color = FONT_CHAR_COLOR,
            animations = [sprite]
        )

class Text:
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value : int):
        self.set_pos(value, self._y)
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value : int):
        self.set_pos(self._x, value)

    def __init__(
            self,
            context,
            x : int,
            y : int,
            text : str,
            color : tuple[int, int, int] = (255, 255, 255)
        ):

        self.context = context

        self._x = x
        self._y = y

        self.width = -TEXT_CHARS_GAP
        self.characters = self.__create_chars(x, y, text, color)

    def __create_chars(self, x : int, y : int, text : str, color : tuple[int, int, int]) -> list[TextChar]:
        self.width = -TEXT_CHARS_GAP
        characters : list[TextChar] = []

        for i in range(0, len(text)):
            characters.append(TextChar(self.context, x, y, text[i], color))
            x += FONT_CHAR_WIDTH + TEXT_CHARS_GAP
            self.width += FONT_CHAR_WIDTH + TEXT_CHARS_GAP
        
        return characters
    
    def __destroy_chars(self):
        for char in self.characters:
            char.destroy()
        
        self.characters = []

    def set_pos(self, x : int, y : int):
        self._x = x
        self._y = y

        for char in self.characters:
            char.rect.x = x
            char.rect.y = y

            x += FONT_CHAR_WIDTH + TEXT_CHARS_GAP
    
    def set_text(self, text : str, color : tuple[int, int, int] = (255, 255, 255)):
        self.__destroy_chars()
        self.characters = self.__create_chars(self.x, self.y, text, color)