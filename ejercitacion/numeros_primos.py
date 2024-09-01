def divisores (a):
    div = [1,a];
    div += [i for i in range(2, (a//2)+1) if a % i == 0]
    return sorted(div)

def numeros_primos (a):
    return len(divisores(a)) == 2;

for i in range (1,100):
    if numeros_primos(i):
        print(i)