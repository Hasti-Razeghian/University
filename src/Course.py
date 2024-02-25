class Course():

    def __init__(self, course_name, course_id) -> None:
        self.name = course_name
        self.id = course_id

    def course_dict(self):
        return {'name': self.name, 'id': self.id}