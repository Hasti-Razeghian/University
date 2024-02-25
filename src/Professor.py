from src.Person import Person

class Professor(Person):

    def __init__(self, name, family_name, prof_id, lectures):
        super().__init__(name, family_name, prof_id)
        self.lectures = lectures

    
    def give_grade():
        pass

    def take_lectures():
        pass


    def prof_dict(self):
        return {'name': self.name, 'family_name':self.family_name, 'id': self.id, 'lectures':self.lectures}