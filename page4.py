from os import system
system("clear||cls")

print("You tell the server that you would like to order the tacos.")
print("The server warns you that these are the most spicy tacos in town but you think nothing of it.")
print("As you take the first bite it feels as if you are breathing out fire!")
print("")
print("1. Steal the chocolate milk from the infant sitting next to you.")
print("2. Drink the glass of water infront of you.")

choice = input("what will you do? (type 1 or 2)")

if choice == "1":
    import page5
elif choice == "2":
    import page6
else:
    print("invalid answer, restart ")



