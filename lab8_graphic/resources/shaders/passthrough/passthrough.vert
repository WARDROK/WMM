#version 330

in vec2 in_position;

out vec2 varColor;

void main()
{
    varColor = in_position;
    gl_Position = vec4(in_position + vec2(-0.2, 0.5), 0.0, 1.0);
}