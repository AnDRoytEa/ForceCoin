import os
from System.Source import ForceNET as FNET
import time


import colorama
from colorama import Fore, Back, Style


a = FNET.server_init()
if a == 'done':
    print('ForceNET ' + Style.BRIGHT + '- server_init() ----', Fore.GREEN + a + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + ' - server_init() ----', Fore.RED + a + Style.RESET_ALL)

    print('You need update the ForceNET system')
    time.sleep(10000)



z = FNET.client_folder_init()
if z == 'done':
    print('ForceNET ' + Style.BRIGHT + '- folder_init(client) ----', Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + '- folder_init(client) ----', Fore.RED + z + Style.RESET_ALL)




z = FNET.create_wallet()
if z == 'done':
    print('ForceNET ' + Style.BRIGHT + '- wallet(create) ----', Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + '- wallet(create) ----', Fore.RED + z + Style.RESET_ALL)




z = FNET.server_folder_init()
if z == 'done':
    print('ForceNET ' + Style.BRIGHT + '- folder_init(server) ----', Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + '- folder_init(server) ----', Fore.RED + z + Style.RESET_ALL)




z = FNET.wallet_init()
if z == 'done':
    print('ForceNET ' + Style.BRIGHT + '- wallet(init) ----', Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + '- wallet(init) ----', Fore.RED + z + Style.RESET_ALL)




z = FNET.download('blockchain')
if z == 'done':
    print('ForceNET ' + Style.BRIGHT + '- download(blockchain) ----', Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + '- download(blockchain) ----', Fore.RED + z + Style.RESET_ALL)


FNET.processing('blockchain_processing_0')
FNET.processing('blockchain_processing_1')
FNET.processing('blockchain_processing_2')
FNET.processing('blockchain_processing_3')



z = FNET.download('block_that_needs_mining')
if z == 'done':
    print('ForceNET ' + Style.BRIGHT + '- download(block_that_needs_mining) ----', Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + '- download(block_that_needs_mining) ----', Fore.RED + z + Style.RESET_ALL)


z = FNET.upload('blockchain')
if z == 'done':
    print('ForceNET ' + Style.BRIGHT + '- upload(blockchain) ----', Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + '- upload(blockchain) ----', Fore.RED + z + Style.RESET_ALL)



z = FNET.upload('block_that_needs_mining')
if z == 'done':
    print('ForceNET ' + Style.BRIGHT + '- upload(block_that_needs_mining) ----',  Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET ' + Style.BRIGHT + '- upload(block_that_needs_mining) ----', Fore.RED + z + Style.RESET_ALL)




print('')
while True:
    a = input('ForceNET>> ')

    if a == '/help':
        print('    available commands:')
        print('    /stats - Returns information about your account')
        print('    /send_coin - Sends coins to the recipients name')
        print('')

    if a == '/stats':
        print('    Your wallet:', FNET.wallet_address)
        a = FNET.coin_balance_info()
        print('    Your balance: ', a)
        print('')
        cprint('Вывод с помощью cprint', 'green', 'on_blue')

    if a == '/send_coin':
        object = input('    object>> ')
        recipient = input('    recipientt>> ')
        a = send_coin(object, recipient)
        z = upload('blockchain')
        print('    ForceNET - upload(blockchain) ----',z);
        z = upload('block_that_needs_mining')
        print('    ForceNET - upload(block_that_needs_mining) ----',z);






























