# An example of the 0/1 Knapsack Problem solved using dynamic programming in Python:

# knapsack function: Implements the 0/1 Knapsack Problem using dynamic programming.
# weights: A list of weights of the items.
# values: A list of values of the items.
# capacity: The maximum weight capacity of the knapsack.
# The function initializes a 2D array dp to store maximum values for different capacities and items.
# It iterates through each item and each possible capacity, filling the dp array according to the knapsack recurrence relation.
# After filling the dp array, it reconstructs the items included in the knapsack by tracing back the items from the dp array.

# Example usage: Demonstrates how to use the knapsack function to find the maximum value of items that can be
# included in the knapsack, along with the items included.

# The 0/1 Knapsack Problem is solved using dynamic programming by breaking it down into smaller subproblems and
# storing the solutions to avoid redundant calculations. The time complexity of the knapsack algorithm using
# dynamic programming is O(n * capacity), where n is the number of items and capacity is the maximum weight
# capacity of the knapsack.

def knapsack(weights, values, capacity):
    n = len(weights)

    # Initialize a 2D array to store maximum values for different capacities and items
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the dp array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # If the current item can be included
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            # If the current item cannot be included
            else:
                dp[i][j] = dp[i - 1][j]

    # Reconstruct the items included in the knapsack
    included_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        # If the value comes from the previous item, skip the current item
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        # If the value comes from including the current item, add it to the included items
        else:
            included_items.append(i - 1)
            j -= weights[i - 1]
            i -= 1

    # Reverse the included items list to get the correct order
    included_items.reverse()

    return dp[n][capacity], included_items


# Example usage:
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    max_value, items = knapsack(weights, values, capacity)
    print("Maximum value of items in the knapsack:", max_value)
    print("Items included in the knapsack:", items)
