from stratasys_working import image_processing

im = image_processing.ImageProcessing()


#####


prj_path = "_images_\\200409_Sphere\\"
src_path = prj_path + "out_fix\\"
new_path = prj_path + "images_0\\"


file_count = 2422
init_count = 0

### Change Layer Height
### 0.014mm >> 0.027mm

for i in range(file_count):
    
    if i%2 == 0:
        
        ### Format
        index_src = "%04d"%(int(i))
        index_new = "%04d"%(int(init_count))

        path_src = src_path + "slice_{}.png".format(index_src)
        path_new = new_path + "image_{}.png".format(index_new)

        image_src = im.open_image(path_src)
        
        im.export_image(image_src, path_new)

        init_count += 1