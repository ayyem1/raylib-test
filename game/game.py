"""

Handles game loop.

"""

import pyray
from raylib import DrawTextureRec

from engine.assets import AssetDatabase
from game import settings
from game.player import Player


class Game:
    def __init__(self) -> None:
        pyray.init_window(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, settings.GAME_NAME)
        # pyray.set_target_fps(60)

        AssetDatabase().add_animation_asset("player_right", b"data/graphics/player/right.png", 4)
        AssetDatabase().add_animation_asset("player_left", b"data/graphics/player/left.png", 4)
        AssetDatabase().add_animation_asset("player_up", b"data/graphics/player/up.png", 4)
        AssetDatabase().add_animation_asset("player_down", b"data/graphics/player/down.png", 4)

        self.player = Player(pyray.Vector2(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2))

    def run(self) -> None:
        # Main game loop
        while not pyray.window_should_close():  # Detect window close button or ESC key
            dt: float = pyray.get_frame_time()
            # Update
            self.player.update(dt=dt)

            # Draw
            pyray.begin_drawing()

            DrawTextureRec(
                self.player.animation.texture, self.player.animation.frame_rect, self.player.position, pyray.WHITE
            )
            pyray.clear_background(pyray.BLACK)
            pyray.draw_fps(2, 2)

            pyray.end_drawing()

        # De-Initialization
        pyray.close_window()  # Close window and OpenGL context
