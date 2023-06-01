def solution(inputString):
    if inputString == inputString[::-1]:
        return True
    else:
        return False



if __name__ =="__main__":
    inputString = input("Ingrese la frase")
    print(solution(inputString))