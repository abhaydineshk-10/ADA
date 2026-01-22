number=float(input("Enter a number: "))
guess=number/2
while (guess*guess>number):
    guess= guess- 0.00001
    
print("The square root of", number, "is approximately", guess)