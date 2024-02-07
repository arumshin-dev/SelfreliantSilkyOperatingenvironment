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
pay_tax(to_pay)