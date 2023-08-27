# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# solution(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

def solution(s1,s2):
    char_count = [0] * 26  # Assuming only lowercase English letters

    for char in s1:
        char_count[ord(char) - ord('a')] += 1

    common_count = 0
    for char in s2:
        if char_count[ord(char) - ord('a')] > 0:
            common_count += 1
            char_count[ord(char) - ord('a')] -= 1

    print(common_count)

    



if __name__ == "__main__":
    solution("aabcc","adcaa")