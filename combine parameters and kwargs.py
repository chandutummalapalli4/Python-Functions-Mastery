def student_details(student_id, **details):
    print("Student ID :", student_id)

    for key, value in details.items():
        print(key, ":", value)

student_details(
    101,
    name="Chandu",
    age=21,
    city="Nagullanka",
    course="Python"
)