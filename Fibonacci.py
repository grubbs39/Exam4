import time

def FibonacciRecursion(n):
    if n<0:
        print("Incorrect input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return FibonacciRecursion(n-1)+FibonacciRecursion(n-2)

def FibonacciIteratively(n):
    x = 0
    y = 1
    z = 1
    for i in range(0, n):
        x = y;
        y = z;
        z = x + y;
    return x;

num = int(input("Enter the last element of Fibonacci sequence: "))

start1 = time.time()
print("Recursion:", FibonacciRecursion(num))
end1 = time.time()
print(f"Runtime of the program is {end1 - start1}")

start2 = time.time()
print("Iteratively:", FibonacciIteratively(num))
end2 = time.time()
print(f"Runtime of the program is {end2 - start2}")
