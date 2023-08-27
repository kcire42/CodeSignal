# Some people are standing in a row in a park. 
# There are trees between them which cannot be moved. 
# Your task is to rearrange the people by their heights 
# in a non-descending order without moving the trees. 
# People can be very tall!

def solution(a):

    #print(a)
    people_heights = [h for h in a if h != -1]
    #print(people_heights)
    sorted_heights = sorted(people_heights)
    #print(sorted_heights)
    sorted_index = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sorted_heights[sorted_index]
            sorted_index += 1
    return a 
    
    
    


            
    
    






if __name__ == "__main__":
    
    solution([-1, 150, 190, 170, -1, -1, 160, 180])