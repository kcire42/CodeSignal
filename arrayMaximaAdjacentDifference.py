# Given an array of integers, find the maximal absolute 
# difference between any two of its adjacent elements.

def arrayMaximalAdjacentDifference(inputArray):

    diff_array = []
    for element in range(len(inputArray)-1):
        diff = inputArray[element]-inputArray[element+1]
        if diff < 0:
            diff_array.append(diff*-1)
        else:
            diff_array.append(diff)
    diff_array.sort(reverse=True)
    return diff_array[0]
            





def testing(input,output):
    if input == output:
        print("Test Pass")
    else:
        print("Test Fail")
    print(f"Input: {input}, Output: {output}")


if __name__ == "__main__":
    testing(arrayMaximalAdjacentDifference([2,4,1,0]),3)