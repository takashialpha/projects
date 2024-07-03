import random
global deuBom, numero_escolhido_pelo_tubarao_baitola, numero
def tela_de_resumo(n):
    if deuBom == True:
        print("""\n                                         _                  
           |  _ \ __ _ _ __ __ _| |__   /_/ _ __  ___ 
           | |_) / _` | '__/ _` | '_ \ / _ \ '_ \/ __|
           |  __/ (_| | | | (_| | |_) |  __/ | | \__ /
           |_|   \__,_|_|  \__,_|_.__/ \___|_| |_|___/  \n""")
        print("\n \n \n \nO Tubarão baitola escolheu o mesmo número que você!")
        input()
    else:
         print("""\ ____              _            
|  _ \ ___ _ __ __| | ___ _   _ 
| |_) / _ \ '__/ _` |/ _ \ | | |
|  __/  __/ | | (_| |  __/ |_| |
|_|   \___|_|  \__,_|\___|\__,_| """)
         print("Não foi dessa vez... o Tubarão baitola escolheu", numero_escolhido_pelo_tubarao_baitola)
         input()

def play():
        menu = """\     _                         _                                        
    | | ___   __ _  ___     __| | ___                                   
 _  | |/ _ \ / _` |/ _ \   / _` |/ _ \                                  
| |_| | (_) | (_| | (_) | | (_| | (_) |                                 
 \___/ \___/ \__, |\___/   \__,_|\___/                                  
 _         _ |___/          /\/|         _           _ _        _       
| |_ _   _| |__   __ _ _ __|/\/_  ___   | |__   __ _(_) |_ ___ | | __ _ 
| __| | | | '_ \ / _` | '__/ _` |/ _ \  | '_ \ / _` | | __/ _ \| |/ _` |
| |_| |_| | |_) | (_| | | | (_| | (_) | | |_) | (_| | | || (_) | | (_| |
 \__|\__,_|_.__/ \__,_|_|  \__,_|\___/  |_.__/ \__,_|_|\__\___/|_|\__,_|\n"""
        print(menu, """\                                                                ,.
                                                               /  \
                                                              /..-'
                                                             .'
                                      __.-,'',--,..
           ,-.                    ,-''  .',-\' / _ |
           |  |              ,,'``      //  |   '| `
           `. |          _.-' /'        | ()|  ()|(,.-'''''-.
             '`        ,'    /         --.  | '--'          /
                    _,'     /              -'      __..._ ,'
                   /       /                   _,-'    ,.-
     .-.         ,'       /       _,.....,'- .'_  ,-:-'
     \  \      .'        /       '          `.` \  \
      `. |     `..---._ /     _. --           '-._..\.
        `\             .  _,-'           ..         _/             _
         '             /,'                 :.___,,.'            ,-' |
                      ,'                '''`-                ,,'   /
                    ,'        .         ,-'|             _.-'    ,'
                   ,'       ,/        ,'   |          _,'    _.-'
                  .'    _.-'/       ,'     |         '  _.-''
.'`-.             |  ,-'   |       /  \    |       ,:,-'
'.   \            `-' |    |     ,'    \   |       '
 `.   \               |   |     /       `._/
   `.  `.             |   |    /
     `-_`.            |   |   |                          _..'
        `|.           |   |   |                     _.-''  _/
          \            \  |   |       ,,-'\        /.,---`'
           '            \ |   |   _,-'   ,'
                         \ \  |,-'      /
                 _        \ \ |       ,'
                <.`.       \ \|      /               _.""")
        print("not made by me. found in ascii art.")
        try: 
            numero = int(input("Qual é seu número escolhido de 0 a 200? "))
            numero_escolhido_pelo_tubarao_baitola = random.randint(0,200)
        except ValueError:
            print("Tem que ser número")
        except UnboundLocalError:
            print("Tem que ser número")
        finally:
            tela_de_resumo(numero)
        
        if numero == numero_escolhido_pelo_tubarao_baitola:
            deuBom = True
        else:
            deuBom = False




def main():
    menu = """\     _                         _                                        
    | | ___   __ _  ___     __| | ___                                   
 _  | |/ _ \ / _` |/ _ \   / _` |/ _ \                                  
| |_| | (_) | (_| | (_) | | (_| | (_) |                                 
 \___/ \___/ \__, |\___/   \__,_|\___/                                  
 _         _ |___/          /\/|         _           _ _        _       
| |_ _   _| |__   __ _ _ __|/\/_  ___   | |__   __ _(_) |_ ___ | | __ _ 
| __| | | | '_ \ / _` | '__/ _` |/ _ \  | '_ \ / _` | | __/ _ \| |/ _` |
| |_| |_| | |_) | (_| | | | (_| | (_) | | |_) | (_| | | || (_) | | (_| |
 \__|\__,_|_.__/ \__,_|_|  \__,_|\___/  |_.__/ \__,_|_|\__\___/|_|\__,_|\n 1 - Iniciar\n 2 - Fechar\n :"""
    while True:
        try:
            escolha = int(input(menu))
            match escolha:
                case 1:
                    play()
                case 2:
                    break
                case _:
                    print("Tem que ser uma dessas opções")
        except ValueError:
            print("Tem que ser uma dessas opções")
            
                
main()
