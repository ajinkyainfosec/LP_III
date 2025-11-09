# Fibonacci using iteration with step count

def fibonacci(n):
    step_count = 0  # To count number of steps
    
    # Base cases
    if n <= 0:
        print("Invalid input! Enter a positive integer.")
        return None, step_count
    elif n == 1:
        step_count += 1
        return 0, step_count
    elif n == 2:
        step_count += 1
        return 1, step_count
    
    # Iterative calculation
    a, b = 0, 1
    for i in range(2, n):
        step_count += 1
        c = a + b
        a, b = b, c
    
    return b, step_count


# Main program
n = int(input("Enter the term number (n): "))
fib_num, steps = fibonacci(n)
print(f"\nFibonacci({n}) = {fib_num}")
print(f"Total Steps Taken = {steps}")
