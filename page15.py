from os import system
system("clear||cls")

print("You decide to play volleyball.")
print("You ask them if you can join and they accept.")
print("The parents look at you weird as you are a random middle aged guy playing against a couple middle schoolers.")
print("The score slowly becomes one sided as you dominate the game.")
print("After around 15 minutes you begin to get bored.")
print("")

print("1.Home")
print("2.Aquarium")

choice = input("What will you do?(type 1 or 2)")
if choice == "1":
    import page11
elif choice =="2":
    import page17
else:
    print("invalid answer, restart")