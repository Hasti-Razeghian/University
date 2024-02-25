from src.Course import Course
from src.Professor import Professor
from src.write_file import write_file
from src.read import read
from src.Student import Student


def main():

    courses = [Course('algorithm', 1).course_dict(), Course('python', 2).course_dict(), Course('network', 3).course_dict()]
    write_file(courses, 'Courses')
    profs = [Professor('Ali', 'Jalali', 1 ,['algorithm','network']).prof_dict(), Professor('Hamed', 'Salehi', 2, ['python']).prof_dict()]
    write_file(profs, 'Professors')
    studs = [Student('Shima', 'Amiri', 1, 19, {'algorithm': 15, 'python': 11}).stu_dict(), Student('Farzad', 'Davoodi', 2, 24, {'python': None, 'network': None}).stu_dict()]
    write_file(studs, 'Students')

    stu_lst = read('Students')
    course_lst = read('Courses')
    prof_lst = read('Professors')

    inp = input('Are you a student or a professor?\nEnter s or p: ')

    if inp == 's':
        
        for stu in stu_lst:
            print(f"\nid:{stu['id']}\nname: {stu['name']} {stu['family_name']}\n")

        inp_id = input('Please enter your student id: ')


        for stu in stu_lst:
            if inp_id == str(stu['id']):
                print(f"\nWelcome {stu['name']} {stu['family_name']}\n")
                indx = stu_lst.index(stu)
                student = Student(stu_lst[indx]['name'], stu_lst[indx]['family_name'], stu_lst[indx]['id'], stu_lst[indx]['age'],stu_lst[indx]['grades'])
                break
        else:
            print('\nWrong ID\n')

        act = input('1.Pick a lecture\n2.Check your status\n3.Average of your scores\n\nSelect an action by it\'s number:')

        if act == '1':
            course_name = student.pick_lecture()
            student.grades[course_name] = None
            stu_lst[indx] = student.stu_dict()
            write_file(stu_lst, 'Students')


        elif act == '2':
            student.status()

        elif act == '3':
            print('The average is ',student.avg_grades())

        else:
            print('Wrong entry!')
            

    elif inp == 'p':
        for prof in prof_lst:
            print(f"\nid:{prof['id']}\nname: prof. {prof['name']} {prof['family_name']}\n")

        inp_id = input('Please enter your professor id: ')

        for prof in prof_lst:
            if inp_id == str(prof['id']):
                print(f"\nWelcome {prof['name']} {prof['family_name']}\n")
                indx = prof_lst.index(prof)
                professor = Professor(prof_lst[indx]['name'], prof_lst[indx]['family_name'], prof_lst[indx]['id'],prof_lst[indx]['lectures'])
                break
        else:
            print('\nWrong ID\n')

        act = input('1.Enter a grade\n2.Add a lecture\n\nSelect an action by it\'s number:')

        if act == '1':
            professor.give_grade()

        elif act == '2':
            professor.take_lectures()


    else:
        print('Wrong entry!')

if __name__ == '__main__':
    main()
    