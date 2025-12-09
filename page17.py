from os import system
system("clear||cls")

print("As you step foot into the aquarium you find the waiter that you ran away from")
print("You both make eye contact and only one thing comes to mind...")
print("")

print("1.FIGHT THEM")
print("2.Apologize")
print("3. Go home")

choice = input("What will you do?(type 1 or 2 or 3)")
if choice == "1":
    import page18
elif choice =="2":
    import page19
elif choice =="3":
    import page11
else:
    print("invalid answer, restart")