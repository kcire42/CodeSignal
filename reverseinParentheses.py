def solution(inputString):
    # var = inputString.replace('(','-#').replace(')','#-')
    # var2 = var.split('-')
    # #print(var2)
    # new_string = []
    # for i in range(len(var2)):
    #     target = var2[i]
    #     if '#' in target:
    #         new_string.append(target[::-1].replace('#',''))
    #     else:
    #         new_string.append(target)
    # reverse = ''.join(new_string)
    # print(reverse)
    # return reverse
    stack = []
    result = ""
    
    for char in inputString:
        if char == '(':
            stack.append(result)
            result = ""
        elif char == ')':
            popped = stack.pop()
            result = popped + result[::-1]
        else:
            result += char
    
    return result
    
def testing(input,output):
    if input == output:
        print("Test Pass")
    else:
        print("Test Fail")

if __name__ == "__main__":
    
    testing(solution("foo(bar)baz(blim)"),"foorabbazmilb")
    testing(solution('foo(bar(baz))blim'),'foobazrabblim')