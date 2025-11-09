# Fibonacci using Dynamic Programming (Bottom-Up Approach)

def fibonacci_dp(n):
    step_count = 0  # To count computation steps

    # Base conditions
    if n <= 0:
        print("Invalid input! Enter a positive integer.")
        return None, step_count
    elif n == 1:
        return [0], 1
    elif n == 2:
        return [0, 1], 2

    # Initialize array to store Fibonacci numbers
    fib = [0, 1]

    # Build the series from bottom up
    for i in range(2, n):
        step_count += 1
        fib.append(fib[i - 1] + fib[i - 2])

    return fib, step_count


# Main Program
n = int(input("Enter how many terms you want: "))
fib_series, steps = fibonacci_dp(n)

print(f"\nFibonacci Series up to {n} terms:")
print(fib_series)
print(f"\nTotal Steps Taken = {steps}")
