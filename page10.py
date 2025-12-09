from os import system
system("clear||cls")

print("You decide to make a run for it at the restaurant.")
print("the waiter comes with the bill but you insist that you need to grab your wallet from your car.")
print("As you step outside the building you bolt around the corner and run... ")
print("")
print("1.home")
print("2.to the beach")
print("3.back to the restaurant")
choice = input("What will you do?(type 1 or 2 or 3)")
if choice == "1":
    import page11
elif choice =="2":
    import page12
elif choice == "3":
    import page13
else:
    print("invalid answer, restart")