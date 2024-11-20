# Fibonacci Series in Python

a = 0
b = 1

n = int(input("Enter the number of terms: "))

if n == 1:
    print(a)

else:
    print(a, b , end=" ")
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        
        print(c , end=" ")

