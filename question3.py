
#Question 3
# Using loop of your choice, WITI  has tasked you to automate a simple grading system. 
# As a python student, write a program using functions and conditions to display the grades that 
# the students will be receiving. 
# The grades are:
# 90% - 100%  Grade is A
# 80% - 89% Grade is   B
# 70% - 79% Grade is   C                                                        
# 60% - 69%  Grade is  D                  
# 50% - 59%  Grade is  E  
# < 50%   Fail 
def grade_students():
    # Function to determine the grade based on the score and handle user input.
    try: #try helps in code maintainance/handling
        num_students = int(input("Enter the number of students: "))
        
        for number in range(num_students):
            try:
                # Prompt the user to enter each student's score.
                score = float(input(f"Enter the score for student {number + 1} : "))
                if 90 <= score <= 100:
                    grade = "A"
                elif 80 <= score <= 89:
                    grade = "B"
                elif 70 <= score <= 79:
                    grade = "C"
                elif 60 <= score <= 69:
                    grade = "D"
                elif 50 <= score <= 59:
                    grade = "E"
                elif 0 <= score < 50:
                    grade = "Fail"
                else:
                    grade = "Invalid score"
                
                # Print the result.
                print(f"Student {number + 1}  Scores: {score}%  the Grade is: {grade}")

            except ValueError:
                print("Invalid input. Please enter a numeric score.")
    except ValueError:
        print("Invalid input. Please enter a valid number of students.")
grade_students()
