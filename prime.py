try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit() 

is_prime = True

if num <= 1:
    is_prime = False
elif num == 2:
    is_prime = True
elif num % 2 == 0:  
    is_prime = False
else:
    i = 3
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break  
        i += 2

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")