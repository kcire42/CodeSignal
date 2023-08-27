# You are given an array of integers. 
# On each move you are allowed to increase exactly one of its element by one. 
# Find the minimal number of moves required to obtain a strictly increasing sequence 
# from the input.

def solution(inputArray):
    # n = len(inputArray)
    # count = 0
    # print(inputArray)
    # for i in range(n):
    #     for j in range(0,n-i-1):
    #         if inputArray[j] > inputArray[j+1]:
    #             count += 1
    #             inputArray[j], inputArray[j+1] = inputArray[j+1], inputArray[j]
                
    # print(inputArray)
    # return count
    moves = 0
    prev_num = inputArray[0]

    for num in inputArray[1:]:
        if num <= prev_num:
            moves += prev_num - num + 1
            prev_num += 1
        else:
            prev_num = num

    return moves


def testing(input,output):
    if input == output:
        print("Test Pass")
    else:
        print("Test Fail")
    print(f"Input: {input}, Output: {output}")


if __name__ =="__main__":
    testing(solution([1,1,1]),3)
    testing(solution([-1000,0,-2,0]),5)
