# You are given an array of integers representing coordinates of
# obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 
#     to the right. You are allowed only to make jumps of the same 
#     length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.
import math
from functools import reduce


def avoidObstacles(inputArray):
    max_obstacle = max(inputArray)
    jump_length = 1

    while True:
        jump_success = True
        position = 0

        while position <= max_obstacle:
            if position in inputArray:
                jump_success = False
                break
            position += jump_length

        if jump_success:
            return jump_length

        jump_length += 1



def testing(input,output):
    if input == output:
        print("Test Pass")
    else:
        print("Test Fail")
    print(f"Input: {input}, Output: {output}")


if __name__ == "__main__":
    testing(avoidObstacles([5,3,6,7,9]),4)






# 0
# 1
# 2
# 3
# 4-
# 5
# 6
# 7
# 8
# 9
# 10