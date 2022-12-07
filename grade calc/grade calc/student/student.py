def list_courses(id, c_list, r_list):

    print("Courses registered:")
    total = 0
    if id in r_list[0]:
        print("CSC101")
        total += 1
    if id in r_list[1]:
        print("CSC102")
        total += 1
    if id in r_list[2]:
        print("CSC103")
        total += 1
    print("Number of courses registered:", total)

    print()
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has three parameters: id is the ID of the
    # student; c_list is the course list; r_list is the list of
    # class rosters. This function has no return value.
    # -------------------------------------------------------------

    #pass # temporarily avoid empty function definition


def add_course(id, c_list, r_list, m_list):

    course = input("Enter course you want to add: ")
    course = course.upper()
    index = -1
    if course == "CSC101":
        index = 0
    elif course == "CSC102":
        index = 1
    elif course == "CSC103":
        index = 2
    else:
        print('Course not found')

    if 0 <= index <= 2:
        enrollment = len(r_list[index])
        if enrollment >= m_list[index]:
            print("Course already full.")
        elif id in r_list[index]:
            print("You are already enrolled in that course.")
        else:
            r_list[index].append(id)
            print("Course added")
    print()

    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    #pass # temporarily avoid empty function definition


def drop_course(id, c_list, r_list):

    course = input("Enter course you want to drop: ")
    course = course.upper()
    index = -1
    if course == "CSC101":
        index = 0
    elif course == "CSC102":
        index = 1
    elif course == "CSC103":
        index = 2
    else:
        print('Course not found')

    if 0 <= index <= 2:
        if id in r_list[index]:
            r_list[index].remove(id)
            print("Course dropped")
        else:
            print("You are not enrolled in that course.")
    print()
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_list is the course list; r_list is the list of class
    # rosters. This function asks user to enter the course he/she
    # wants to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.  This function has no return value.
    # -------------------------------------------------------------

    #pass # temporarily avoid empty function definition
