def show_details(**details):
    for key, value in details.items():
        print(key, ":", value)

show_details(
    name="Chandu",
    age=21,
    city="Nagullanka",
    course="Python"
)