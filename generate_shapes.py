"""
Running this script will create arrays of images
Which can then be used as "Textures" in Grease Pencil materials
Each array features varying sizes of shapes
Currently there are Disc, Squares and Stripes.
"""

import bpy


def generate_img_shape(size, name, is_in_shape):
    image = bpy.data.images.get(name)
    if image is None:
        image = bpy.data.images.new(name, width=size[0], height=size[1])
    else:
        image.generated_width = size[0]
        image.generated_height = size[1]

    pixels = [None] * (size[0] * size[1])

    for x in range(size[0]):
        for y in range(size[1]):
            pixels[(y * size[0]) + x] = is_in_shape(x, y)

    pixels = [v for v in pixels for _ in range(4)]

    image.pixels = pixels

if __name__ == "__main__":    
    size = 150, 150  
    middle_x = size[0] / 2
    middle_y = size[1] / 2
    
    for rad, rad_size in zip((0.1, 0.2, 0.3, 0.4, 0.49), ("10", "20", "30", "40", "50")):
        radius_squared = (rad * min(size[0], size[1])) ** 2
        generate_img_shape(size, "GP_HATCH_DISC_" + rad_size, lambda x, y: int(((x - middle_x) ** 2 + (y - middle_y) ** 2) < radius_squared))
        
        generate_img_shape(
            size, 
            "GP_HATCH_SQUARE_" + rad_size, 
            lambda x, y: 
                int(
                    (x - middle_x) ** 2 < radius_squared and
                    (y - middle_y) ** 2 < radius_squared                
                )
        )
        
        generate_img_shape(
            size,
            "GP_HATCH_BAND_" + rad_size,
            lambda x, y:
                int(
                    (x - middle_x) ** 2 < radius_squared          
                )
        )
    
    