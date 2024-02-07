from random import randint
print("Welcome to the Number Guessing Game!")
pc_choice=randint(1,10)
playing=True
while playing:
  user_choice=int(input("Chooose a number between 1 and 10: "))
  if user_choice==pc_choice:
    print("You won!")
    playing=False
  elif user_choice>pc_choice:
    print("Lower!")
  elif user_choice<pc_choice:
    print("Higher!")

print("Game over! Thank you for playing!")