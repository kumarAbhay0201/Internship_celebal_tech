#code for pyramid pattern 

rows = int(input("Enter number of rows "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for u in range(2 * i + 1):
        print('*', end="")
    print()
