'''
The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
Marks scored  Grade 
100            S
90 - 99        A
80 - 89        B
70 - 79        C
60 - 69        D
50 - 59        E
<50            F

Input format:
The input consists of one integer which corresponds to the marks scored by the student

Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.
Sample Input:
78
Sample Output:C
'''
x = int(input())
if x == 100:
    print("S")
elif x >= 90 and x <= 99:
    print("A")
elif x >= 80 and x <= 89:
    print("B")
elif x >= 70 and x <= 79:
    print("C")
elif x >= 60 and x <= 69:
    print("D")
elif x >= 50 and x <= 59:
    print("E")
elif x < 50:
    print("F")
elif x > 100:
    print("Invalid Input")
