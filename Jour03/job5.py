def nbrpremiers(n):
    for i in range(2, n):
            if n % i == 0:
                return False
    return True

for x in range(2, 1000):
    if nbrpremiers(x):
        print(x)