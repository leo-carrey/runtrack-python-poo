def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

userinput = input("entrer un nombre entier :")
print(factorielle(int(userinput)))