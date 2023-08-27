# Two arrays are called similar if one can be obtained from another
# by swapping at most one pair of elements in one of the arrays.

# Given two arrays a and b, check whether they are similar.


def solution(a,b):
    
    if len(a) != len(b):
        return False
    
    for element in a:
        if element in b:
            b.remove(element)
            continue    
        else:
            return False
    return True




def testing(input,output):
    if input == output:
        print("Test Pass")
    else:
        print("Test Fail")


if __name__ == "__main__":
    testing(solution([1,2,3],[2,1,3]),True)
    testing(solution([1,2,2],[2,1,1]),False)
    testing(solution([1,2,1,2],[2,2,1,1]),True)
    testing(solution([832, 998, 148, 570, 533, 561, 894, 147, 455, 279],[832, 570, 147, 998, 533, 561, 455, 147, 894, 279]),False)
   