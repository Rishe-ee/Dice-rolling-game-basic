import random
print("Do you want me to Roll the Dice for you(yes/no)")
userWish=input().lower()
if userWish == "y" :
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print({die1},{die2})
elif userWish == "n" :
    print("Thanks for playing !!")
else :
    print("Invalid Choice") 