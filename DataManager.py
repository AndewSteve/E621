import csv
from Teacher import Teacher
Data_path = "./Data/teachers.csv"
class TeacherDataWriter:
    def __init__(self):
        self.csv_file = open(Data_path, mode='w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.csv_file)
        self.writer.writerow(["Department", "Name", "Title", "Photo"])

    def __del__(self):
        if hasattr(self,'csv_file') and not self.csv_file.closed:
            self.csv_file.close()

    def writeTeacherData(self,teacher):
        self.writer.writerow([str(teacher.department), str(teacher.name),str(teacher.identity), str(teacher.photo_save_path).replace('\\','/')])
        print(f"Teacher data recorded:{teacher.name}")
    
    def writeMultiTeacherData(self,teachers):
        for teacher in teachers:
            self.writeTeacherData(teacher)

if __name__ == '__main__':
    teacher = Teacher("学生","momoi","千年游戏开发部","momoi.jpg")
    dataWriter = TeacherDataWriter()
    dataWriter.writeTeacherData(teacher)
    print(" ")