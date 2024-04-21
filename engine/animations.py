import pyray


class Animation:
    def __init__(self, texture: pyray.Texture2D, num_frames: int, img_frame_dur: float = 5, loop: bool = True):
        self.texture = texture

        # Multiplying these two together will result in the total duration of the animation.
        self.num_frames = num_frames
        self.img_frame_duration = img_frame_dur

        self.frame: float = 0.0
        self.frame_rect: pyray.Rectangle = pyray.Rectangle(
            0.0, 0.0, self.texture.width / num_frames, self.texture.height
        )

        self.loop = loop
        self.done: bool = False

    def copy(self):
        return Animation(self.texture, self.num_frames, self.img_frame_duration, self.loop)

    def update(self):
        # Note: This update function should be called once per frame so this animation will be
        # dependent on the framerate.
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_frame_duration * self.num_frames)
        else:
            self.frame = (self.frame + 1) % self.img_frame_duration * self.num_frames - 1
            self.done = True

        self.frame_rect.x = (self.frame // self.img_frame_duration) * (self.texture.width / self.num_frames)
