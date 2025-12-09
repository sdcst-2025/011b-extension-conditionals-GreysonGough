from os import system
system("clear||cls")

print("You successfully made your way to the restaurant but you come across a variety of food to order from.")
print("")
print("1.Tacos")
print("2.Burger")
print("3.Icecream")



choice = input("Where do you want to go next? (type 1, 2 or 3.)")

if choice == "2":
    import page7
elif choice == "1":
    import page4
elif choice == "3":
    import page3
else:
    print("not a valid answer")
