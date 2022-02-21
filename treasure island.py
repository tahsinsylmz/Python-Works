import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

#two digit number
position = input("Where do you want to put the treasure? ")

i = int(position[1])
j = int(position[0]) - 1
if i == 1 :
  row1[j] = "x"
elif i == 2 :
  row2[j] = "x"
else :
  row3[j] = "x"


print(f"{row1}\n{row2}\n{row3}")