a=int(input("Enter first number:"))
b=int(input("Enter first number:"))
c=int(input("Enter first number:"))

if(a>=b)and(a>=c):
    largest=a
elif(b>=a)and(b>=c):
    largest=b
else:
    largest=c

print("The largest number is",largest)