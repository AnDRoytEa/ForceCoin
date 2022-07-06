import os
from System.Source import ForceNET as FNET
import time
import colorama
from colorama import Fore, Back, Style




colorama.init()
a = FNET.server_init()
if a == 'done':
    print('ForceNET - server_init() ----', Style.BRIGHT + Fore.GREEN + a + Style.RESET_ALL)
else:
    print('ForceNET  - server_init() ----', Style.BRIGHT + Fore.RED + a + Style.RESET_ALL)

    print('You need update the ForceNET system')
    time.sleep(10000)



z = FNET.client_folder_init()
if z == 'done':
    print('ForceNET - folder_init(client) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET - folder_init(client) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)




z = FNET.create_wallet()
if z == 'done':
    print('ForceNET - wallet(create) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET - wallet(create) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)




z = FNET.server_folder_init()
if z == 'done':
    print('ForceNET - folder_init(server) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET - folder_init(server) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)




z = FNET.wallet_init()
if z == 'done':
    print('ForceNET - wallet(init) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET - wallet(init) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)




z = FNET.download('blockchain')
if z == 'done':
    print('ForceNET - download(blockchain) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET - download(blockchain) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)





a = FNET.processing('blockchain_processing_0')
print('ForceNET - blockchain_processing_0 ----', Style.BRIGHT + Fore.GREEN + str(a) + Style.RESET_ALL)

b = FNET.processing('blockchain_processing_1')
if a != b:
    print('ForceNET - blockchain_processing_1 ----', Style.BRIGHT + Fore.RED + str(a) + Style.RESET_ALL)
else:
    print('ForceNET - blockchain_processing_1 ----', Style.BRIGHT + Fore.GREEN + str(a) + Style.RESET_ALL)

c = FNET.processing('blockchain_processing_2')
if b != c:
    print('ForceNET - blockchain_processing_2 ----', Style.BRIGHT + Fore.RED + str(a) + Style.RESET_ALL)
else:
    print('ForceNET - blockchain_processing_2 ----', Style.BRIGHT + Fore.GREEN + str(a) + Style.RESET_ALL)

d = FNET.processing('blockchain_processing_3')
if c != d:
    print('ForceNET - blockchain_processing_3 ----', Style.BRIGHT + Fore.RED + str(a) + Style.RESET_ALL)
else:
    print('ForceNET - blockchain_processing_3 ----', Style.BRIGHT + Fore.GREEN + str(a) + Style.RESET_ALL)






z = FNET.download('block_that_needs_mining')
if z == 'done':
    print('ForceNET - download(block_that_needs_mining) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET - download(block_that_needs_mining) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)


z = FNET.upload('blockchain')
if z == 'done':
    print('ForceNET - upload(blockchain) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET - upload(blockchain) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)



z = FNET.upload('block_that_needs_mining')
if z == 'done':
    print('ForceNET - upload(block_that_needs_mining) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
else:
    print('ForceNET - upload(block_that_needs_mining) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)



























print('')
while True:
    a = input('ForceNET>> ')

    if a == '/help':
        print('    available commands:')
        print('    /stats - Returns information about your account')
        print('    /send_coin - Sends coins to the recipients wallet address')
        print('    /send_coin_by_id - Sends coins to the recipients id')
        print('    /create_new_NFT - Creating an nft on the ForceNET network')
        print('    /send_NFT - Sends NFT to the recipients wallet address')
        print('    /last_transactions - show 8 last transactions with your wallet')
        print('')




    if a == '/stats':
        print('    Your wallet:', FNET.wallet_address)
        print('    Your wallet id:', FNET.account_id(FNET.wallet_address))
        a = FNET.coin_balance_info()
        print('    Your balance:', a)
        a = FNET.NFT_balance_info()
        print('    Your NFT:', a)
        print('')




    if a == '/send_coin':
        object = input('    object>> ')
        recipient = input('    recipientt>> ')
        object = str(object)
        recipient = str(recipient)
        a = FNET.send_coin(object, recipient)
        z = FNET.upload('blockchain')
        print('    ForceNET - upload(blockchain) ----',z)
        z = FNET.upload('block_that_needs_mining')
        print('    ForceNET - upload(block_that_needs_mining) ----',z)
        print('')


    if a == '/send_coin_by_id':
        object = input('    object>> ')
        recipient = input('    recipient_id>> ')
        object = str(object)
        recipient = FNET.address_by_id(int(recipient))
        a = FNET.send_coin(object, recipient)
        z = FNET.upload('blockchain')
        print('    ForceNET - upload(blockchain) ----',z)
        z = FNET.upload('block_that_needs_mining')
        print('    ForceNET - upload(block_that_needs_mining) ----',z)
        print('')


    if a == '/create_new_NFT':
        object = input('    object>> ')

        FNET.create_new_NFT(object)
        z = FNET.upload('blockchain')
        print('    ForceNET - upload(blockchain) ----',z)
        z = FNET.upload('block_that_needs_mining')
        print('    ForceNET - upload(block_that_needs_mining) ----',z)
        print('')



    if a == '/send_NFT':
        object = input('    object>> ')
        recipient = input('    recipientt>> ')
        object = str(object)
        recipient = str(recipient)
        a = FNET.send_NFT(object, recipient)
        z = FNET.upload('blockchain')
        print('    ForceNET - upload(blockchain) ----',z)
        z = FNET.upload('block_that_needs_mining')
        print('    ForceNET - upload(block_that_needs_mining) ----',z)
        print('')


    if a == '/last_transactions':
        a = FNET.last_transactions()
        if len(FNET.last_transactions()) >= 16:
            for i in range(16):
                print('    ', a[i])
                if i%2:
                    print(' ')
        else:
            for i in range(len(FNET.last_transactions())):
                print('    ', a[i])
                if i%2:
                    print(' ')























