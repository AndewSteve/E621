import os
from WebGetter import WebGetter
import Parser
resource_folder_path = './WebResource'
Img_folder_path = './WebResource/Img'

downloadImg = False
files_check = os.listdir(resource_folder_path)
if len(files_check)==0:
    WebGetter.DownloadHTMFile()
files_check = os.listdir(Img_folder_path)
if len(files_check)==0:
    downloadImg = True

Parser.ParseFiles(DownloadImg= downloadImg,Resource_folder_path = resource_folder_path)