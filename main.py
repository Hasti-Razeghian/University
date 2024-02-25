from src.Student import Student
from src.Person import Person
from src.Course import Course
from src.Professor import Professor
from src.write_file import write_file

def main():
    courses = [Course('Algorithm', 1).course_dict(), 
            Course('Python', 2).course_dict(), 
            Course('Network', 3).course_dict()]
    write_file(courses, 'Courses')


    profs = [Professor('Ali', 'Jalali', 1 ,['Algorithm','Network']),
             Professor('Hamed', 'Salehi', 2, [courses[1]])]
    write_file(profs, 'Professors')


    studs = [Student('Shima', 'Amiri', 1, 19, {'Algorithm': None, 'Python': None}),
             Student('Farzad', 'Davoodi', 2, 24, {'Python': None, 'Network': None})]
    write_file(studs, 'Students')



# if __name__ == '__main__':
#     main()
    
main()