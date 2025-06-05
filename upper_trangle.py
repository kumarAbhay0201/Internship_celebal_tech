#code for upper-triangle pattern 

row = int(input("Enter number of rows "))

for i in range(row,-1,-1):
    for j in range(i+1):
        print('*', end= "")
    print()
