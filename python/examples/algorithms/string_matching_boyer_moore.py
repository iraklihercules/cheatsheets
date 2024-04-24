# bad_character_table function: Generates the bad character table for the given pattern.
# The bad character table stores the rightmost position of each character in the pattern,
# except for the last character.
# If a mismatch occurs during the matching process, the algorithm uses this table to determine
# how far to shift the pattern based on the mismatched character in the text.

# good_suffix_table function: Generates the good suffix table for the given pattern.
# The good suffix table stores the shift values to be applied when a mismatch occurs between
# the pattern and the text.
# It calculates the shift values based on the longest suffix of the pattern that matches a prefix of the pattern.

# boyer_moore function: Implements the Boyer-Moore Algorithm for string matching.
# The function iterates through the text, attempting to match the pattern against substrings of the text.
# It uses the bad character table and the good suffix table to efficiently determine the shift
# values when a mismatch occurs.
# When a match is found, the function records the starting index of the match.

# Example usage: Demonstrates how to use the boyer_moore function to find occurrences of a pattern in a text.

# The Boyer-Moore Algorithm achieves efficient string matching by utilizing both the bad character
# rule and the good suffix rule to determine the optimal shift values during the matching process.
# It has a time complexity of O(n + m), where n is the length of the text and m is the length of the pattern.

def bad_character_table(pattern):
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - 1 - i
    return table


def good_suffix_table(pattern):
    m = len(pattern)
    suffixes = [0] * m
    shift = 1

    for i in range(m - 2, -1, -1):
        while shift <= i + 1 and pattern[i] != pattern[i + 1 - shift]:
            shift += suffixes[i + 1 - shift]
        suffixes[i] = shift

    for i in range(m - 1):
        suffixes[i] = m - suffixes[i]

    return suffixes


def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    bc_table = bad_character_table(pattern)
    gs_table = good_suffix_table(pattern)
    matches = []

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j == -1:
            matches.append(i)
            i += gs_table[0]
        else:
            i += max(bc_table.get(text[i + j], 0), gs_table[j])

    return matches


# Example usage:
if __name__ == "__main__":
    text = "ABABCABABABAABCABAB"
    pattern = "ABABA"
    matches = boyer_moore(text, pattern)

    if matches:
        print("Pattern found at indices:", matches)
    else:
        print("Pattern not found in the text")
