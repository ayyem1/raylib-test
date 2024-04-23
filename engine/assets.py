from typing import Self

from raylib import LoadTexture

from engine.animations import Animation


class AssetDatabase:
    """
    This class is responbile for holding all assets for your game.
    The internal structure is a dictionary of key to a list of assets.
    In the future, this will need to be cleaned up to use an Asset class,
    but for now this will do.

    If the asset is not part of an animation, the list will have only 1 item
    """

    _instance: Self | None = None
    _assets = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def add_animation_asset(
        self, key: str, path: str, num_frames: int, img_frame_duration: float = 5.0 / 60.0, loop: bool = True
    ):
        if key in self._assets:
            print(f"Key already exists in asset database. key={key}")
            return

        self._assets[key] = Animation(
            LoadTexture(path), num_frames=num_frames, img_frame_dur=img_frame_duration, loop=loop
        )

    def get_asset(self, key: str):
        return self._assets[key]
