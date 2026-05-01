import os

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
FPS = 60

TOP_PANEL = 60
COLS = WIDTH // CELL_SIZE
ROWS = (HEIGHT - TOP_PANEL) // CELL_SIZE

BASE_SPEED = 8
LEVEL_UP_EVERY = 5
OBSTACLES_PER_LEVEL = 4

IMAGE_DIR = os.path.join(os.path.dirname(__file__), "images")
SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.json")

IMAGE_FILES = {
    "food": "food.png",
    "poison": "poison.png",
    "speed": "speed.png",
    "slow": "slow.png",
    "shield": "shield.png",
    "snake_head": "snake_head.png",
    "snake_body": "snake_body.png",
    "obstacle": "obstacle.png",
    "background": "background.png"
}

DB_CONFIG = {
    "host": "localhost",
    "database": "snake_db",
    "user": "postgres",
    "password": "postgres",
    "port": 5432,
}