from stratasys_working import image_processing

im = image_processing.ImageProcessing()


#####


prj_path = "_images_\\200409_Sphere\\"
dir_0 = prj_path + "images_0\\"
dir_1 = prj_path + "images_1\\"


file_count = 1211

### Change Scale
### 800 x 400 >>> 400 x 400

for i in range(file_count):

    ### Format
    index = "%04d"%(int(i))

    path_0 = dir_0 + "image_{}.png".format(index)
    path_1 = dir_1 + "image_{}.png".format(index)

    image_0 = im.open_image(path_0)
    image_0_resize = im.change_scale(image_0, 400, 400)

    im.export_image(image_0_resize, path_1)

