def calculate_total(*mark):
    total=0
    for marks in mark:
        print("Marks:",marks)
        total+=marks
    print("Total Marks:",total)
calculate_total(85,75,55,65,97)

