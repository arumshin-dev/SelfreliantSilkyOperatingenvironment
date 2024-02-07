def plus(a=0,b=0):
  
  print(f"{a} + {b} =",a+b)
  print(f"{a} + {b} = {a+b}")

#plus()
#plus(1,2)

def tax_calc(money):
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying",tax)

to_pay = tax_calc(1500000000)
#pay_tax(to_pay)
#pay_tax(tax_calc(1800000))

def make_juice(fruit):
  return f"🍹{fruit}+🥤"

def add_ice(juice):
  return f"🧊{juice}+🧊"

def add_sugar(iced_juice):  
  return f"🍬{iced_juice}+🍬" 
juice = make_juice("🍎")
cold_juice = add_ice(juice)  
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)