# Code Signal Solutions
# Arrays - firstNotRepeatingCharacter
# Jaedin Davasligil (2024)

# PROBLEM
# Given a string s consisting of small English letters, find and return the 
# first instance of a non-repeating character in it. If there is no such 
# character, return '_'.

# SOLUTION [Time: O(n) Space: O(1)]
# Use a dictionary (hashmap) to keep track of the number of occurrences of each
# character. Then, find the first character with only one occurrence.
def solution(s):
    occurrences = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0
        }
    
    for c in s:
        occurrences[c] += 1
    
    for c in s:
        if occurrences[c] == 1:
            return c
    
    return '_'

# TESTS
def test_solution():
    s1 = "abacabad"
    s2 = "abacabaabacaba"

    assert solution(s1) == 'c'
    assert solution(s2) == '_'

    print("Tests completed.")

# MAIN
if __name__ == "__main__":
    test_solution()
