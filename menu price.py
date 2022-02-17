
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = {'S':15,'M':20,'L':25,'Y':1,'N':0}
if add_pepperoni == "Y":
    if size == "S" :
        add_pepperoni = 2
    else:
        add_pepperoni = 3
else: add_pepperoni = 0
a = price[size] + price[extra_cheese] + add_pepperoni
print("Your final bill is: $" + str(a) + ".")