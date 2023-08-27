# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# solution(inputArray) = ["aba", "vcd", "aba"].

def solution(inputArray):
    inputArray.sort(key=len, reverse=True )
    outputArray = []
    for i in range(len(inputArray)):
        
        if len(inputArray[i]) == len(inputArray[0]):
            outputArray.append(inputArray[i])
    
    return outputArray


def testing(array,answer):
    if array == answer:
        print("Test Pass")
    else:
        print("Test Fail")


if __name__ == "__main__":
    testing(solution(["aba", "aa", "ad", "vcd", "aba"]),["aba", "vcd", "aba"])
    testing(solution(["aa"]),["aa"])
    testing(solution(["abc", "eeee", "abcd", "dcd"]),["eeee", "abcd"])