from urllib.error import URLError
import urllib.request
import os
def DownloadHTMFile():
    folder_path = './WebResource'
    url_map= {
        'professor': 'https://sdmda.bupt.edu.cn/szdw/js.htm',
        'associate_professor': 'https://sdmda.bupt.edu.cn/szdw/fjs.htm',
        'lecturer': 'https://sdmda.bupt.edu.cn/szdw/js1.htm'
    }
    for title, url in url_map.items():
        file_name = f'{folder_path}/{title}.htm'
        try:
            urllib.request.urlretrieve(url, file_name)
            print(f'{title} HTML file secured.')
        except URLError as e:
            print("NetWork Error:", e)
        except FileNotFoundError as e:
            print("File Not Found Error:", e)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.htm') or file_name.endswith('.html'):
            file_path = os.path.join(folder_path, file_name)
            FixHTMContent(file_path)

def FixHTMContent(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    html_content = html_content.replace('&#34;', '\'')
    html_content = html_content.replace('&quot;', '\'')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)


if __name__ =='__main__':
    DownloadHTMFile()