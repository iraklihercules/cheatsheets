# An example of the Longest Common Subsequence (LCS) problem solved using dynamic programming in Python:

# longest_common_subsequence function: Implements the LCS problem using dynamic programming.
# text1 and text2: The input strings for which the LCS needs to be found.
# The function initializes a 2D array dp to store lengths of LCS. dp[i][j] represents the length of
# LCS between text1[:i] and text2[:j].
# It iterates through each character of both strings and fills the dp array according to the LCS recurrence
# relation.
# After filling the dp array, it reconstructs the LCS string by tracing back the longest common subsequence
# from the dp array.

# Example usage: Demonstrates how to use the longest_common_subsequence function to find the longest common
# subsequence between two strings.

# Dynamic programming is used to efficiently solve the LCS problem by breaking it down into smaller
# subproblems and storing the solutions to avoid redundant calculations. The time complexity of the
# LCS algorithm using dynamic programming is O(m * n), where m and n are the lengths of the input strings.

def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    # Initialize a 2D array to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp array using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from dp array
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs = text1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs


# Example usage:
if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    lcs = longest_common_subsequence(text1, text2)
    print("Longest Common Subsequence (LCS):", lcs)  # Output: "ace"
