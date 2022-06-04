from scene_base import SceneBase


class Material(SceneBase):
    # TODO: Implement constructor
    def __init__(self, name, refractive_index, albedo, diffuse_color, specular_exponent):
        self.name = name
        self.refractive_index = refractive_index
        self.albedo = albedo
        self.diffuse_color = diffuse_color
        self.specular_exponent = specular_exponent

    # TODO: Implement __str__
    def __str__(self):
        return f"Name: {self.name}, Refractive Index: {self.refractive_index}, Albedo: {self.albedo}, Diffuse Color: {self.diffuse_color}, Specular Exponent: {self.specular_exponent}"

    # TODO: Implement to_json

    pass
