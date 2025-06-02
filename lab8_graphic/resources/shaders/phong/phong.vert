#version 330

in vec3 in_position;
in vec3 in_normal;

out vec3 v_position;
out vec3 v_normal;

void main()
{

	//v_position = (M * vec4(in_position, 1.0)).xyz;
	//v_normal = (M * vec4(in_normal, 0.0)).xyz;
	
	// TODO: Write transformation part
    //gl_Position = ...
}