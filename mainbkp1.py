import random
def tela_de_resumo():
    numero_escolhido_pelo_tubarao_baitola = random.randint(0, 500)
    if numero_escolhido_pelo_tubarao_baitola == numero:
        print("""\ ____                 _       __           
|  _ \ __ _ _ __ __ _| |__   /_/ _ __  ___ 
| |_) / _` | '__/ _` | '_ \ / _ \ '_ \/ __|
|  __/ (_| | | | (_| | |_) |  __/ | | \__ \
|_|   \__,_|_|  \__,_|_.__/ \___|_| |_|___/ """)
        print("O Tubarão baitola escolheu o mesmo número que você!")
    else:
         print("""\ ____              _            
|  _ \ ___ _ __ __| | ___ _   _ 
| |_) / _ \ '__/ _` |/ _ \ | | |
|  __/  __/ | | (_| |  __/ |_| |
|_|   \___|_|  \__,_|\___|\__,_| """)
         print("Não foi dessa vez... o Tubarão baitola escolheu", numero_escolhido_pelo_tubarao_baitola)

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
        global numero
        numero = input("Qual é seu número escolhido de 0 a 500? ")
        print("Você escolheu:", numero)
        tela_de_resumo()




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
    escolha = int(input(menu))
    match escolha:
        case 1:
            play()
        case 2:
            exit
               
main()