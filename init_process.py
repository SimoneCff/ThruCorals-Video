from __future__ import absolute_import, division, print_function
import os
from SeaThru.transform import run
from CNN.valuate import Smart_sorting
import tempfile
import zipfile

def create_zip(dir):
    zip_name = "output.zip"
    with zipfile.ZipFile(zip_name, "w") as zip_file:
        for root, dirs, files in os.walk(dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                zip_file.write(filename=file_path)

def get_frame_list(path):
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
    image_list = []

    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            extension = os.path.splitext(filename)[-1].lower()
            if extension in image_extensions:
                image_path = os.path.join(foldername, filename)
                image_list.append(image_path)

    return image_list


#Start Process
def Start_process(input):
    temp_dir = tempfile.mkdtemp()

    bright, balance, illum, min, max, fract, add, mul, size, transf, raw = input.submit()
    
    print("<TERMINAL> Inizio Processo... \n")
    
    #Check dir exists
    if  == "":
        print("<ERROR> Input Dir not specified")
        return

    video_frames = get_frame_list(input.dir)

    #Check images inside
    if video_frames is None or len(video_frames) == 0:
       print("<ERROR> No Frames Extracted")
       return

    #Start Loop Transform
    for element in image_l:
        print("<SEATHRU> Inizio Trasformazione Immagine : "+os.path.basename(element)+" ")
        try:
            run(element,"SeaThru/models/mono+stereo_1024x320",bright, balance, illum, min, max, fract, add, mul, size, raw,temp_dir)
            print("DONE \n")
        except:
            print("ERROR \n")

    print("<SEATHRU> Processo Terminato Corretamente \n")

    print("<CNN> Inizio Processo Classificazione \n")
    file_list = get_image_list(temp_dir)
    for element in file_list:
        print("<CNN> Classificazione Immagine : "+os.path.basename(element)+" ")
        label = Smart_sorting(temp_dir,element)
        print("Label : "+label+"\n")
            
    print("<CNN> Processo Classificazione Terminato Corretamente \n")
    create_zip(temp_dir)