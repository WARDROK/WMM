#version 330

out vec4 f_color;

uniform vec3 color;

in vec2 varColor;

void main()
{
    // f_color = vec4(0.0, 0.0, 1.0, 0.0);
    f_color = vec4(abs(varColor * 2.0), color.z, 1.0);
}
