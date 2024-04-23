import pyray


class Animation:
    def __init__(self, texture: pyray.Texture2D, num_frames: int, img_frame_dur: float = 5.0 / 60.0, loop: bool = True):
        self.texture = texture

        # Multiplying these two together will result in the total duration of the animation.
        self.num_frames = num_frames
        self.frame_width: float = self.texture.width / self.num_frames
        self.frame_duration = img_frame_dur

        self.frame: int = 0
        self.elapsed_time = 0.0
        self.frame_rect: pyray.Rectangle = pyray.Rectangle(0.0, 0.0, self.frame_width, self.texture.height)

        self.loop = loop
        self.done: bool = False

    # def copy(self):
    #     return Animation(self.texture, self.num_frames, self.frame_duration, self.loop)

    def update(self, dt: float):
        # Note: This update function should be called once per frame so this animation will be
        # dependent on the framerate.
        self.elapsed_time += dt
        if self.elapsed_time >= self.frame_duration:
            self.frame += 1
            self.elapsed_time -= self.frame_duration

        if self.loop:
            self.frame = self.frame % self.num_frames
        elif self.frame > self.num_frames:
            self.frame = self.num_frames - 1
            self.done = True

        self.frame_rect.x = self.frame * self.frame_width
