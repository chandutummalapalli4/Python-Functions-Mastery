def student_report(student_id,*marks,**details):
    print("Student ID   :",student_id)
    print("Marks        :",marks)
    print()
    for key,values in details.items():
        print(key,":",values)
student_report(101,
               65,75,88,
               name="Chandu",
               age=21,
               branch="IT",
               )