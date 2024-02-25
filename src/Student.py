from src.Person import Person
from src.Course import Course
from src.read import read


class Student(Person):

    def __init__(self, name, family_name, std_id, age:int, grades):
        super().__init__(name, family_name, std_id)
        self.age = age
        self.grades = grades

    def pick_lecture(self):
            courses_lst = read('Courses')

            for course in courses_lst:
                print(f"\nID:{course['id']}\nname: {course['name']}\n")
            
            id_selected = int(input("\nSelect a course by it\'s ID: "))

            if id_selected not in self.grades.keys():

                for course in courses_lst:

                    if course['id'] == id_selected:
                        course_name = course['name']
                        print('Course added!')
                        return course_name
                else:
                    print('Wrong entry!')    

            else:
                print('This lecture already exists!')
            
            
            
                 

    def avg_grades(self):
        sum = 0
        count = 0

        for grade in self.grades.values():
            if grade != None:
                sum += grade
                count += 1
                
        if sum == 0:
            print('No grades yet!')

        return sum//count
            

    def status(self):
        avg = self.avg_grades()
        if  20 > avg >= 10:
            print('\nYou passed!\n')
        elif 10 > avg > 0:
            print('\nYou failed!\n')
        else:
            print('\nInvalid!\n')

    def stu_dict(self):
        return {'name': self.name, 'family_name':self.family_name, 'id': self.id, 'age':self.age, 'grades':self.grades}