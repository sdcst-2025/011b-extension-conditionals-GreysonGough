from os import system
system("clear||cls")

print("As you run to the beach you see countless activities to do, but 2 catch your eye...")
print("")
print("1.Swimming")
print("2.Volley ball")

choice = input("What will you do?(type 1 or 2)")
if choice == "1":
    import page14
elif choice =="2":
    import page15
else:
    print("invalid answer, restart")