def show_cities(*names):
    print("First City  :",names[0])
    print("Second City :",names[1])
    print("Thrid City  :",names[2])
show_cities("Nagullanka","Razole","P.ganavaram")

##--------loop version-------##
def show_cities(*names):
    for city in names:
        print(city)

show_cities("Nagullanka", "Razole", "P. Ganavaram")