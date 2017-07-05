def age_foo(age):
    new_age = age + 50
    return new_age

age = float(input("Enter age: "))

if age < 50:
    print(age_foo(age))
else:
    print("Really? ", age_foo(age))
