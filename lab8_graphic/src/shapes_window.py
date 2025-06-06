import moderngl
from pyrr import Matrix44, Vector3

import models
from base_window import BaseWindow

from math import radians

class ShapesWindow(BaseWindow):

    def __init__(self, **kwargs):
        super(ShapesWindow, self).__init__(**kwargs)

    def load_models(self):
        self.cube_3d = models.load_cube(self.program)
        self.cone_3d = models.load_cone(self.program)
        self.roller_3d = models.load_roller(self.program)

    def init_shaders_variables(self):
        self.uniform_projection = self.program["projection"]
        self.uniform_view = self.program["view"]
        self.uniform_camera_position = self.program["camera_position"]
        self.uniform_model = self.program["model"]
        self.uniform_material_diffuse = self.program["material_diffuse"]
        self.uniform_material_ambient = self.program["material_ambient"]
        self.uniform_material_shininess = self.program["material_shininess"]
        self.uniform_material_specular = self.program["material_specular"]

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.1, 0.2, 0.3, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)
        eye = (5.0, 5.0, -15.0)

        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        view = Matrix44.look_at(
            eye,
            (0.0, 2.0, 0.0),
            (0.0, 1.0, 0.0),
        )

        # look at (paramater eye) (5.0, 5.0, -15.0) it t means that the camera is from back of the robot

        self.uniform_projection.write(projection.astype('f4'))
        self.uniform_view.write(view.astype('f4'))
        self.uniform_camera_position.write(Vector3(eye).astype('f4'))
        self.uniform_material_specular.write(Vector3((0.4, 0.4, 0.4)).astype('f'))  # Specular value for all materials
        self.uniform_material_shininess.value = 10  # Shininess value for all materials 

        # Head
        material_diffuse = (0.8, 0.8, 0.2)
        material_ambient = tuple(0.2 * x for x in material_diffuse)
        self.uniform_material_diffuse.write(Vector3(material_diffuse).astype('f'))
        self.uniform_material_ambient.write(Vector3(material_ambient).astype('f'))
        model_rotation = Matrix44.from_x_rotation(radians(0))

        model_translation = Matrix44.from_translation((0, 5.5, 0))
        model_scale = Matrix44.from_scale((1, 1, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cone_3d.render(moderngl.TRIANGLES)

        # Body
        material_diffuse = (0.2, 0.6, 1.0)
        material_ambient = tuple(0.2 * x for x in material_diffuse)
        self.uniform_material_diffuse.write(Vector3(material_diffuse).astype('f'))
        self.uniform_material_ambient.write(Vector3(material_ambient).astype('f'))

        model_translation = Matrix44.from_translation((0, 2, 0))
        model_rotation = Matrix44.from_z_rotation(radians(0))
        model_scale = Matrix44.from_scale((1.2, 2.2, 1.2))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.roller_3d.render(moderngl.TRIANGLES)
        
        # Right Arm
        material_diffuse = (0.3, 0.8, 0.6)
        material_ambient = tuple(0.2 * x for x in material_diffuse)
        self.uniform_material_diffuse.write(Vector3(material_diffuse).astype('f'))
        self.uniform_material_ambient.write(Vector3(material_ambient).astype('f'))

        model_translation = Matrix44.from_translation((2.5, 4, 0))
        model_rotation = Matrix44.from_z_rotation(radians(45))
        model_scale = Matrix44.from_scale((1, 2.5, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)

        # Left Arm
        material_diffuse = (0.3, 0.8, 0.6)
        material_ambient = tuple(0.2 * x for x in material_diffuse)
        self.uniform_material_diffuse.write(Vector3(material_diffuse).astype('f'))
        self.uniform_material_ambient.write(Vector3(material_ambient).astype('f'))

        model_translation = Matrix44.from_translation((-2.5, 2, 0))
        model_rotation = Matrix44.from_z_rotation(radians(-150))
        model_scale = Matrix44.from_scale((1, 2.5, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)

        # Right Leg
        material_diffuse = (0.7, 0.1, 0.1)
        material_ambient = tuple(0.2 * x for x in material_diffuse)
        self.uniform_material_diffuse.write(Vector3(material_diffuse).astype('f'))
        self.uniform_material_ambient.write(Vector3(material_ambient).astype('f'))

        model_translation = Matrix44.from_translation((2, -2, 0))
        model_rotation = Matrix44.from_z_rotation(radians(-30))
        model_scale = Matrix44.from_scale((1, 3, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)

        # Left Leg
        material_diffuse = (0.7, 0.1, 0.1)
        material_ambient = tuple(0.2 * x for x in material_diffuse)
        self.uniform_material_diffuse.write(Vector3(material_diffuse).astype('f'))
        self.uniform_material_ambient.write(Vector3(material_ambient).astype('f'))

        model_translation = Matrix44.from_translation((-2, -2, 0))
        model_rotation = Matrix44.from_z_rotation(radians(30))
        model_scale = Matrix44.from_scale((1, 3, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)
