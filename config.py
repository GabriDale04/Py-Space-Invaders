from pizza import Sprite, TextureAtlas

# [WINDOW]
WINDOW_WIDTH                        = 924
WINDOW_HEIGHT                       = 820
WINDOW_TITLE                        = "スペースインベーダー"
WINDOW_COLOR                        = (0, 0, 0)

# [MAP]
MAP_LEFT_BOUND                      = 125
MAP_RIGHT_BOUND                     = WINDOW_WIDTH - 125
MAP_TOP_BOUND                       = 125
MAP_BOTTOM_BOUND                    = WINDOW_HEIGHT - 75

# [PLAYER]
PLAYER_SPRITES                      = [Sprite("textures/spaceship.png", 48, 48)]

PLAYER_WIDTH                        = 40
PLAYER_HEIGHT                       = 40

PLAYER_COLOR                        = (100, 100, 100)

PLAYER_SPEED                        = 7

PLAYER_SPAWN_POS_X                  = MAP_LEFT_BOUND
PLAYER_SPAWN_POS_Y                  = MAP_BOTTOM_BOUND - PLAYER_WIDTH - 25

PLAYER_EXPLOSION_TRIGGER_SPRITES    = [Sprite("textures/spaceship_explosion_trigger.png", 48, 48)]
PLAYER_EXPLOSION_SPRITES            = [Sprite("textures/spaceship_explosion_1.png", 48, 48), Sprite("textures/spaceship_explosion_2.png", 48, 48)]

PLAYER_EXPLOSION_WIDTH              = 45
PLAYER_EXPLOSION_HEIGHT             = 45

PLAYER_EXPLOSION_COLOR              = (255, 0, 255)

PLAYER_EXPLOSION_TRIGGER_DURATION   = 100
PLAYER_EXPLOSION_TOTAL_DURATION     = 900 + PLAYER_EXPLOSION_TRIGGER_DURATION
PLAYER_EXPLOSION_ANIMATION_DURATION = 75

# [ALIENS]
ALIEN_JELLYFISH_SPRITES             = [Sprite("textures/jellyfish_idle.png", 48, 48), Sprite("textures/jellyfish_stance.png", 48, 48)]
ALIEN_ANDROID_SPRITES               = [Sprite("textures/android_idle.png", 48, 48), Sprite("textures/android_stance.png", 48, 48)]
ALIEN_SKULL_SPRITES                 = [Sprite("textures/skull_idle.png", 48, 48), Sprite("textures/skull_stance.png", 48, 48)]

ALIEN_JELLYFISH_WIDTH               = 24
ALIEN_JELLYFISH_HEIGHT              = 24
ALIEN_ANDROID_WIDTH                 = 34
ALIEN_ANDROID_HEIGHT                = 34
ALIEN_SKULL_WIDTH                   = 36
ALIEN_SKULL_HEIGHT                  = 36

ALIEN_COLOR                         = (0, 0, 255)

ALIEN_KIND_JELLYFISH                = "jellyfish"
ALIEN_KIND_ANDROID                  = "android"
ALIEN_KIND_SKULL                    = "skull"

ALIEN_JELLYFISH_POP_REWARD          = 30
ALIEN_ANDROID_POP_REWARD            = 20
ALIEN_SKULL_POP_REWARD              = 10

ALIEN_SPEED                         = 10

ALIEN_POP_SPRITES                   = [Sprite("textures/pop.png", 48, 48)]
ALIEN_POP_WIDTH                     = 39
ALIEN_POP_HEIGHT                    = 39

ALIEN_POP_COLOR                     = (0, 255, 0)

ALIEN_POP_DURATION                  = 250

# [UFO]
ALIEN_UFO_SPRITES                   = [Sprite("textures/ufo.png", 48, 48)]

ALIEN_UFO_WIDTH                     = 48
ALIEN_UFO_HEIGHT                    = 48

ALIEN_UFO_COLOR                     = (0, 0, 127)

ALIEN_KIND_UFO                      = "ufo"

ALIEN_UFO_POP_REWARD                = 100

ALIEN_UFO_SPEED                     = 7

# [ALIEN STORM]
ALIEN_STORM_COLOR                   = (128, 0, 0)

ALIEN_STORM_CELL_WIDTH              = 48
ALIEN_STORM_CELL_HEIGHT             = 48
ALIEN_STORM_GAP                     = 0
ALIENS_ROWS                         = 5
ALIENS_PER_ROW                      = 11
ALIENS_BASE_MOVE_TIME_SPAN          = 1000

ALIEN_STORM_SPAWN_POS_X             = MAP_LEFT_BOUND
ALIEN_STORM_SPAWN_POS_Y             = MAP_TOP_BOUND + ALIEN_STORM_CELL_HEIGHT * 2

# [PROJECTILES]
PROJECTILE_PEW_SPRITES              = [Sprite("textures/pew.png", 48, 48)]
PROJECTILE_HAMMER_SPRITES           = [Sprite("textures/hammer_1.png", 48, 48), Sprite("textures/hammer_2.png", 48, 48)]
PROJECTILE_LIGHTNING_SPRITES        = [Sprite("textures/lightning_1.png", 48, 48), Sprite("textures/lightning_2.png", 48, 48), Sprite("textures/lightning_3.png", 48, 48)]
PROJECTILE_SPRING_SPRITES           = [Sprite("textures/spring_1.png", 48, 48), Sprite("textures/spring_2.png", 48, 48), Sprite("textures/spring_3.png", 48, 48)]

PROJECTILE_PEW_WIDTH                = 8
PROJECTILE_PEW_HEIGHT               = 16
PROJECTILE_HAMMER_WIDTH             = 8
PROJECTILE_HAMMER_HEIGHT            = 16
PROJECTILE_LIGHTNING_WIDTH          = 8
PROJECTILE_LIGHTNING_HEIGHT         = 16
PROJECTILE_SPRING_WIDTH             = 8
PROJECTILE_SPRING_HEIGHT            = 16

PROJECTILE_COLOR                    = (255, 0, 0)

PROJECTILE_KIND_PEW                 = "pew"
PROJECTILE_KIND_HAMMER              = "hammer"
PROJECTILE_KIND_LIGHTNING           = "lightning"
PROJECTILE_KIND_SPRING              = "spring"

PROJECTILE_PEW_SPEED                = 7
PROJECTILE_HAMMER_SPEED             = 7
PROJECTILE_LIGHTNING_SPEED          = 7
PROJECTILE_SPRING_SPEED             = 7

PROJECTILE_ANIMATION_DURATION       = 50

PROJECTILE_CRASH_ROOF               = [Sprite("textures/crash_roof.png", 48, 48)]
PROJECTILE_CRASH_FLOOR              = [Sprite("textures/crash_floor.png", 48, 48)]

PROJECTILE_CRASH_ROOF_WIDTH         = 36
PROJECTILE_CRASH_ROOF_HEIGHT        = 36
PROJECTILE_CRASH_FLOOR_WIDTH        = 24
PROJECTILE_CRASH_FLOOR_HEIGHT       = 24

PROJECTILE_CRASH_COLOR              = (0, 255, 0)

PROJECTILE_CRASH_KIND_ROOF          = "roof"
PROJECTILE_CRASH_KIND_FLOOR         = "floor"

PROJECTILE_CRASH_DURATION           = 250

# [MOVE DIRECTIONS]
LEFT                                = "left"
RIGHT                               = "right"
UP                                  = "up"
DOWN                                = "down"

# [FONT]
FONT_SPRITE                         = Sprite("textures/font.png", 318 // 2, 318 // 2)

FONT_CHAR_WIDTH                     = 30 // 2
FONT_CHAR_HEIGHT                    = 42 // 2

FONT_CHAR_COLOR                     = (0, 139, 139)

FONT_TEXTURE_ATLAS                  = TextureAtlas(FONT_SPRITE, FONT_CHAR_WIDTH, FONT_CHAR_HEIGHT, 6 // 2)

FONT_CHAR_MAP                       = {
    'A': (0, 0), 'B': (1, 0), 'C': (2, 0), 'D': (3, 0), 'E': (4, 0), 'F': (5, 0), 'G': (6, 0), 'H': (7, 0), 'I': (8, 0), 
    'J': (0, 1), 'K': (1, 1), 'L': (2, 1), 'M': (3, 1), 'N': (4, 1), 'O': (5, 1), 'P': (6, 1), 'Q': (7, 1), 'R': (8, 1),
    'S': (0, 2), 'T': (1, 2), 'U': (2, 2), 'V': (3, 2), 'W': (4, 2), 'X': (5, 2), 'Y': (6, 2), 'Z': (7, 2), ' ': (8, 2),
    '1': (0, 3), '2': (1, 3), '3': (2, 3), '4': (3, 3), '5': (4, 3), '6': (5, 3), '7': (6, 3), '8': (7, 3), '9': (8, 3), 
    '0': (0, 4), '<': (1, 4), '>': (2, 4), '-': (3, 4), '*': (4, 4), '?': (5, 4), '=': (6, 4)
}

# [TEXT]
TEXT_CHARS_GAP                      = FONT_TEXTURE_ATLAS.textures_gap

SCORE1_LABEL_TEXT                   = "SCORE<1>"
HI_SCORE_LABEL_TEXT                 = "HI-SCORE"
SCORE2_LABEL_TEXT                   = "SCORE<2>"
SCORE1_TEXT                         = "0000"
HI_SCORE_TEXT                       = "0000"
SCORE2_TEXT                         = "0000"
CREDIT_TEXT                         = "CREDIT 00"
LIVES_LEFT_TEXT                     = "0"
GAME_OVER_TEXT                      = "GAME OVER"
PLAY_TEXT                           = "PLAY"
SPACE_INVADERS_TEXT                 = "SPACE INVADERS"
SCORE_TABLE_TEXT                    = "*SCORE ADVANCED TABLE*"
MYSTERY_POINTS_TEXT                 = "=? MYSTERY"
JELLYFISH_POINTS_TEXT               = "=30 POINTS"
ANDROID_POINTS_TEXT                 = "=20 POINTS"
SKULL_POINTS_TEXT                   = "=10 POINTS"

SCORE1_LABEL_TEXT_TOP_OFFSET        = 25
HI_SCORE_LABEL_TEXT_TOP_OFFSET      = 25
SCORE2_LABEL_TEXT_TOP_OFFSET        = 25

LIVES_LEFT_TEXT_TOP_OFFSET          = WINDOW_HEIGHT - 25 - FONT_CHAR_HEIGHT
CREDIT_TEXT_TOP_OFFSET              = WINDOW_HEIGHT - 25 - FONT_CHAR_HEIGHT

BOTTOM_LINE_WIDTH                   = MAP_RIGHT_BOUND - MAP_LEFT_BOUND
BOTTOM_LINE_HEIGHT                  = 5
BOTTOM_LINE_COLOR                   = (0, 255, 0)
BOTTOM_LINE_TOP_OFFSET              = LIVES_LEFT_TEXT_TOP_OFFSET - BOTTOM_LINE_HEIGHT - TEXT_CHARS_GAP
BOTTOM_LINE_LEFT_OFFSET             = MAP_LEFT_BOUND

GAME_OVER_TEXT_TOP_OFFSET           = MAP_TOP_BOUND + 100

SCORE_TABLE_TOP_OFFSET              = 0

GAME_OVER_TYPING_TIME_SPAN          = 200
SCORE_TABLE_TYPING_TIME_SPAN        = 100

# [DEBUG]
DEBUG_SHOW_RECTS                    = False