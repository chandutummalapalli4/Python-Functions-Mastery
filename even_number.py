def even_num(*numbers):
    count=0
    for num in numbers:
        if num%2==0:
            print("Even Number:",num)
            count+=1
    print("Count Of Even Numbers:",count)
even_num(11,22,12,34,45,36,64)        
