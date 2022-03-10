from Script import Server
from Script import Client
from Script import Blockchain
from Script import Wallet
from Script import Block_that_needs_mining
import sys
import time


Server.init()           # Проверка подключения и создание папок на серверах
Client.init()           # Создание папок на устройстве клиента



#--------------------------------------------------------------------------
# Вход или создание кошелька(если пользователь в первых 100 дается бонус)
sys.stdout.write('Enter the wallet name: ')
wallet_name = input()
sys.stdout.write('Enter the wallet password: ')
wallet_password = input()

Wallet.login(wallet_name, wallet_password)

if Wallet.login == 'NO':                    # Если кошелька не существует...
    sys.stdout.write('Create new wallet? (y/n): ')
    create_new_wallet = input()
    if create_new_wallet == 'y':
        Wallet.create()                     # Создается новый

    else:
        print('Goodbye')
else:
    create_new_wallet = 'n'
#--------------------------------------------------------------------------























#--------------------------------------------------------------------------
#             если пользователь в первых 100 дается бонус

if create_new_wallet == 'y':        # Если новый кошелек был создан...
    Blockchain.download()
    Block_that_needs_mining.download()
    Block_that_needs_mining.create_bonus1000(Wallet.c)



#--------------------------------------------------------------------------


print('Адресс вашего кошелька')
print(Wallet.c)


Wallet.balance_info(Wallet.c)








#--------------------------------------------------------------------------
#                 Отправка монет другому пльзователю
sys.stdout.write('Кому хотите отправить монет?: ')
user_recipient = input()
sys.stdout.write('Сколько монет хотите отправить?: ')
sent_coin = input()

if int(sent_coin) > int(Wallet.balance):
    print('Чурка, не пытайся меня обмануть')
    quit()

Blockchain.download()
Block_that_needs_mining.download()
Block_that_needs_mining.create(Wallet.c, user_recipient, sent_coin)


#--------------------------------------------------------------------------















