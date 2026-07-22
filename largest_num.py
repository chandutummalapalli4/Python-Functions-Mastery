def find_largest(*numbers):
    max_num=0
    for num in numbers:
        if num>max_num:
            max_num=num
    print("Largest_number:",max_num)
find_largest(12,23,9,45,56)