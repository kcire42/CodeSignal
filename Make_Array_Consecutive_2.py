def solution(statues):
    components = sorted(statues)
    target = 0
    for id in range(len(components)-1):
        dummy = components[id+1]-1
        if components[id] != dummy:
            diff = (components[id+1]-components[id])-1
            target = target+diff
    
            
    return target

    
def testing(fc_answer,correct_answer):
    if fc_answer == correct_answer:
        print(f"La respuesta es correcta {fc_answer}")
    else:
        print(f"ERROR RESPUESTA INCORRECTA DEBERIA DE SER {correct_answer}")

if __name__ == '__main__':
    #statues = list(map(int,input("Ingrese la lista de numeros").split()))
    testing(solution([6,2,3,8]),3)
    testing(solution([0,3]),2)
    testing(solution([5,4,6]),0)
    testing(solution([6,3]),2)
    