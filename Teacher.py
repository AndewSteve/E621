import os
from urllib.error import URLError
import urllib.request
web_path = "https://sdmda.bupt.edu.cn/"
Img_save_path = "./WebResource/Img"
class Teacher:
    def __init__(self, identity, name, department, photo_url,downloadImg = False):
        self.identity = identity
        self.name = name
        self.department = department
        self.photo_web_url = FixURL(photo_url)
        self.photo_save_path = FixSavePath(name)
        if downloadImg :
            GetImgFromWeb(self.photo_web_url,self.photo_save_path,name)

def GetImgFromWeb(photo_web_url,photo_save_path,name):
    try:
        urllib.request.urlretrieve(photo_web_url, photo_save_path)
        print(f'{name} Img file secured.')
    except URLError as e:
        print("NetWork Error:", e)
    except FileNotFoundError as e:
        print("File Not Found Error:", e)

def FixSavePath(name):
    file_name = name+ ".jpg"
    photo_save_path = os.path.join(Img_save_path,file_name)
    return photo_save_path

def FixURL(photo_url):
    if photo_url.startswith('/'):
        photo_url = photo_url.lstrip('/')
    if photo_url.endswith("?e=.jpg"):
        photo_url = photo_url.replace("?e=.jpg","")
    if not photo_url.startswith("https://"):
        photo_url = os.path.join(web_path, photo_url)
        return photo_url
    
if __name__ == '__main__':
    teacher = Teacher("学生","momoi","千年游戏开发部","momoi.jpg",True)
    print()