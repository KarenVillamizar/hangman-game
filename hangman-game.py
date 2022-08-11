from itertools import combinations_with_replacement


def run():
    word = "cama"
    #w = list(enumerate(word))
    n = len(word)
    dif = n
    lines = []
    c2 = 0
    for i in range(0, n):
            lines.append('_ ')
    while dif != 0:
        print("Adivina la palabra :)")
        print(*lines)
        letter = input("ingresa una letra:")
        c = 0
        for i in word:
            c = c + 1
            if letter == i:
                c2 = c2 + 1 
                lines[c-1] = letter
        dif = n - c2
    print(*lines)
    print("Ganaste!")




if __name__ == '__main__':
    run()



    