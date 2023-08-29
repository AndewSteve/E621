from html.parser import HTMLParser
import os
from Teacher import Teacher
from DataManager import TeacherDataWriter   
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dataWriter = TeacherDataWriter()
        self.teachers = []
        self.current_teacher = {
            'name': "",
            'department': "",
            'Photo_Url': ""
        }
        self.is_department_info = False
        self.is_teacher_info = False
        self.teacher_identity = "教授"
        self.is_teacher_name = False
        self.is_teacher_iden = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.is_department_info = True
        if tag == 'div' and ('class','col-md-1-5 col-sm-1-5  col-xs-6') in attrs:
            self.is_teacher_info = True
        if self.is_teacher_info:
            if tag =='img':
                for attr in attrs:
                    if attr[0] == 'src':
                        self.current_teacher['Photo_Url'] = attr[1]
            elif tag=='span':
                if ('class','name') in attrs:
                    self.is_teacher_name = True
                elif ('class','iden') in attrs:
                    self.is_teacher_iden = True

    def handle_endtag(self, tag):
        if tag == 'html':
            self.clearTeachersBuffer()
        if tag == 'title':
            self.is_department_info = False
        if tag == 'div' and self.is_teacher_info:
            self.is_teacher_info = False
        if self.is_teacher_info:
            if tag =='span' and self.is_teacher_name:
                self.is_teacher_name = False
            elif tag =='span' and self.is_teacher_iden:
                self.is_teacher_iden = False

    def handle_data(self, data):
        if self.is_department_info and data.strip():
            self.teacher_identity = data.strip()
            self.teacher_identity=self.teacher_identity.split('-')[0]
        if self.is_teacher_info and data.strip():
            if self.is_teacher_name:
                self.current_teacher['name'] = data.strip()
            elif self.is_teacher_iden:
                self.current_teacher['department'] = data.strip()
                self.pushTeacherBuffer()

    def clearTeachersBuffer(self):
        self.dataWriter.writeMultiTeacherData(self.teachers)
        self.teachers = []

    def pushTeacherBuffer(self):
        teacher = Teacher(self.teacher_identity,
                        self.current_teacher['name'],
                        self.current_teacher['department'],
                        self.current_teacher['Photo_Url'],
                        downloadImg= False)
        self.teachers.append(teacher)
        if len(self.teachers) >=5:
            self.clearTeachersBuffer()
        self.current_teacher = {
            'name': "",
            'department': "",
            'Photo_Url': ""
        }

def ParseFiles(resource_folder_path = "./WebResource"):
    parser = MyHTMLParser()
    for file_name in os.listdir(resource_folder_path):
        if file_name.endswith(".htm") or file_name.endswith(".html"):
            file_path = os.path.join(resource_folder_path,file_name)
            with open(file_path, "r", encoding="utf-8") as html_file:
                html_content = html_file.read()
                parser.feed(html_content)

if __name__ == '__main__':
    ParseFiles()
    print()