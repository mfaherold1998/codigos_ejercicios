def divisores (a):
    div = [1,a];
    div += [i for i in range(2, a//2) if a % i == 0]
    return sorted(div)

def numeros_primos (a):
    return len(divisores(a)) == 2;

lqqjwndicvbfei