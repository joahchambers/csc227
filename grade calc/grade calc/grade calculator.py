
# Student 1's Grades
S1 = {"Name": "Christopher Collins",
      "Lab": [100, 95, 100, 91, 100, 100, 96, 100, 97, 93, ],
      "Midterm/Final Exam": [98, 97],
      "Project": [100]
      }

# Student 2's Grades
S2 = {"Name": "Annie White",
      "Lab": [100, 100, 89, 88, 88, 96, 91, 94, 88, 91, ],
      "Midterm/Final Exam": [98, 89],
      "Project": [100]
      }

# Student 3's Grades
S3 = {"Name": "Justin Martin",
      "Lab": [98, 93, 98, 89, 95, 92, 89, 100, 93, 90],
      "Midterm/Final Exam": [100, 98],
      "Project": [100]
      }

# Student 4's Grades
S4 = {"Name": "Theresa Jackson",
      "Lab": [100, 100, 98, 100, 99, 98, 97, 100, 99, 89],
      "Midterm/Final Exam": [98, 99],
      "Project": [100]
      }

# Student 5's Grades
S5 = {"Name": "Bruce Thomas",
      "Lab": [100, 100, 76, 100, 72, 80, 75, 73, 100, 91],
      "Midterm/Final Exam": [95, 95],
      "Project": [100]
      }

# Student 6's Grades
S6 = {"Name": "Lisa Martinez",
      "Lab": [82, 76, 78, 91, 84, 86, 100, 93, 96, 88],
      "Midterm/Final Exam": [96, 86],
      "Project": [100]
      }

# Student 7's Grades
S7 = {"Name": "Roger Evans",
      "Lab": [97, 96, 100, 100, 88, 76, 84, 72, 100, 85],
      "Midterm/Final Exam": [95, 98],
      "Project": [100]
      }

# Student 8's Grades
S8 = {"Name": "Angela Diaz",
      "Lab": [100, 100, 94, 100, 100, 95, 87, 77, 91, 75],
      "Midterm/Final Exam": [88, 95],
      "Project": [100]
      }

# Student 9's Grades
S9 = {"Name": "Douglas Cox",
      "Lab": [76, 97, 100, 87, 100, 98, 100, 77, 94, 100],
      "Midterm/Final Exam": [100, 91],
      "Project": [100]
      }

# Student 10's Grades
S10 = {"Name": "Kathy Green",
       "Lab": [100, 100, 87, 94, 89, 84, 71, 83, 100, 95],
       "Midterm/Final Exam": [89, 98],
       "Project": [100]
       }


# calculating average
def get_average(points):
    total = sum(points)
    total = float(total)
    return total / len(points)


# calculating total average
def calculate_total_average(students):
    lab = get_average(students["Lab"])
    exam = get_average(students["Midterm/Final Exam"])
    project = get_average(students["Project"])

    # Return the result based on weight of grade
    return ((0.39 * lab) +
            (0.26 * exam) + (0.09 * project))


# Calculate letter grade of each student
def assign_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


# calculating the average total of whole class
def class_average_is(student_list):
    grades_list = []

    for student in student_list:
        student_avg = calculate_total_average(student)
        grades_list.append(student_avg)
        return get_average(grades_list)


# list of all student dictionaries (grades)
students = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]

# Iterate through the list of students then calculate their average points and grade
for i in students:
    print(i["Name"])
    print("")
    print("Average Grade of %s: %s" % (i["Name"],
                                            "{:.2f}".format(calculate_total_average(i)))+"%")

    print("Letter Grade of %s: %s" % (i["Name"],
                                        assign_letter_grade(calculate_total_average(i))))

    print("--------------------------------------")

# Calculate the average of whole class
class_avg = class_average_is(students)

print("Class Average: %s" % "{:.2f}".format(class_avg)+"%")
print("Letter Grade of the class: %s "
      % (assign_letter_grade(class_avg)))
