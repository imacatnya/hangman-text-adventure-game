name = str(input("Enter your name: "))
print(f"{name} you are stuck at work")
print(" You are still working and suddenly you saw a ghost, Now you have three options ")
print("1.run. 2.Jump from the window. 3.Try to fight the ghost")
user  = int(input("Choose 1  2 or 3: "))
if user == 1:
    print("You did it you tell your boss to never put you on night shifts ever agian")
elif user == 2:
    print("You broke both legs your kinda dumb but you got away from the ghost but you may never walk agian") 
elif user == 3:
    print("Your dumb dont ever run this agian until you get a brain")
else:
    print("That was not a option please pick 1 2 or 3")