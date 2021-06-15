from PIL import Image, ImageTk
import os

def img_resize(img, size):
    #print("img_resize here")
    pic        = Image.open(img)
    resize_pic = pic.resize(size, Image.ANTIALIAS)
    resize_pic.save(img)



def image_process():
    image = Image.open("image/chess_pattern_orig.jpg")
    default_size_num = image.size


    string_dir = 'image/'
    extensions = [".jpg"]
    file_list  = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]

    path2file  = [string_dir + element for element in file_list]


    print(path2file)

    max_size = (992,992)

    for element in path2file:
        image = Image.open(element)
        size_num = image.size

        print("defore resize: ", size_num)

        if size_num != max_size:
            img_resize(element,default_size_num)

        else:
            pass


        image = Image.open(element)
        size_num = image.size

        print("after resize: ", size_num)





if __name__ == '__main__':
    image_process()