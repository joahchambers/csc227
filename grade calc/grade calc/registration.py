

import student.student as student


def main():


    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]
    while True:
        sid = input("Enter ID to log in, or 0 to quit: ")
        if sid == '0':
            print()
            break
        else:
            success=login(sid, student_list)
            while success:
                choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
                if choice == 0:
                    print("Student session ended.")
                    print()
                    success=False
                if choice == 1:
                    student.add_course(sid, course_list, roster_list, max_size_list)
                    print()
                if choice == 2:
                    student.drop_course(sid, course_list, roster_list)
                    print()
                if choice == 3:
                    student.list_courses(sid, course_list, roster_list)
                    print()


def login(id, s_list):

    pin = input("Enter PIN: ")
    found = False
    for i  in s_list:
        if (i[0] == id and i[1] == pin):
            print("ID and PIN verified")
            print()
            return True
    if(found == False):
        print("ID or PIN incorrect")
        return False

main()



