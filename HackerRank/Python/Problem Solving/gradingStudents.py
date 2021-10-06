# Manuel Ortiz Hernández at 2020
#Problem solving. Extracted from: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def grading_students(grades):
    i = 0
    if not grades:
        return "There are no grades"
    else:
        while i < len(grades):
            if grades[i] >= 38:
                if ((grades[i]+1)%5) == 0:
                    grades[i] += 1
                elif ((grades[i]+2)%5) == 0:
                    grades[i] += 2
 
            i+=1
        return grades
    
if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = [] 
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = grading_students(grades)
    print(result)