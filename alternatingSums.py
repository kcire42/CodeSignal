# Several people are standing in a row and need to be divided into two teams. 
# The first person goes into team 1, the second goes into team 2, the third goes into
# team 1 again, the fourth into team 2, and so on.

# You are given an array of positive integers - the weights of the people. 
# Return an array of two integers, where the first element is the total weight of team 1, 
# and the second element is the total weight of team 2 after the division is complete.


def solution(a):

    team_1 = 0
    team_2 = 0
    for element in range(len(a)):
        id = element+1
        if id%2 == 0:
            team_2 += a[element] 
        else:
            team_1 += a[element]

    return [team_1,team_2]


def testing(intput,output):
    if input == output:
        print("Test Pass")

    else:
        print("Test Fail")
    print(f"Input: {intput} Output: {output}") 

if __name__ == "__main__":
    testing(solution([50, 60, 60, 45, 70]),[180, 105])