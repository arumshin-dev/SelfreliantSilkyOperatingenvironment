from random import randint
user_choice=int(input("Chooose a number between 1 and 10: "))
pc_choice=randint(1,10)
if user_choice==pc_choice:
  print("You won!")
elif user_choice>pc_choice:
  print("Lower! Correct number was", pc_choice)
elif user_choice<pc_choice:
  print("Higher! Correct number was", pc_choice)
