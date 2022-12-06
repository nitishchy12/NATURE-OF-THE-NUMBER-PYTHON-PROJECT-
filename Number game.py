import random
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a = random.randrange(a,b+1)
if a>0:
    print(a,"is a positive number.")
else:
    print(a,"is a negative number.")    
if a%2 == 0:
    print(a,"is an even number.")    
else:
    print(a,"is an odd number.")    
x = True
for i in range(2,a):
    if a%i == 0:
        x = True
        break
    else:
        x = False
if x == True:
    print(a,"is a composite number.")           
else:
    print(a,"is a prime number.")