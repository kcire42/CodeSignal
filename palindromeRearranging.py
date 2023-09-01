def palindromeRearranging(inputString):
    count_letters = {}
    for letra in inputString:
        if letra in count_letters:
            count_letters[letra] += 1
        else:
            count_letters[letra] = 1
    count_odd = 0 
    for element in count_letters:
        if count_letters[element] %2 != 0:
            count_odd += 1
     
    if count_odd <= 1:
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
    testing(palindromeRearranging("aabb"),True)
    testing(palindromeRearranging("a"),True)
    testing(palindromeRearranging("ab"),False)
    testing(palindromeRearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"),False)
    testing(palindromeRearranging("zyyzzzzz"),True)
    testing(palindromeRearranging("zaa"),True)