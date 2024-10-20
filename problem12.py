size = int(input("Enter a size: "))
num = 1
row_size = 1

while num <= size:
    for i in range(row_size):
        if num <= size:
            print(num, end=" ")
            num += 1
    print()
    row_size += 2