size = 10
c = 1
row_len = 1
while c <= size:
    index = 1
    for i in range(row_len, 0, -1):
        if c <= size:
            print((c + i) - index, end=' ')
            c += 1
        index += 1
    print()
    row_len += 1