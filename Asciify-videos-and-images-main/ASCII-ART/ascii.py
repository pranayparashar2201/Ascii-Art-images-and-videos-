from doctest import FAIL_FAST
import cv2
#import imgkit
import os
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont
if not os.path.exists('output'):
    os.mkdir("output")
if not os.path.exists('outputvideo'):
    os.mkdir("outputvideo")
Character = {
    #"standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}
inp= input("ENTER FILE NAME: ")
lengt= len(inp)
check=True
if inp.find('.mp4')==-1:
    check = False
def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale

def convert_frames_to_video(input_list,output_file_name,fps,size):
    out = cv2.VideoWriter(output_file_name,fourcc,fps,size)
    num_frames =len(input_list)
    for i in range(num_frames):
        base_name='output'
        img_name= base_name + '{:01d}'.format(i)+'.jpg'
        img_path=os.path.join(input_frame_path,img_name)
        img = cv2.imread(img_path)
        out.write(img)
        if img is not None:
           cv2.imshow('img',img)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
           break
    
    out.release()
    shutil.rmtree('output')
    cv2.destroyAllWindows()


bg = "black"
# bg = "black"
if bg == "white":
    bg_code = (255,255,255)
elif bg == "black":
    bg_code = (0,0,0)

char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 400
#for video
if check ==True:
    vidObj = cv2.VideoCapture("./data/"+inp)
    count =0
    frame_width=0
    frame_height=0
    while (True) :
        success , image = vidObj.read()
        #if count ==6:
        #    break
        if success== False:
            break
        if (True):
        
            height, width, _ = image.shape
            frame_height=height
            frame_width=width
            cell_w = width / num_cols
            cell_h = scale * cell_w
            num_rows = int(height / cell_h)

            char_width, char_height = font.getsize("A")
            out_width = char_width * num_cols
            out_height = scale * char_height * num_rows
       

            out_image = Image.new("RGB", (out_width, out_height), bg_code)
            draw = ImageDraw.Draw(out_image)
        


            for i in range(num_rows):
                for j in range(num_cols):
                    partial_image= image[int(i*cell_h):min(int((i+1)*cell_h),height),int(j*cell_w):min(int((j+1)*cell_w),width),:]
                    partial_avg_color = np.sum(np.sum(partial_image,axis=0),axis=0)/(cell_h*cell_w)
                    partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist()) 
                    c = char_list[min(int(np.mean(partial_image)*num_chars/255),num_chars-1)]
                    draw.text((j*char_width,i*char_height),c,fill = partial_avg_color, font= font)


            if bg == "white":
                cropped_image = ImageOps.invert(out_image).getbbox()
            elif bg == "black":
                cropped_image = out_image.getbbox()


            out_image = out_image.crop(cropped_image)
      
            out_image.save('./output/output'+str(count)+'.jpg')
        count+=1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vidObj.release()



    path= os.getcwd()
    data_dir='data'
    data_subdir='output'
    output_vid_dir='outputvideo'
    if not os.path.exists(output_vid_dir):
        os.mkdir(output_vid_dir)

    input_frame_path= os.path.join(path,data_subdir)
    img_list = os.listdir(input_frame_path)
    frame = cv2.imread(os.path.join(input_frame_path,'output0.jpg'))
    height, width, channels = frame.shape
    fps=10
    output_file_name='outputvideo/finalvid.mp4'
    fourcc= cv2.VideoWriter_fourcc(*'mp4v')
    size= (width,height)
    convert_frames_to_video(img_list,output_file_name,fps,size)
#for image
else:
    image = cv2.imread("./data/"+inp)
    height, width, _ = image.shape

    cell_w = width / num_cols
    cell_h = scale * cell_w
    num_rows = int(height / cell_h)
    char_width, char_height = font.getsize("A")
    out_width = char_width * num_cols
    out_height = scale * char_height * num_rows
    out_image = Image.new("RGB", (out_width, out_height), bg_code)
    draw = ImageDraw.Draw(out_image)


    for i in range(num_rows):
        for j in range(num_cols):
            partial_image= image[int(i*cell_h):min(int((i+1)*cell_h),height),int(j*cell_w):min(int((j+1)*cell_w),width),:]
            partial_avg_color = np.sum(np.sum(partial_image,axis=0),axis=0)/(cell_h*cell_w)
            partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist()) 
            c = char_list[min(int(np.mean(partial_image)*num_chars/255),num_chars-1)]
            draw.text((j*char_width,i*char_height),c,fill = partial_avg_color, font= font)

    if bg == "white":
        cropped_image = ImageOps.invert(out_image).getbbox()
    elif bg == "black":
        cropped_image = out_image.getbbox()

# Saving the new Image
    out_image = out_image.crop(cropped_image)
    out_image.save("./data/outputimage.jpg")
