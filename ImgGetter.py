import os
import requests

web_path = "https://sdmda.bupt.edu.cn/"
save_path = "./WebResource/Img"

def FixURL(image_url):
    if image_url.startswith('/'):
        image_url = image_url.lstrip('/')
    if not image_url.startswith('https://'):
        image_url = os.path.join(web_path, image_url)
        print(image_url)

def DownloadHTMFile(image_url,save_path):
    try:
        # 发送GET请求获取图片数据
        response = requests.get(image_url)
        
        # 检查响应状态码是否为200（表示成功）
        if response.status_code == 200:
            # 以二进制模式打开文件，保存图片数据
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded and saved as {save_path}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {str(e)}")
if __name__ == '__main__':
    DownloadHTMFile("/__local/6/AB/9D/0283B095A82459A238799253784_99B7F9CC_A5003.jpg",save_path)