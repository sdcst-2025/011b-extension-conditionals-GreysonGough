from os import system
system("clear||cls")

print("After finishing your burger, the server comes around with the bill.")
print("")
print("1. Tip the server")
print("2. Don't tip the server")
print("3. Dine and dash")
choice = input("What will you do?(type 1 or 2 or 3)")

if choice == "1":
    import page8
elif choice =="2":
    import page9
elif choice == "3":
    import page10

else:
    print("invalid answer, restart ")
