# true love letters and people names 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

a = name1 + name2
n = 0
s = 0
s2 = 0
point1 = ["T", "R", "U", "E","t", "r", "u", "e"] 
point2 = ["L", "O", "V", "E", "l", "o", "v", "e"]
while n != len(a) :
  n = n + 1
  char = a[len(a)-n]
  if char in point1 :
    s = s + 1
  else : s = s

  if char in point2 :
    s2 = s2 + 1
  else : s2 = s2

i = int(str(s) + str(s2))
if i<10 or i>90 :
    print("Your score is "+str(i)+", you go together like coke and mentos.")
elif 40<i<50 :
    print("Your score is "+str(i)+", you are alright together.")
else : print("Your score is "+str(i))

# .count kullanarak saydırmıştı harfleri
# etc.
#a = "Ahmeta"
#print(a.count("t"))
#=>> 2