# Call two arms equally strong if the heaviest weights they each are able
# to lift are equal.

# Call two people equally strong if their strongest arms are equally 
# strong (the strongest arm can be both the right and the left), and 
# so are their weakest arms.

# Given your and your friend's arms' lifting capabilities find out 
# if you two are equally strong.

def areEquallyStrong(yourLeft,yourRight,friendsLeft,friendsRight):
    you = {yourLeft,yourRight}
    friend = {friendsLeft,friendsRight}
   
    if you == friend:
        return True
    else:
        return False



def testing(input,output):
    if input == output:
        print("Test Pass")
    else:
        print("Test Fail")
    print(f"Input: {input}, Output: {output}")




if __name__ == "__main__":
    testing(areEquallyStrong(10,15,15,10),True)
    testing(areEquallyStrong(15,10,15,10),True)
    testing(areEquallyStrong(15,10,15,9),False)
    testing(areEquallyStrong(10,15,5,20),False)
    testing(areEquallyStrong(10,5,5,10),True)
    