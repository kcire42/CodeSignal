# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def solution(picture):
    border_matrix = ['*'+row+'*' for row in picture]
    #print(border_matrix)
    border_matrix.insert(0,'*'*len(border_matrix[0]))
    border_matrix.append('*'*len(border_matrix[0]))
    return border_matrix

def testing(input,output):
    if input == output:
        print("Test Pass")
    else:
        print("Test Fail")




if __name__ == "__main__":
    testing(solution(["abc","ded"]),["abc","ded"])
    testing(solution(["a"]),["***","*a*", "***"])

