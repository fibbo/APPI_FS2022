from scene_base import SceneBase


class Scene(SceneBase):
    # TODO: Implement constructor
    def __init__(self, lights, spheres):
        self.lights = lights
        self.spheres = spheres

    # TODO: Implement __getitem__
    def __getitem__(self, name):
        if name == "lights":
            return self.lights
        if name == "spheres":
            return self.spheres

    # TODO: Implement __str__
    def __str__(self):
        info = ""
        for light in self.lights:
            info += light.__str__()
        
        for sphere in self.spheres:
            info += sphere.__str__()
        return info

    # TODO: Implement to_json

    # TODO: Implement from_json
    pass
