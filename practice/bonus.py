salary = int(input('Enter your salary: '))
rating = int(input("Enter the rating: "))
experience = int(input("How much experience: "))
attendance = int(input("Enter the attendance: "))
bonus =0
if rating==5:
    bonus+= salary*0.25
elif rating == 4:
    bonus += salary*0.15
elif rating ==3:
    bonus += salary*0.10

if experience>10:
    bonus += salary*0.10
elif experience >= 5 and experience <=10:
    bonus += salary*0.05

if attendance >=95:
    bonus += 5000
elif attendance >=85 and attendance<=94:
    bonus += 2000
print(bonus)