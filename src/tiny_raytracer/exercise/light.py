from scene_base import SceneBase


class Light(SceneBase):
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

    def __str__(self):
        return f"Center: {self.position}, Intensity: {self.intensity}"

    # TODO: Implement to_json

    # TODO: Implement __eq__

    pass
