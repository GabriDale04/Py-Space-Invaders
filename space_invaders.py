from pizza import Context, GameObject, Sprite, window
from config import DEBUG_SHOW_RECTS

class SpaceInvadersObject(GameObject):
    def __init__(
            self,
            context : Context,
            width : int,
            height : int,
            x : int,
            y : int,
            color : tuple[int, int, int] = None,
            animations : list[Sprite] = None
        ):

        super().__init__(
            context,
            width,
            height,
            x,
            y,
            color,
            animations
        )

    def update(self):
        if DEBUG_SHOW_RECTS:
            self.draw_rect()

        super().update()