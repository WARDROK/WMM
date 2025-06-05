import moderngl
from pyrr import Matrix44, Vector3

import models
from base_window import BaseWindow

from math import radians

class RobotWindow(BaseWindow):

    def __init__(self, **kwargs):
        super(RobotWindow, self).__init__(**kwargs)

    def load_models(self):
        self.cube_3d = models.load_cube(self.program)

    def init_shaders_variables(self):
        self.uniform_projection = self.program["projection"]
        self.uniform_view = self.program["view"]
        self.uniform_model = self.program["model"]
        self.uniform_color = self.program["color"]

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.2, 0.2, 0.2, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        view = Matrix44.look_at(
            (5.0, 5.0, -15.0),
            (0.0, 2.0, 0.0),
            (0.0, 1.0, 0.0),
        )
        self.uniform_projection.write(projection.astype('f4'))
        self.uniform_view.write(view.astype('f4'))

        # Head
        self.uniform_color.write(Vector3((0.8, 0.8, 0.2)).astype('f'))

        model_translation = Matrix44.from_translation((0, 5, 0))
        model_scale = Matrix44.from_scale((1.5, 1.5, 1.5))
        model = model_translation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)

        # Body
        self.uniform_color.write(Vector3((0.2, 0.6, 1.0)).astype('f'))

        model_translation = Matrix44.from_translation((0, 2, 0))
        model_scale = Matrix44.from_scale((2, 4, 2))
        model = model_translation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)

        # look at ((5.0, 5.0, -15.0)) it t means that the camera is from back of the robot
        
        # Right Arm
        self.uniform_color.write(Vector3((0.3, 0.8, 0.6)).astype('f'))

        model_translation = Matrix44.from_translation((2.5, 4, 0))
        model_rotation = Matrix44.from_z_rotation(radians(45))
        model_scale = Matrix44.from_scale((1, 2.5, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)

        # Left Arm
        self.uniform_color.write(Vector3((0.3, 0.8, 0.6)).astype('f'))

        model_translation = Matrix44.from_translation((-2.5, 2, 0))
        model_rotation = Matrix44.from_z_rotation(radians(-150))
        model_scale = Matrix44.from_scale((1, 2.5, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)

        # Right Leg
        self.uniform_color.write(Vector3((0.7, 0.1, 0.1)).astype('f'))

        model_translation = Matrix44.from_translation((2, -2, 0))
        model_rotation = Matrix44.from_z_rotation(radians(-30))
        model_scale = Matrix44.from_scale((1, 3, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)

        # Left Leg
        self.uniform_color.write(Vector3((0.7, 0.1, 0.1)).astype('f'))

        model_translation = Matrix44.from_translation((-2, -2, 0))
        model_rotation = Matrix44.from_z_rotation(radians(30))
        model_scale = Matrix44.from_scale((1, 3, 1))
        model = model_translation * model_rotation * model_scale
        self.uniform_model.write(model.astype('f4'))

        self.cube_3d.render(moderngl.TRIANGLES)