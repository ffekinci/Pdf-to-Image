""" 
  $ sudo apt-get install libmagickwand-dev
  $ pip install Wand
  $ pip install Pillow
"""

from PIL import Image as Img
from wand.image import Image
import uuid
import numpy as np
import glob
import os
import sys

dataset_path = "/home/ffekinci/Desktop/PdftoImage"
currentDir = os.getcwd()
save_path = currentDir + "/result"
files = []

for _ in os.listdir(dataset_path+'/'):
    files.append(dataset_path+'/'+_)

def convert(filepdf,savePath):
    page = 1
    with Image(filename=filepdf, resolution=200) as img:
        img.compression_quality = 80
        img.save(filename=savePath+"/%s.jpg" % page)
        page += 1

counter = 1
for pdfPath in files:
    pdf = pdfPath.split("/")[-1]
    print("### {}/{} Processing {} ###".format(counter, len(files), pdf))
    save_tmp = save_path + "/" + pdf.split(".")[0]
    if os.path.exists(save_tmp):
        os.system("rm -r "+save_tmp)
    os.system("mkdir -p "+save_tmp)
    result = convert(pdfPath,save_tmp)
    counter += 1
