print("Enter name of the Person:")
person = str(input())
print("Enter gender of the person: (M/F)")
gender = str(input())
print("Enter age of the person: ")
age = int(input())
if age < 18:
    print("This person is not eligible to vote")
elif age > 60:
    print("This person is eligible to vote")
elif gender == "M" and age > 30:
    print("This person is eligible to vote")
else:
    print("This person is not eligible to vote")
