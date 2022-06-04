from scene_base import SceneBase


class Sphere(SceneBase):
    # TODO: Implement constructor
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    # TODO: Implement __str__
    def __str__(self):
        return f"Center: {self.center}, Radius: {self.radius}, Material: {self.material}"

    # TODO: Implement to_json

    # TODO: Implement __eq__

    pass
