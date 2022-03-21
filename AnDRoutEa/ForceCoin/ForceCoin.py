global balance
balance = 0



import random

from Script import Server
from Script import Client
from Script import Blockchain
from Script import Wallet
from Script import Block_that_needs_mining
import sys
import time
import hashlib
import os

#cmd = 'mode 100,40'
#os.system(cmd)



hello_world = [
'       .                                                                           ',
'       |`.                                                                         ',
'       ;  `.                                                                       ',
'       ; :. \           __                                                         ',
'       ; ; \ \      .--"  \                                                        ',
'       ; ;  ; ;     :      \                                                       ',
'       ; ;  : :     ; ;     ;                                                      ',
'       \ :   ; ;    ;::     :                                                      ',
'        \ \  : ;--.-;; l     ;                                                     ',
'         \ \  ;:    :;// -.__:                                                     ',
'         /\ \ ::____:::-\                                                          ',
'        /  ).:+ """""""= \                                                         ',
'       :_,=""     /"-.    ;                                                        ',
'       ;"       .     `.  |                                                        ',
'      :      .-^=    ==.\ |                                                        ',
'      |  _.-".gp      gp:;:                                                        ',
'      ;    /  $$      $$;: ;                                                       ',
'     :    :  `--      --:  |                                                       ',
'     ;    ;\        ,      |                                                       ',
'    :    :  \      _   /   :   Семпай, войди в меня...                             ',
'    ;    |   `.   `-  /     ;                                                      ',
'   :     :    :`-.__.''     |                                                      ',
'   ;          ;     :       |                                                      ',
'  :     ...._/      ''__..  |                                                      ',
'  ;   ./                  \ ;                                                      ',
' :   /                   _ Y                                                       ',
' ;  :         .g$$p.    d$$+.                                                      ',
' ;  ;     :.g$$$$$$$$p.d$$$$$b                                                     ',
' :  :     :$$$$$$$$$$$T$$$$$$$;                                                    ',
'  \  ;    ;$$$$S$$$$$$$S$$$$$P                                                     ',
'   `.|    |$$$$S$$$$$$$S$$$$P                                                      ',
'     |    |T$$$$$SSSSS$$$$$$                                                       ',
'     :    | `T$$$$$$$$$$$$$;                                                       ',
'      ;   |   $$$$$$$$$$$$$                                                        ',
'      |   :   $$$$$$$$$$$$;                                                        ',
'      :    ; d$$$$$$$$$$$$;                                                        ',
'      |    :d$$$$$$$$$$$$$$                                                        ',
'      ;    :"^T$$$$$$$$$$$$"                                                       ',
'     :     ;   `T$$$$$$$$$$P;                                                      ',
'     ;    :      `T$$$$$$$P :                                                      ',
'     |    ;        T$$$$$P   ;                                                     ',
'     |   :          T$$P     ;                                                     ',
'     :   ;           $       :                                                     ',
'    ._;__;           :       :                                                     ',
'    ; ;  ;           |       :                                                     ',
'    :_L__:           |       ;                                                     ']
for i in range(25):
    print(hello_world[i])
print('------------------------------')
time.sleep(3)





def login():
    try:
        f = open('Database/wallet.txt', 'r')                    # Чтение файла кошелька
        wallet_name = f.readlines(1)
        wallet_password = f.readlines(2)
        wallet_key = f.readlines(3)
        wallet_name = str(wallet_name[0][:-1])
        wallet_password = str(wallet_password[0][:-1])
        wallet_key = str(wallet_key[0][:-1])
        f.close()
        #print('Файл с данными кошелька существует')
        Wallet.login(wallet_name, wallet_password, wallet_key)   # Вход через данные из файла кошелька
    except:
        print('Файл с данными кошелька НЕ существует')
        sys.stdout.write('Enter the wallet name: ')
        wallet_name = input()
        sys.stdout.write('Enter the wallet password: ')
        wallet_password = input()

        f = open('Database/wallet.txt', 'w')                      # Создание файла данных кошелька, запись данных
        f.writelines(wallet_name + '\n')
        f.writelines(wallet_password + '\n')
        f.writelines(str(random.randint(0,1000000)) + '\n')
        f.close()
        print('Ваш кошелек успешно создан')

        f = open('Database/wallet.txt', 'r')                      # Чтение данных из  кошелька
        wallet_name = f.readlines(1)
        wallet_password = f.readlines(2)
        wallet_key = f.readlines(3)
        wallet_name = str(wallet_name[0][:-1])
        wallet_password = str(wallet_password[0][:-1])
        wallet_key = str(wallet_key[0][:-1])
        f.close()
        Wallet.login(wallet_name, wallet_password, wallet_key)


        Blockchain.init()                                      # Скачнивание блокчейна
        Block_that_needs_mining.clear()                            # Очистка блоков которые нужно майнить
        Block_that_needs_mining.download()                         # Скачнивание блоков которые нужно майнить
        Block_that_needs_mining.create_bonus1000(Wallet.c)         # Если пользователь в первых 100 дается бонус

        Wallet.login(wallet_name, wallet_password, wallet_key)     # Вход через данные из файла кошелька














Server.init()           # Проверка подключения и создание папок на серверах
Client.init()           # Создание папок на устройстве клиента
login()                 # Запуска входа в кошелек











Blockchain.init()
Block_that_needs_mining.clear()
Block_that_needs_mining.download()


#clear = lambda: os.system('cls')
#clear()

print('Адресс вашего кошелька')
print(Wallet.c)
Wallet.balance_info(Wallet.c)








#pyinstaller.exe --onefile --icon=app.ico ForceCoin.py
#pyinstaller -w -F -i "app.ico" ForceCoin.py

balance = Wallet.balance


#--------------------------------------------------------------------------
#                 Отправка монет другому пльзователю
#sys.stdout.write('Кому хотите отправить монет?: ')
#user_recipient = input()
#sys.stdout.write('Сколько монет хотите отправить?: ')
#sent_coin = input()

#if (int(sent_coin) > int(Wallet.balance)):
#    print('Чурка, не пытайся меня обмануть')
#    quit()
#if  int(sent_coin) <= 0:
#    print('Чурка, не пытайся меня обмануть')
#    quit()
#
#Blockchain.init()
#Block_that_needs_mining.clear()
#Block_that_needs_mining.download()
#Block_that_needs_mining.create(Wallet.c, user_recipient, sent_coin)
#--------------------------------------------------------------------------















