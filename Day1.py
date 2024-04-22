# แสดงผลข้อมูล
print("hello world")
print("*" * 10)


# Variable
pet = ["dog", "cat"]
rated = 4.5
values = 10
isPublished = True
print(pet)
print(rated)
print(values) # ปริ้นค่าใน Variable
print("The value is: " + str(values)) # แสดงผลลัพธ์เป็นตัวหนังสือ พร้อมค่าจากใน Variable
print(isPublished)


# Receiving Input
name = input('What is your name ? ')
favoriteColor = input('What is your favorite color ? ')
print(name + " like " + favoriteColor + ".")


# Typing Conversion
birthYear = input('Brith year ? ')
age = 2024 - int(birthYear)
print(type(age))
print(age)

weight_kg = input('Weight (Kg): ')
weight_lbs = int(weight_kg) / 0.45
print(weight_lbs)
print("Weight(lbs) is: " + str(weight_lbs) + " lbs.")