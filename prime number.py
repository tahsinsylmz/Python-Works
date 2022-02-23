#prime number test
def prime_checker(number, a=2, c=0):
    
    while number > a :
        if number % a == 0 :
            number = a
            c = 1
        else :
            a += 1
            c = 0
    if c == 1 :
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)