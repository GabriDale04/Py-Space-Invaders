from space_invaders import SpaceInvadersObject
from pizza import Context
import config

def short(value : int) -> int:
    SHORT_MIN_VALUE = -(2 ** 15)
    SHORT_MAX_VALUE = (2 ** 15) - 1

    range_size = SHORT_MAX_VALUE - SHORT_MIN_VALUE

    return (value - SHORT_MIN_VALUE) % range_size + SHORT_MIN_VALUE

class BottomLine(SpaceInvadersObject):
    def __init__(
            self,
            context : Context,
            x : int,
            y : int
        ):

        super().__init__(
            context = context,
            width = config.BOTTOM_LINE_WIDTH,
            height = config.BOTTOM_LINE_HEIGHT,
            x = x,
            y = y,
            color = config.BOTTOM_LINE_COLOR
        )
    
    def update(self):
        super().update()
        self.draw_rect()