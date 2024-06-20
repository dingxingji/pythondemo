width = eval(input("please input a width nums:"))
width += 1  # range less than fact so add 1 to the width
half = width // 2  # get the half index for symmetry rectangle print
arr = []  # set of the stars in line before
for i in range(1, width):  # it for line
    if i <= half:
        stars = i * 2 - 1  # star nums
        if i < half:
            arr.append(stars)
        else:
            arr.insert(0, 0)
    else:
        stars = arr[half - i]
    for j in range(1, width):  # it for column in one line
        if ((width - stars) // 2) < j <= ((width - stars) // 2 + stars):
            print('*', end='')
        else:
            print('-', end='')
    print()
