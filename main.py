from src.Student import Student
from src.Person import Person
from src.Course import Course
from src.Professor import Professor

def main():
    courses = [Course('Algorithm', 1), 
               Course('Python', 2), 
               Course('Network', 3)]
    

    profs = [Professor('Ali', 'Jalali', 1 ,[courses[0],courses[2]]),
             Professor('Hamed', 'Salehi', 2, [courses[1]])]


    studs = [Student('Shima', 'Amiri', 1, 19, {courses[0]: 12, courses[1]: 16}),
             Student('Farzad', 'Davoodi', 2, 24, {courses[1]: 14, courses[2]: 16})]