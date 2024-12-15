import config
from pizza import Context
from space_invaders import SpaceInvadersObject
from player import Player, PlayerLives
from alien import AlienStorm, AlienDummy
from text import Text

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

# 'static_hud_context' manages the HUD game objects that are always displayed
static_hud_context             = Context()

score1_text_label              = Text(static_hud_context, config.MAP_LEFT_BOUND, config.SCORE1_LABEL_TEXT_TOP_OFFSET, config.SCORE1_LABEL_TEXT)

hi_score_text_label            = Text(static_hud_context, config.WINDOW_WIDTH // 2, config.HI_SCORE_LABEL_TEXT_TOP_OFFSET, config.HI_SCORE_LABEL_TEXT)
hi_score_text_label.x          -= hi_score_text_label.width // 2

score2_text_label              = Text(static_hud_context, config.MAP_RIGHT_BOUND, config.SCORE2_LABEL_TEXT_TOP_OFFSET, config.SCORE2_LABEL_TEXT)
score2_text_label.x            -= score2_text_label.width

score1_text                    = Text(static_hud_context, score1_text_label.x + score1_text_label.width // 4, score1_text_label.y + config.FONT_CHAR_HEIGHT + config.TEXT_CHARS_GAP * 4, config.SCORE1_TEXT)

hi_score_text                  = Text(static_hud_context, hi_score_text_label.x + hi_score_text_label.width // 4, hi_score_text_label.y + config.FONT_CHAR_HEIGHT + config.TEXT_CHARS_GAP * 4, config.HI_SCORE_TEXT)

score2_text                    = Text(static_hud_context, score2_text_label.x + score2_text_label.width // 4, score2_text_label.y + config.FONT_CHAR_HEIGHT + config.TEXT_CHARS_GAP * 4, config.SCORE2_TEXT)

credit_text                    = Text(static_hud_context, config.MAP_RIGHT_BOUND, config.CREDIT_TEXT_TOP_OFFSET, config.CREDIT_TEXT)
credit_text.x                  -= credit_text.width

# 'game_context' manages the game objects that are displayed when playing the game
game_context                   = Context()

alien_storm                    = AlienStorm(game_context, config.ALIEN_STORM_SPAWN_POS_X, config.ALIEN_STORM_SPAWN_POS_Y)
player                         = Player(game_context, config.PLAYER_SPAWN_POS_X, config.PLAYER_SPAWN_POS_Y)

bottom_line                    = BottomLine(game_context, config.BOTTOM_LINE_LEFT_OFFSET, config.BOTTOM_LINE_TOP_OFFSET)

player_lives                   = PlayerLives(game_context, config.MAP_LEFT_BOUND, config.LIVES_LEFT_TEXT_TOP_OFFSET)

# 'game_over_context' manages the HUD game objects shown once the player is defeated
game_over_context              = Context()

game_over_text                 = Text(game_over_context, config.WINDOW_WIDTH // 2, config.GAME_OVER_TEXT_TOP_OFFSET, config.GAME_OVER_TEXT, (255, 0, 0))
game_over_text.x               -= game_over_text.width // 2

# 'score_advanced_table_context' manages the points table that is shown before the game starts
score_advanced_table_context   = Context()

play_text                      = Text(score_advanced_table_context, config.WINDOW_WIDTH // 2, config.SCORE_TABLE_TOP_OFFSET, config.PLAY_TEXT)
play_text.x                    -= play_text.width // 2

space_invaders_text            = Text(score_advanced_table_context, config.WINDOW_WIDTH // 2, play_text.y + config.FONT_CHAR_HEIGHT * 4, config.SPACE_INVADERS_TEXT)
space_invaders_text.x          -= space_invaders_text.width // 2

score_table_text               = Text(score_advanced_table_context, config.WINDOW_WIDTH // 2, space_invaders_text.y + config.FONT_CHAR_HEIGHT * 4, config.SCORE_TABLE_TEXT)
score_table_text.x             -= score_table_text.width // 2

mystery_alien_dummy            = AlienDummy(score_advanced_table_context, 0, score_table_text.y + config.FONT_CHAR_HEIGHT * 2, "ufo")
mystery_alien_points_text      = Text(score_advanced_table_context, config.WINDOW_WIDTH // 2 + mystery_alien_dummy.rect.width // 2, mystery_alien_dummy.rect.y, config.MYSTERY_POINTS_TEXT)
mystery_alien_points_text.x    -= mystery_alien_points_text.width // 2
mystery_alien_dummy.rect.x     = mystery_alien_points_text.x - mystery_alien_dummy.rect.width

jellyfish_alien_dummy          = AlienDummy(score_advanced_table_context, 0, mystery_alien_points_text.y + config.FONT_CHAR_HEIGHT * 2, "jellyfish")
jellyfish_alien_points_text    = Text(score_advanced_table_context, mystery_alien_points_text.x, jellyfish_alien_dummy.rect.y, config.JELLYFISH_POINTS_TEXT)
jellyfish_alien_dummy.rect.x   = jellyfish_alien_points_text.x - jellyfish_alien_dummy.rect.width - (mystery_alien_dummy.rect.width - jellyfish_alien_dummy.rect.width) // 2

android_alien_dummy            = AlienDummy(score_advanced_table_context, 0, jellyfish_alien_points_text.y + config.FONT_CHAR_HEIGHT * 2, "android")
android_alien_points_text      = Text(score_advanced_table_context, mystery_alien_points_text.x, android_alien_dummy.rect.y, config.ANDROID_POINTS_TEXT)
android_alien_dummy.rect.x     = android_alien_points_text.x - android_alien_dummy.rect.width  - (mystery_alien_dummy.rect.width - android_alien_dummy.rect.width) // 2

skull_alien_dummy              = AlienDummy(score_advanced_table_context, 0, android_alien_points_text.y + config.FONT_CHAR_HEIGHT * 2, "skull")
skull_alien_points_text        = Text(score_advanced_table_context, mystery_alien_points_text.x, skull_alien_dummy.rect.y, config.SKULL_POINTS_TEXT)
skull_alien_dummy.rect.x       = skull_alien_points_text.x - skull_alien_dummy.rect.width - (mystery_alien_dummy.rect.width - skull_alien_dummy.rect.width) // 2