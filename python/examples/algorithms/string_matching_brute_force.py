# brute_force_string_matching function: Implements the Brute Force String Matching Algorithm.
# text: The text in which the pattern is to be searched.
# pattern: The pattern to be searched for in the text.
# The function iterates through the text and compares each substring of length equal to the pattern
# with the pattern itself.
# If a substring matches the pattern completely, the index of the starting position of the match is recorded.
# Example usage: Demonstrates how to use the brute_force_string_matching function to find occurrences
# of a pattern in a text.

# The Brute Force String Matching Algorithm compares the pattern with every possible substring of the
# text, one by one, to find occurrences of the pattern. It has a time complexity of O((n - m + 1) * m),
# where n is the length of the text and m is the length of the pattern.

def brute_force_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):  # Iterate through text
        j = 0
        while j < m and text[i + j] == pattern[j]:  # Compare characters
            j += 1
        if j == m:  # If pattern matches completely
            matches.append(i)

    return matches


# Example usage:
if __name__ == "__main__":
    text = "ABABCABABABAABCABAB"
    pattern = "ABABA"
    matches = brute_force_string_matching(text, pattern)

    if matches:
        print("Pattern found at indices:", matches)
    else:
        print("Pattern not found in the text")
