size = input("Enter Size: ")
count = 1
stop = 2
for i in range(1, int(size) + 1):
    for j in range(1, stop):
        print(count, end=' ')
        count += 1
    print()
    stop += 2