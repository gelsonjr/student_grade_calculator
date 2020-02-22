# student_grade.calculator.py

# Gelson Cardoso

# This is my class grades average calculator
# It calculates grade letters, average scores (individual and class),
# highest / lowest scores, and class median score


def main():

    # Intro
    print("Welcome to my student average and grades calculator!\n")

    # Lists
    students = []
    student_ids = []
    grades = []

    # Get number of students
    num_students = int(input("How many students in this class? "))

    # To initialize highest and lowest scores
    high_score = 0
    low_score = 999999

    # Loop to get students info
    for x in range(num_students):
        student_name = input("Please enter student # " +
                             str(x+1) + " First and Last names: ")
        student_id = input("Please enter student ID (XXXX): ")
        print("Please enter student grades (0-100):")
        grade_1 = int(input("Grade 1: "))
        grade_2 = int(input("Grade 2: "))
        grade_3 = int(input("Grade 3: "))
        grade_4 = int(input("Grade 4: "))
        grade_5 = int(input("Grade 5: "))
        grade_6 = int(input("Grade 6: "))
        grade_7 = int(input("Grade 7: "))
        grade_8 = int(input("Grade 8: "))
        grade_9 = int(input("Grade 9: "))
        grade_10 = int(input("Grade 10: "))

        total = grade_1 + grade_2 + grade_3 + grade_4 + grade_5 + \
            grade_6 + grade_7 + grade_8 + grade_9 + grade_10

        student_avg = total / 10

        print(student_name, "has an average score of", student_avg, end=" ")

        # To get letter grade
        if(student_avg >= 90 and student_avg <= 100):
            print('and received letter grade "A"\n')
        elif(student_avg >= 80 and student_avg < 90):
            print('and received letter grade "B"\n')
        elif(student_avg >= 70 and student_avg < 80):
            print('and received letter grade "C"\n')
        elif(student_avg >= 60 and student_avg < 70):
            print('and received letter grade "D"\n')
        elif(student_avg >= 0 and student_avg < 60):
            print('and received letter grade "F"\n')
        else:
            print("Strange Grade!\n")

        # To determine if student has the highest score in class
        if student_avg >= high_score:
            high_score = student_avg
            high_score_student_name = student_name

        # To determine if student has the lowest score in class
        if student_avg <= low_score:
            low_score = student_avg
            low_score_student_name = student_name

        # To add values to lists
        students.append(student_name)
        student_ids.append(student_id)
        grades.append(student_avg)

    print("-- Class information --\n")

    print("There are", num_students, "students in this class.\n")

    print(high_score_student_name +
          " has the highest student score! Score: " + str(high_score))
    print(low_score_student_name +
          " has the lowest student score! Score: " + str(low_score))

    class_avg = sum(grades) / num_students

    print("\nThe class average score is:", round(class_avg, 2))

    print("\nThe class median score is:", median(grades))

# Function to calculate class median
def median(grades):
    sorted_list = sorted(grades)
    list_len = len(grades)
    index = (list_len - 1) // 2

    if (list_len % 2):
        return sorted_list[index]
    else:
        return (sorted_list[index] + sorted_list[index + 1])/2.0


main()
