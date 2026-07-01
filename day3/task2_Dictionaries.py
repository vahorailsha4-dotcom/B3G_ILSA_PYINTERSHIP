students=[
         {"name": "Vahora Ilsa","marks":100},     
         {"name": "afrin","marks":90},
         {"name": "sara","marks":80}
         ]
top=students[0]
for student in students:
    if student["marks"]>top["marks"]:
        top=student
print("Topper Name is:",top["name"])
print("marks:",top["marks"])