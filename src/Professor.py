from Person import Person

class Professor(Person):

    def __init__(self, name, family_name, prof_id, lectures):
        super().__init__(name, family_name, prof_id)
        self.lectures = lectures

    

    def give_grade():
        pass

    def take_lectures():
        pass