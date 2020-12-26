import time
print("Please wait..")
time.sleep(2)
print("Please enter your information correctly")
time.sleep(1)
print("="*50)


name=input("What is your name : ")
surname=input("What is your surname : ")
year=int(input("What is your birthday : "))
age=(2020-year)

information=[(name,surname,year)]


print("="*50)
if age > 18:
    for i in information:
        print(f"Hello {name} {surname}\nYou are {age} years old.\nYou were born in {year}\nYou can go out on the street.")
else:
    for i in information:
        print(f"Hello {name} {surname}\nYou are {age} years old.\nYou were born in {year}\nSorry...\nYou can't go out!\nBecause it's too dangerous.")
print("="*50)





