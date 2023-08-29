import os
from WebGetter import WebGetter
import Parser
resource_folder_path = './WebResource'

files_check = os.listdir(resource_folder_path)
if len(files_check)==0:
    WebGetter.DownloadHTMFile()

Parser.ParseFiles(resource_folder_path)