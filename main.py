age=int(input("How old are you?"))
print("You are",age,"years old")
print(type(age))
if age<10:
  print("You are a child")
elif age<20:
  print("You are a teenager")
elif age>=30 and age<=50:
  print("You are an adult")
elif age==60 or age==70:
  print("You are old")
else:
  print("You are a senior")