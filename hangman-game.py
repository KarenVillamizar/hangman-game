from itertools import combinations_with_replacement
import os

def run():

    datos = []
    with open("./data.txt", "r", encoding="utf 8") as f:
        for line in f:
            datos.append(line.strip())


    for dato in datos: #recorre la lista de palabras
        word = dato
        #w = list(enumerate(word))
        n = len(word) #inica cantidad de caracteres en la cadena 
        lines = [] #lineas mostradas en consola
        for i in range(0, n):
                lines.append('_ ')
        c2 = 0 # contador caracteres adivinados
        dif = n # caracteres por divinar
        while dif != 0:
            os.system ("clear")
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
    print("Fin")


if __name__ == '__main__':
    run()



    