i = 0
def len(string, i):
    if string == "":
        print(i)
    else:
        i += 1
        len(string[:-1], i)

len("récursivité", i)