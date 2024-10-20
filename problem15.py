size = 6
for i in range(size):
    for j in range(size - 1, i ,-1):
        print(j, end=' ')
    for j in range(i + 1, size):
        print(j, end=' ')
    print()
