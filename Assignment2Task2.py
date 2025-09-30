# Generate a numeric pattern that consists of rows of numbers, where each row starts from the row number and decrements to 1
for i in range(0,10):
    for j in range(i):
        print(end = ' ')
    for k in range(10-i,0,-1):
        print(k,end = " ")
    print()