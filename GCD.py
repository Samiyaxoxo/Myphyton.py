def find_gcd(a, b):
    gcd = 1  
    for i in range(1, min(a, b) + 1): 
        if a % i == 0 and b % i == 0:  
            gcd = i  
    return gcd
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"GCD of {num1} and {num2} is {find_gcd(num1, num2)}")
print("samiya,23")
