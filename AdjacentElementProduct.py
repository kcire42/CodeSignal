def solution(inputArray):
    largest_product = inputArray[0]*inputArray[1]
    for element in range(len(inputArray)-1):
        product = inputArray[element]*inputArray[element+1]
        if product > largest_product:
            largest_product = product
        else:
            continue
    return largest_product




if __name__ == '__main__':
    inputArray = list(map(int,input().split()))
    solution(inputArray)