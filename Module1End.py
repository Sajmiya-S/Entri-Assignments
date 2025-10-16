# Student Grade Management System

def calculate_average(marks): # Function to calculate the average of all marks in the list
    sum = 0
    for i in marks:
        sum += i
    average = sum / 5
    return average

def get_grade(average): # Function to determine grade based on average marks
    if average >= 90:
        grade = 'A'
    elif average >= 80 and average < 90:
        grade = 'B'
    elif average >= 70 and average < 80:
        grade = 'C'
    elif average >= 60 and average < 70:
        grade = 'D'
    elif average < 60:
        grade = 'F'
    return grade

class RangeError(Exception): # Creating 'RangeError' 
    pass

print('\n *****Student Grade Management System*****\n')
marks = [] # Empty list to store input marks

for i in range(5):
    try:
        mark = float(input(f'\nEnter mark of subject {i + 1}: '))
        if mark < 0 or mark > 100 : # Condition for 'RangeError'
            raise RangeError
        
    except ValueError: # Handling non-integer input 
        mark = float(input('\nEnter a valid number : '))

    except Exception as RangeError:  # Handling out of range input
        mark = float(input('\nEnter a number between 0 and 100 : '))

    finally:
        marks.append(mark) # Add marks to the list

# Calculate and display Average mark
average = calculate_average(marks)
print('\nAverage Marks: ', average)

# Determine and display Grade based on average
grade = get_grade(average)
print('\nGrade : ',grade)
