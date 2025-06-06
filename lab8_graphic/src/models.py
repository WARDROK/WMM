import numpy
from moderngl_window.opengl.vao import VAO
import math

def load_quad_2D(program):
    size = 1.0
    unit = size / 2.0

    positions = []

    positions.append([-unit, unit])
    positions.append([-unit, -unit])
    positions.append([unit, -unit])
    positions.append([-unit, unit])
    positions.append([unit, -unit])
    positions.append([unit, unit])

    positions = numpy.array(positions, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "2f", ["in_position"])

    return vao.instance(program)


def load_cube(program):
    size = 1.0
    unit = size / 2.0

    positions = []
    # Front face
    positions.append([unit, unit, unit])
    positions.append([-unit, unit, unit])
    positions.append([-unit, -unit, unit])
    positions.append([-unit, -unit, unit])
    positions.append([unit, -unit, unit])
    positions.append([unit, unit, unit])
    # Back face
    positions.append([unit, -unit, -unit])
    positions.append([-unit, -unit, -unit])
    positions.append([-unit, unit, -unit])
    positions.append([-unit, unit, -unit])
    positions.append([unit, unit, -unit])
    positions.append([unit, -unit, -unit])
    # Top face
    positions.append([unit, unit, -unit])
    positions.append([-unit, unit, -unit])
    positions.append([-unit, unit, unit])
    positions.append([-unit, unit, unit])
    positions.append([unit, unit, unit])
    positions.append([unit, unit, -unit])
    # Bottom face
    positions.append([unit, -unit, unit])
    positions.append([-unit, -unit, unit])
    positions.append([-unit, -unit, -unit])
    positions.append([-unit, -unit, -unit])
    positions.append([unit, -unit, -unit])
    positions.append([unit, -unit, unit])
    # Left face
    positions.append([-unit, unit, unit])
    positions.append([-unit, unit, -unit])
    positions.append([-unit, -unit, -unit])
    positions.append([-unit, -unit, -unit])
    positions.append([-unit, -unit, unit])
    positions.append([-unit, unit, unit])
    # Right face
    positions.append([unit, unit, -unit])
    positions.append([unit, unit, unit])
    positions.append([unit, -unit, unit])
    positions.append([unit, -unit, unit])
    positions.append([unit, -unit, -unit])
    positions.append([unit, unit, -unit])

    normals = generate_normals(positions)

    positions = numpy.array(positions, dtype=numpy.float32).flatten()
    normals = numpy.array(normals, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "3f", ["in_position"])
    vao.buffer(normals, "3f", ["in_normal"])
    return vao.instance(program)

def load_cone(program):
    size = 1
    points = []
    positions = []
    circleCenter = [0.0, 0.0]  
    radius = 1.0
    segments = 50


    for segment in range(segments):
        theta0 = 2.0 * math.pi * segment / segments
        theta1 = 2.0 * math.pi * ((segment + 1) % segments) / segments

        X0 = circleCenter[0] + radius * math.cos(theta0)
        Y0 = circleCenter[1] + radius * math.sin(theta0)
        X1 = circleCenter[0] + radius * math.cos(theta1)
        Y1 = circleCenter[1] + radius * math.sin(theta1)

        points.append(circleCenter)
        points.append([X1, Y1])
        points.append([X0, Y0])


    for i in range(0, len(points), 3):
        cx, cz   = points[i]   
        x0, z0   = points[i + 1] 
        x1, z1   = points[i + 2] 

        y_base = -size


        positions.append([cx,  y_base, cz])
        positions.append([x1,  y_base, z1])
        positions.append([x0,  y_base, z0])


    for segment in range(segments):
        theta0 = 2.0 * math.pi * segment / segments
        theta1 = 2.0 * math.pi * ((segment + 1) % segments) / segments

        x0 = circleCenter[0] + radius * math.cos(theta0)
        z0 = circleCenter[1] + radius * math.sin(theta0)
        x1 = circleCenter[0] + radius * math.cos(theta1)
        z1 = circleCenter[1] + radius * math.sin(theta1)

        y_base = -size
        y_apex = +size


        positions.append([0.0,    y_apex, 0.0]) 
        positions.append([x0,     y_base, z0])  
        positions.append([x1,     y_base, z1])  


    normals = generate_normals(positions)


    positions = numpy.array(positions, dtype=numpy.float32).flatten()
    normals = numpy.array(normals, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "3f", ["in_position"])
    vao.buffer(normals,   "3f", ["in_normal"])
    return vao.instance(program)

def load_roller(program):
    size = 1
    points = []

    positions = []
    circleCenter = [0.0, 0.0]   
    radius = 1.0
    segments = 40


    for segment in range(segments):

        theta0 = 2.0 * math.pi * segment / segments
        theta1 = 2.0 * math.pi * ((segment + 1) % segments) / segments

        X0 = circleCenter[0] + radius * math.cos(theta0)
        Y0 = circleCenter[1] + radius * math.sin(theta0)
        X1 = circleCenter[0] + radius * math.cos(theta1)
        Y1 = circleCenter[1] + radius * math.sin(theta1)

 
        points.append(circleCenter)
        points.append([X1, Y1])
        points.append([X0, Y0])


    for i in range(0, len(points), 3):
        cx, cz   = points[i]     
        x0, z0   = points[i + 1] 
        x1, z1   = points[i + 2] 

        y_cap = +size 


        positions.append([cx,  y_cap, cz])
        positions.append([x1,  y_cap, z1])
        positions.append([x0,  y_cap, z0])

 
    for i in range(0, len(points), 3):
        cx2, cz2 = points[i]    
        xb0, zb0 = points[i + 1] 
        xb1, zb1 = points[i + 2] 

        y_bot = -size 

        positions.append([cx2,  y_bot, cz2])
        positions.append([xb1,  y_bot, zb1])
        positions.append([xb0,  y_bot, zb0])


    for segment in range(segments):
        theta0 = 2.0 * math.pi * segment / segments
        theta1 = 2.0 * math.pi * ((segment + 1) % segments) / segments

        x0 = circleCenter[0] + radius * math.cos(theta0)
        z0 = circleCenter[1] + radius * math.sin(theta0)
        x1 = circleCenter[0] + radius * math.cos(theta1)
        z1 = circleCenter[1] + radius * math.sin(theta1)

        yt = +size
        yb = -size


        positions.append([x0, yt, z0]) 
        positions.append([x1, yb, z1])  
        positions.append([x0, yb, z0])  

        positions.append([x0, yt, z0])  
        positions.append([x1, yt, z1]) 
        positions.append([x1, yb, z1])   


    normals = generate_normals(positions)


    vertices = []
    for i in range(len(positions)):
        px, py, pz = positions[i]
        nx, ny, nz = normals[i]
        vertices += [px, py, pz,   nx, ny, nz]

    normals = generate_normals(positions)
    positions = numpy.array(positions, dtype=numpy.float32).flatten()
    normals = numpy.array(normals, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "3f", ["in_position"])
    vao.buffer(normals, "3f", ["in_normal"])
    return vao.instance(program)


def generate_normals(positions):
    N = len(positions)
    normals = []
    for i in range(0, N, 3):
        p0 = numpy.array(positions[i + 0])
        p1 = numpy.array(positions[i + 1])
        p2 = numpy.array(positions[i + 2])
        cross = numpy.cross(p1 - p0, p2 - p0)
        norm = cross / numpy.linalg.norm(cross)
        for v in range(3):
            normals.append(list(norm))
    return normals