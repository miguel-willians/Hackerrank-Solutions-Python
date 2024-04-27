# Solution: / Solução:
if __name__ == '__main__':
    uniqueScores = set() 
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name,score]
        students.append(student)
        uniqueScores.add(score)
    
    if len(uniqueScores) > 1:
        listScore = sorted(list(uniqueScores))
        secondLowestScore = listScore[1]
        
        secondLowestStudents = [student[0] for student in students if student[1] ==secondLowestScore]
        
        secondLowestStudents.sort()
        
        for student in secondLowestStudents:
            print(student)
    else:
        print("There is no second lowest score.") 
