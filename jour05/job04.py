def Fibonacci(pos, n=1, n2=0):
    if pos > 2:
        return Fibonacci(pos - 1, n + n2, n)
    
    return n


fibPos = int(input("Bing chilling number: "))
print(Fibonacci(fibPos))