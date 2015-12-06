def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)

grades = [32, 1, 2, 3, 44]
print(drop_first_last(grades))


##############################################################
