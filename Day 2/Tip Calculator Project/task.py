print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
percenttip = tip / 100
billandtip = (percenttip + 1) * bill
people = int(input("How many people to split the bill? "))
personpays = (billandtip / people)
print(f"Each person pays: {(round(personpays, 4))}")

