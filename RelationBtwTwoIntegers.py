'''
Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"
Sample Input:
6
8
Sample Output:
6 less than 8
'''
x = int(input())
y = int(input())
if x == y:
    print(str(x) + " and " + str(y) + " are equal")
elif x > y:
    print(str(x) + " greater than " + str(y))
else:
    print(str(x) + " less than " + str(y))
