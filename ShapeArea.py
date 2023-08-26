def shapeArea(n):
    if n == 1:
        return 1
    result = (n*n) + ((n-1)*(n-1))
    return result


if __name__ == "__main__":
    n = int(input("Ingresar el numero de cuadros"))
    print(shapeArea(n))