import random
def tela_de_resumo():
    numero_escolhido_pelo_tubarao_baitola = random.randint(0, 500)
    if numero_escolhido_pelo_tubarao_baitola == numero:
        print("parabens")
        print("O Tubarão baitola escolheu o mesmo número que você!")
    else:
         print("perdeu.")
         print("Não foi dessa vez... o Tubarão baitola escolheu", numero_escolhido_pelo_tubarao_baitola)

def play():
        menu = "--Tubarão Baitola--"
        print(menu)
        global numero
        numero = input("Qual é seu número escolhido de 0 a 500? ")
        print("Você escolheu:", numero)
        tela_de_resumo()




def main():
    menu = "--Tubarão Baitola--\n 1 - Iniciar\n 2 - Fechar\n :"
    escolha = int(input(menu))
    match escolha:
        case 1:
            play()
        case 2:
            exit
               
main()
