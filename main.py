from src.Student import Student
from src.Course import Course
from src.Professor import Professor
from src.write_file import write_file
from src.fill_files import fill_files
from src.read import read

def main():

    fill_files()
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
                break
        else:
            print('\nWrong ID\n')

        act = input('1.Pick a lecture\n2.Check your status\n3.Average of your scores\nSelect an action by it\'s number:')

        if act == '1':
            pass

        elif act == '2':
            pass

        elif act == '3':
            pass

        else:
            print('Wrong entry!')
            

    elif inp == 'p':
        pass
    else:
        print('Wrong entry!')

if __name__ == '__main__':
    main()
    