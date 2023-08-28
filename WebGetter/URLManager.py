import urllib.request
import os
def DownloadHTMFile():
    professor_url = 'https://sdmda.bupt.edu.cn/szdw/js.htm'
    associate_professor_url = 'https://sdmda.bupt.edu.cn/szdw/fjs.htm'
    lecturer_url = 'https://sdmda.bupt.edu.cn/szdw/js1.htm'
    urllib.request.urlretrieve(professor_url,'./WebResource/professor.htm')
    urllib.request.urlretrieve(associate_professor_url,'./WebResource/associate_professor.htm')
    urllib.request.urlretrieve(lecturer_url,'./WebResource/lecturer.htm')

    folder_path = './WebResource'
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