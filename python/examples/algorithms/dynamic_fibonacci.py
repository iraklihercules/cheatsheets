# An example of the Fibonacci series algorithm implemented using dynamic programming in Python:

# fibonacci function: Implements the Fibonacci series algorithm using dynamic programming.
# n: The index of the Fibonacci number to be calculated.
# The function initializes an array fib with the first two Fibonacci numbers (0 and 1).
# It iterates from the third Fibonacci number to the n-th Fibonacci number, calculating each Fibonacci
# number by adding the two previous Fibonacci numbers.
# By using dynamic programming and storing previously calculated Fibonacci numbers, it avoids redundant
# calculations and improves efficiency.

# Example usage: Demonstrates how to use the fibonacci function to calculate the n-th Fibonacci number.

# Dynamic programming is a technique used to efficiently solve problems by breaking them down into simpler subproblems
# and storing the solutions to subproblems to avoid redundant calculations. In the case of the Fibonacci series,
# dynamic programming helps to optimize the time complexity from exponential to linear.

def fibonacci(n):
    # Initialize an array to store Fibonacci numbers
    fib = [0, 1]

    # Calculate Fibonacci numbers using dynamic programming
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]


# Example usage:
if __name__ == "__main__":
    n = 10
    print(f"The {n}-th Fibonacci number is:", fibonacci(n))  # Output: The 10-th Fibonacci number is: 55
