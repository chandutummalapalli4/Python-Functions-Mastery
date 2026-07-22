def find_smallest(*num):
    min_num = num[0]
    for number in num:
        if number < min_num:
            min_num = number
    print("smallest Number:",min_num)
find_smallest(87,23,27,12,33)
