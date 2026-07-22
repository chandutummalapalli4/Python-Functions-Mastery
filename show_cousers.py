def show_courses(*courses):
    for names in courses:
        print("Name of Courses:",names)
show_courses("SQl","Python","Java","Maths","Physics")
##---------advance version-----------##
def show_courses(*courses):
    count = 1

    for course in courses:
        print("Course", count, ":", course)
        count += 1

show_courses("SQL", "Python", "Java", "Maths", "Physics")