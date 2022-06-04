from scene_base import SceneBase


class Light(SceneBase):
    # TODO: Implement constructor
    def __init__(self, center, intensity):
        self.center = center
        self.intensity = intensity

    # TODO: Implement __str__
    def __str__(self):
        return f"Center: {self.center}, Intensity: {self.intensity}"

    # TODO: Implement to_json

    # TODO: Implement __eq__

    pass
