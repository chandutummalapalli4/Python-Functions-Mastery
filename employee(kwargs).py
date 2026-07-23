def empolyee_show(**details):
    for key,value in details.items():
        print(key,":",value)
empolyee_show(name="Chandu",
              city="Hyd",
              age=21,
              department="IT",
              empolyee_id=124675,
              salary=32000)