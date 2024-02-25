from src.Person import Person
from src.read import read


class Professor(Person):

    def __init__(self, name, family_name, prof_id, lectures):
        super().__init__(name, family_name, prof_id)
        self.lectures = lectures

    
    def give_grade(self):

        stu_lst = read('Students')

        for course in self.lectures:
            print(f"\ncourse name: {course}\n")
            
        crs_selected = input("\nSelect a course: ")
        crs_selected = crs_selected.lower()
        
        for student in stu_lst:
            if crs_selected in student['grades'].keys():
                print(f"\nID: {student['id']}\nname: {student['name']} {student['family_name']}\n\n") 
                break

        else:
            print('No student has this course!')

        stu_id_selected = int(input("Choose a student by ID :"))

        grade = int(input('Enter the grade: '))

        for student in stu_lst:
            if stu_id_selected == student['id']:
                student['grades'][crs_selected] = grade
                




    def take_lectures(self):
        if len(self.lectures) < 3:
            courses_lst = read('Courses')

            for course in courses_lst:
                print(f"\nID:{course['id']}\nname: {course['name']}\n")

            crs_selected = input("\nSelect a course: ")
            crs_selected = crs_selected.lower()

            if crs_selected not in self.lectures:

                for lecture in self.lectures:

                    if lecture == crs_selected:
                        self.lectures.append(crs_selected)
                        print('Course added!')
                        return self.lectures
                else:
                    print('Wrong entry!')    

            else:
                print('This lecture already exists!')
            


    def prof_dict(self):
        return {'name': self.name, 'family_name':self.family_name, 'id': self.id, 'lectures':self.lectures}