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


# ---------- Operator Precedence ----------
x = (10 + 3) * 2 ** 3
print(x)

# 1. ทำในวงเล็บ
# 2. ทำ 2 ยกกำลัง 3 (**)
# 3. ทำคูณหรือหาร
# 4. ทำบวกหรือลบ


# ---------- Math Function ----------
values1 = 3.6
values2 = -23.6
print(round(values1)) # การปัดทศนิยม
print(abs(values2)) # จะได้เป็นเลขตัวนั้นที่เป็นค่าบวกเท่านั้น


# ---------- If Statements ----------
"""
Conditions

if it is hot
    It is a hot day
    Drink plenty of water
otherwise if it is cold
    It is a cold day
    Wear warm clothes
otherwise
    It is a lovely day


"""

is_hot = False
is_cold = True
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")
else:
    print("It is a lovely day")