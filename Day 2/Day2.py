# ---------- Formatted Strings ----------
firstName = 'John'
lastName = 'Smith'
massage = firstName + ' [' + lastName + '] is a coder'
msg = f'{firstName} [{lastName}] is coder'
print(msg)


# ---------- String Methods ----------
course = 'Python for Beginner'
print(len(course))
print(course.upper())
print(course.find("P")) # ผลออกมาเป็นการนับแบบคอมพิวเตอร์
print(course.replace("Beginner","Absolute Beginners")) # Python for Absolute Beginners