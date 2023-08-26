def solution(sequence):
    count = 0 
    for i in range(len(sequence)-1):
        if sequence[i] > sequence[i+1]:
            count += 1
            if count > 1:
                return False
        if i == 0 or sequence[i -1] < sequence[i+1]:
            sequence[i] = sequence[i +1] -1
        else:
            sequence[i+1] = sequence[i] + 1
    return True
        
def test(result, answer):
    if result == answer:
        print("Test Pass")
    else:
         print("Test Fail")
    
     

if  __name__ == '__main__':
    test(solution([1, 3, 2, 1]),False)
    test(solution([1, 3, 2]),True)
    test(solution([1, 1, 2, 3, 4, 4]),False)
    test(solution([1, 2, 1, 2]),False)
    test(solution([10, 1, 2, 3, 4, 5]),True)


