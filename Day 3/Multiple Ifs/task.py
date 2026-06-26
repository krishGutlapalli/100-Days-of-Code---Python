print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5 for a child ticket.")
        bill += 5
    elif age < 18:
        print("Please pay $7 for a youth ticket.")
        bill += 7
    else:
        print("Please pay $12 for a adult ticket.")
        bill += 12
    photo = input("Do you want a photo? Type y for yes or n for no")
    if photo == "y":
        print("Please pay $3 for a photo")
        bill += 3
    else:
        print("Ok enjoy your ride")
    print("Your final bill is $" + str(bill))
else:
    print("Sorry you have to grow taller before you can ride.")
