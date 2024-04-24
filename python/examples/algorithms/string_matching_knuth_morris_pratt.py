# compute_prefix_function function: Computes the prefix function (pi) for the given pattern.
# The prefix function pi[q] stores the length of the longest proper prefix of pattern[:q+1] that
# is also a suffix of pattern[:q+1].
# The function iterates through the pattern, updating the prefix function values based on the
# comparison of characters.

# kmp function: Implements the Knuth-Morris-Pratt algorithm for string matching.
# text: The text in which the pattern is to be searched.
# pattern: The pattern to be searched for in the text.
# The function uses the computed prefix function to efficiently skip unnecessary comparisons during
# the string matching process.
# It iterates through the text, comparing characters with the pattern while utilizing the prefix
# function to determine the next character to compare.
# When a match is found, the function records the starting index of the match.

# Example usage: Demonstrates how to use the kmp function to find occurrences of a pattern in a text.

# The Knuth-Morris-Pratt algorithm achieves efficient string matching by utilizing the information
# about the occurrences of the pattern within itself (i.e., the prefix function) to avoid unnecessary
# comparisons during the search process. It has a time complexity of O(n + m), where n is the length
# of the text and m is the length of the pattern.

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k

    return pi


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    matches = []

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = pi[q - 1]

    return matches


# Example usage:
if __name__ == "__main__":
    text = "ABABCABABABAABCABAB"
    pattern = "ABABA"
    matches = kmp(text, pattern)

    if matches:
        print("Pattern found at indices:", matches)
    else:
        print("Pattern not found in the text")
