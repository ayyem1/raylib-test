import pyray

from engine.assets import AssetDatabase


class Player:
    MOVE_RIGHT: str = "player_right"
    MOVE_LEFT: str = "player_left"
    MOVE_UP: str = "player_up"
    MOVE_DOWN: str = "player_down"

    def __init__(self, pos: pyray.Vector2) -> None:
        self.action: str = ""
        # TODO: We should have an idle state
        self.set_action(self.MOVE_DOWN)

        self.position = pos

        self.direction = pyray.Vector2(0.0, 0.0)
        self.speed: float = 200.0

    def set_action(self, action: str):
        if action != self.action:
            self.action = action
            self.animation = AssetDatabase().get_asset(action).copy()

    def update(self, dt: float):
        self.handle_input()
        self.handle_movement(dt=dt)
        self.animation.update()

    def handle_input(self):
        # We convert the boolean sotred in keys to an int (0 or 1) to
        # determine the direction
        self.direction.x = pyray.is_key_down(pyray.KEY_RIGHT) - pyray.is_key_down(pyray.KEY_LEFT)
        self.direction.y = pyray.is_key_down(pyray.KEY_DOWN) - pyray.is_key_down(pyray.KEY_UP)

        if pyray.vector2_length_sqr(self.direction) > 0:
            self.direction = pyray.vector2_normalize(self.direction)

        if self.direction.y > 0:
            self.set_action(self.MOVE_DOWN)
        elif self.direction.y < 0:
            self.set_action(self.MOVE_UP)
        elif self.direction.x > 0:
            self.set_action(self.MOVE_RIGHT)
        elif self.direction.x < 0:
            self.set_action(self.MOVE_LEFT)

    def handle_movement(self, dt: float):
        self.position.x += self.direction.x * self.speed * dt
        self.position.y += self.direction.y * self.speed * dt
