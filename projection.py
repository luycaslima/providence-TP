import math
import bpy

def calculate_cam_projection(cameras, tex_width,text_height):

    cam_pos = cameras[0].matrix_world
    #fov_y = 2.0 * math.tan( cameras[0].angle_y / 2.0 )
    print(cam_pos)
    