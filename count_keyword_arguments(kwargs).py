def show_details(**details):
    count=0
    for key,value in details.items():
        count+=1
        print(key,":",value)
    print("Total Arguments:",count)
show_details(name="Chandu",
            age=21,
            city="Nagullanka",
            pincode=533256)
