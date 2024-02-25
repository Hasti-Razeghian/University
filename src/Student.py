from src.Person import Person

class Student(Person):

    def __init__(self, name, family_name, std_id, age:int, grades):
        super().__init__(name, family_name, std_id)
        self.age = age
        self.grades = grades

    def pick_lecture():
        pass

    def avg_grades():
        pass

    def status():
        pass

    def stu_dict(self):
        return {'name': self.name, 'family_name':self.family_name, 'id': self.id, 'age':self.age, 'grades':self.grades}