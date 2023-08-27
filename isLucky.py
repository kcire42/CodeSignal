# Ticket numbers usually consist of an even number of digits. 
# A ticket number is considered lucky if the sum of the first
# half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

def solution(n):
    n = str(n)
    len_str = int(len(n)/2)
    first= n[0:len_str]
    last = n[len_str::]  
    sum_1 = 0
    sum_2 = 0
    for i in range(len(first)):
        sum_1 += int(first[i])
        sum_2 += int(last[i])
    
    if sum_1 == sum_2:
        return True
    else:
        return False

def testing(problem,solution):
    if problem == solution:
        print("Test Pass")
    else:
        print("Test Fail")  


if __name__ == "__main__":
    testing(solution(1230),True)
    testing(solution(239017),False)
    testing(solution(134008),True)
    testing(solution(10),False)