# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Drawing
LINE_WIDTH = 2
LINE_COLOR = "white"

# Player
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED_MAX = 200
PLAYER_ACCEL_MOVE = 1000

PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
SHOT_RADIUS = 5

PLAYER_LIVES = 3
PLAYER_INVINCIBILITY_TIMER_SEC = 3

# Asteroid
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# Font General
SMALL_FONT_SIZE = 20
REG_FONT_SIZE = 40
MED_FONT_SIZE = 60
LARGE_FONT_SIZE = 80

FONT_X = 30
FONT_SPACING = 30
FONT_Y_TOP = 30
FONT_COLOR = "white"

# Gameplay Font Coordinates
SCORE_DISP_COORDS = (FONT_X, FONT_Y_TOP)
LIVES_DISP_COORDS = (FONT_X, FONT_Y_TOP + FONT_SPACING)
INVINCIBILITY_DISP_COORDS = (FONT_X, FONT_Y_TOP + 2*FONT_SPACING)

# Box Information
SCREEN_INFO = {
    "Start": {
        "Start": ["Start", (200, 80), (0, -50), (35, -15)],
        "Controls": ["Controls", (200, 80), (0, 50), (15, -20)],
        "Help": ["Press ""ENTER/RETURN"" to confirm", (0,0), (0,0), (-220, -110)],
        "Help2": ["Press ""W/S"" to navigate", (0,0), (0,0), (-145, -140)]
    },
    "Pause": {
        "HelpNone": ["Pause", (0,0), (0,0), (0,0)],
        "Resume": ["Resume", (250, 80), (0, -50), (15, -15)],
        "Controls": ["Controls", (200, 80), (0, 50), (15, -20)]
    },
    "Controls": {
        "HelpNone": ["Controls", (0,0), (0,0), (0,0)],
        "Back": ["Back", (100, 50), (0, 25), (15, -15)],
        "Help": ["Press ""ENTER/RETURN"" to confirm", (0,0), (0,0), (-220, -110)]
    }
}

ARROW_OFFSET = 20
ARROW_LENGTH = 100
ARROW_POINT_LENGTH = 30
ARROW_POINT_HEIGHT = 20