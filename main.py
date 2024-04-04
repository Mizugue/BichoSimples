import random


def menu():
    print(
        "=====================================================================================================================================")
    print(
        "                             🍀🍀🍀       BEM VINDO AOS PALPITES DO JOGO DO BICHO     🍀🍀🍀                                                                                  ")
    print(
        "=====================================================================================================================================")
    print(
        "                                                                                                                                 by 𝘫𝘤")
    print("")
    while True:
        escolha = (input("Voce deseja receber um novo palpite?(sim/nao):  "))
        if escolha == 'sim':
            numeros = [x for x in range(0, 9999)]
            a = random.choice(numeros)
            b = random.choice(numeros)
            c = random.choice(numeros)
            d = random.choice(numeros)
            e = random.choice(numeros)

            if a < 1000 and a > 99:
                numero = str(a)
                dezena1 = int(numero[1:3])
            elif a > 999:
                numero = str(a)
                dezena1 = int(numero[2:4])
            elif a > 9 and a < 100:
                numero = str(a)
                dezena1 = int(numero)
            else:
                numero = str(a)
                dezena1 = int(numero[0::2])

            if b < 1000 and b > 99:
                numero = str(b)
                dezena2 = int(numero[1:3])
            elif b > 999:
                numero = str(b)
                dezena2 = int(numero[2:4])
            elif b > 9 and b < 100:
                numero = str(b)
                dezena2 = int(numero)
            else:
                numero = str(b)
                dezena2 = int(numero[0::2])

            if c < 1000 and c > 99:
                numero = str(c)
                dezena3 = int(numero[1:3])
            elif c > 999:
                numero = str(c)
                dezena3 = int(numero[2:4])
            elif c > 9 and c < 100:
                numero = str(c)
                dezena3 = int(numero)
            else:
                numero = str(c)
                dezena3 = int(numero[0::2])

            if d < 1000 and d > 99:
                numero = str(d)
                dezena4 = int(numero[1:3])
            elif d > 999:
                numero = str(d)
                dezena4 = int(numero[2:4])
            elif d > 9 and d < 100:
                numero = str(d)
                dezena4 = int(numero)
            else:
                numero = str(d)
                dezena4 = int(numero[0::2])

            if e < 1000 and e > 99:
                numero = str(e)
                dezena5 = int(numero[1:3])
            elif e > 999:
                numero = str(e)
                dezena5 = int(numero[2:4])
            elif e > 9 and e < 100:
                numero = str(e)
                dezena5 = int(numero)
            else:
                numero = str(e)
                dezena5 = int(numero[0::2])

            animais = {'avestruz': [1, 2, 3, 4], 'aguia': [5, 6, 7, 8], 'burro': [9, 10, 11, 12],
                       'borboleta': [13, 14, 15, 16],
                       'cachorro': [17, 18, 19, 20], 'cabra': [21, 22, 23, 24], 'carneiro': [25, 26, 27, 28],
                       'camelo': [29, 30, 31, 32], 'cobra': [33, 34, 35, 36], 'coelho': [37, 38, 39, 40],
                       'cavalo': [41, 42, 43, 44],
                       'elefante': [45, 46, 47, 48], 'galo': [49, 50, 51, 52], 'gato': [53, 54, 55, 56],
                       'jacare': [57, 58, 59, 60],
                       'leao': [61, 62, 63, 64], 'macaco': [65, 66, 67, 68], 'porco': [69, 70, 71, 72],
                       'pavao': [73, 74, 75, 76],
                       'peru': [77, 78, 79, 80], 'touro': [81, 82, 83, 84], 'tigre': [85, 86, 87, 88],
                       'urso': [89, 90, 91, 92],
                       'veado': [93, 94, 95, 96], 'vaca': [97, 98, 99, 0]}
            animal1 = ''
            animal2 = ''
            animal3 = ''
            animal4 = ''
            animal5 = ''

            for chave, valor in animais.items():
                for unidade in valor:
                    if dezena1 == unidade:
                        animal1 = chave
            for chave, valor in animais.items():
                for unidade in valor:
                    if dezena2 == unidade:
                        animal2 = chave
            for chave, valor in animais.items():
                for unidade in valor:
                    if dezena3 == unidade:
                        animal3 = chave
            for chave, valor in animais.items():
                for unidade in valor:
                    if dezena4 == unidade:
                        animal4 = chave
            for chave, valor in animais.items():
                for unidade in valor:
                    if dezena5 == unidade:
                        animal5 = chave

            print(f"1° {a} - {animal1}")
            print(f"2° {b} - {animal2}")
            print(f"3° {c} - {animal3}")
            print(f"4° {d} - {animal4}")
            print(f"5° {e} - {animal5}")



        elif escolha == 'nao':
            print("Obrigado e boa sorte!")
            exit()
        else:
            print("Nao existe essa opcao!")


if __name__ == "__main__":
    menu()