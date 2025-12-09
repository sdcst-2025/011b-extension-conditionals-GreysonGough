from os import system
system("clear||cls")

print("After a long day of coding and fixing countless errors, its time for a break")

print("Choice 1: Go to the park")
print("Choice 2: Go to a restaurant")

choice = input("Where do you want to go? (type 1 or 2)")
if choice == "2":
    import page2
elif choice == "1":
    import page1
else:
    print("invalid answer")
