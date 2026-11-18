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
TITLE_FONT_SIZE = 150

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
        "HelpTitle": ["ASTEROIDS", (0,0), (0,0), (-310, -250)],
        "Start": ["Start", (200, 80), (0, -50), (35, 15)],
        "Controls": ["Controls", (200, 80), (0, 50), (15, 20)],
        "Help": ["Press ""ENTER/RETURN"" to confirm", (0,0), (0,0), (-220, 110)],
        "Help2": ["Press ""W/S"" to navigate", (0,0), (0,0), (-145, 140)]
    },
    "Pause": {
        "HelpNone": ["Pause", (0,0), (0,0), (0,0)],
        "HelpTitle": ["PAUSED", (0,0), (0,0), (-200, -250)],
        "Resume": ["Resume", (250, 80), (0, -50), (15, 15)],
        "Controls": ["Controls", (200, 80), (0, 50), (15, 20)]
    },
    "Controls": {
        "HelpNone": ["Controls", (0,0), (0,0), (0,0)],
        "HelpTitle": ["CONTROLS", (0,0), (0,0), (-310, -350)],
        "Back": ["Back", (150, 80), (0, 300), (10, 15)],

        "DrawHelpSettingsKeybinds": ["Settings Navigation", (0,0), (0,0), (-200, -250)],
        "DrawHelpConfirm": ["Confirm Input", (0,0), (0,0), (-325, -200)],
        "DrawHelpConfirmKey": ["ENTER/RETURN", (0,0), (0,0), (125, -200)],
        "DrawHelpNavigate": ["Navigate Selectable Options", (0,0), (0,0), (-325, -150)],
        "DrawHelpNavigateKey": ["W/S", (0,0), (0,0), (125, -150)],
        "DrawHelpPause": ["Pause Game", (0,0), (0,0), (-325, -100)],
        "DrawHelpPauseKey": ["P", (0,0), (0,0), (125, -100)],

        "DrawHelpGameplayKeybinds": ["Gameplay Keybinds", (0,0), (0,0), (-200, -50)],
        "DrawHelpMoveForward": ["Move Forward", (0,0), (0,0), (-325, 0)],
        "DrawHelpMoveForwardKey": ["W", (0,0), (0,0), (125, 0)],
        "DrawHelpMoveBackward": ["Move Backward", (0,0), (0,0), (-325, 50)],
        "DrawHelpMoveBackwardKey": ["S", (0,0), (0,0), (125, 50)],
        "DrawHelpRotateCW": ["Rotate Clockwise", (0,0), (0,0), (-325, 100)],
        "DrawHelpRotateCWKey": ["D", (0,0), (0,0), (125, 100)],
        "DrawHelpRotateCCW": ["Rotate Counterclockwise", (0,0), (0,0), (-325, 150)],
        "DrawHelpRotateCCWKey": ["A", (0,0), (0,0), (125, 150)]
    }
}

ARROW_OFFSET = 20
ARROW_LENGTH = 100
ARROW_POINT_LENGTH = 30
ARROW_POINT_HEIGHT = 20