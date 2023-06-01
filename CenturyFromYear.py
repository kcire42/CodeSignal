def centuryfromyear(year):
    if (year <= 0):
        raise Exception("No numeros negativos")
    elif(year <= 100):
        return 1
    elif (year % 100 == 0):
        return int(year/100)
    elif (year % 100 !=0):
        century = int(year/100)
        return century+1
    
    


if __name__ =="__main__":
    year = int(input("Ingrese el año"))
    print(centuryfromyear(year))
