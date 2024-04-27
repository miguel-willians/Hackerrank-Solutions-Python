if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

  # Solution: / Solução:
  
    grades = student_marks[query_name]
    gradeSum = 0
    
    for grade in grades:
        gradeSum += grade
    
    result = gradeSum/len(grades)
    
    print(f"{result:.2f}")
