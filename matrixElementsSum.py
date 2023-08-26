def solution(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            element = matrix[i][j]
            if element == 0:
                for k in range(len(matrix)):
                    matrix[k][j] = 0
            if element > 0:
                count += element
    
    
    return(count)


def validation(count,result):
    if count == result:
        print("Test Pass")
    else:
        print("Test Fail")

if __name__ == "__main__":
    
    validation(solution([[0,1,1,2],[0,5,0,0],[2,0,3,3]]),9)
    validation(solution([[1,1,1,0], [0,5,0,1], [2,1,3,10]]),9)
    validation(solution([[1,1,1], [2,2,2], [3,3,3]]),18)
    validation(solution([[0]]),0)
    validation(solution([[1,0,3], [0,2,1], [1,2,0]]),5)

