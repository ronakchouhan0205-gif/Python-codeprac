name = input("Enter your name: ")
name = name.strip().title()

roll_number = input("Enter your roll number: ")
roll_number = roll_number.strip().upper()


maths_marks = input("Enter your Maths marks: ")
maths_marks = int(maths_marks)

science_marks = input("Enter your Science marks: ")
science_marks = int(science_marks)

english_marks = input("Enter your English marks: ")
english_marks = int(english_marks)

total = maths_marks + science_marks + english_marks
print("Total: ", total)

average = total / 3
print("Average: ", average)

if average >=90:
    grade = "A+"
    remark = "Outstanding"
elif average >=75:
    grade = "B+"
    remark = "Excellent"
elif average >=60:
    grade = "C+"
    remark = "Good"
elif average >=40:
    grade = "D+"
    remark = "Need improvement"
else:
    grade = "Fail"

print("-" * 60)
print(f"{'Student Report Card':^50}")
print("-" * 60)
print(f"{'Name':<15}: {name}")
print(f"{'Roll number':<15}: {roll_number}")
print("-" * 60)
print(f"{'Subject':<15} {'Marks':>22}")
print("-" * 60)
print(f"{'Maths':<15} {maths_marks:>20}")
print(f"{'Science':<15} {science_marks:>20}")
print(f"{'English':<15} {english_marks:>20}")
print("-" * 60)
print(f"{'Total':<15} {total:>20}")
print(f"{'Average':<15} {average:>20}")
print(f"{'Grade':<15} {grade:>20}")
print(f"{'Remark':<15} {remark:>20}")
print("-" * 60)
