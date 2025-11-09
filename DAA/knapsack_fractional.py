# Fractional Knapsack Problem using Greedy Approach

def fractional_knapsack(value, weight, capacity):
    n = len(value)
    ratio = []  # value/weight ratio list

    # Step 1: Calculate value/weight ratio
    for i in range(n):
        ratio.append((value[i] / weight[i], value[i], weight[i]))

    # Step 2: Sort items based on ratio in descending order
    ratio.sort(reverse=True)

    total_value = 0  # Maximum value in knapsack
    for r, v, w in ratio:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            # Take fraction of remaining item
            total_value += r * capacity
            break

    return total_value


# Main Program
n = int(input("Enter number of items: "))
value = []
weight = []

for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    value.append(v)
    weight.append(w)

capacity = float(input("Enter knapsack capacity: "))

max_value = fractional_knapsack(value, weight, capacity)
print(f"\nMaximum value in Knapsack = {max_value:.2f}")
