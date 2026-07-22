def sum_even_numbers(*numbers):
    total=0
    for num in numbers:
        if num%2==0:
            print("Even Numbers:",num)
            total+=num
    print("Sum of even Numbers:",total)
sum_even_numbers(12,23,34,56,64,77)        