import math
from PIL import Image, ImageDraw, ImageOps, ImageEnhance


class ImageProcessing():


    ###########################
    ###                     ###
    ###     I/O + Basics    ###
    ###                     ###
    ###########################


    def open_image(self, path):
        img = Image.open(path)
        return img


    def export_image(self, img, path):
        img.save(path, quality=100)
        print("Export : {}".format(path))


    def create_canvas(self, canvas_size_x, canvas_size_y):
        pass
        # new = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
        # return new


    def create_canvas_square(self, canvas_size):
        new = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
        return new


    def paste_alpha(self, img0, img1, offset):
        
        c = Image.new('RGBA', img0.size, (0, 0, 0, 0))
        c.paste(img1, offset)

        img_alpha = Image.alpha_composite(img0, c)

        return img_alpha


    def rotate_image(self, img, angle):

        img_rot = img.rotate(angle, resample = Image.BICUBIC)
        return img_rot


    def change_scale(self, img, target_size_x, target_size_y):
        pass
        # img_resize = img.resize((target_size, target_size), Image.LANCZOS)
        # return img_resize


    def change_scale_square(self, img, target_size):
        img_resize = img.resize((target_size, target_size), Image.LANCZOS)
        return img_resize


    def mirror_image(self, img):
        
        img_mirror = ImageOps.mirror(img)
        return img_mirror


    def replace_pixel_color(self, src_r, src_g, src_b, new_r, new_g, new_b):
        pass
        # r, g, b, a = img.split()
        # img_new = Image.merge("RGBA", (r, r, b, a))
        # return img_new
