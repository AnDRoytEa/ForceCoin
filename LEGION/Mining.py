import os
from System.Source import ForceNET as FNET
import time





a = FNET.server_init()
print('ForceNET - server_init() ----',a)

if a == 'failed':
    print('You need update the ForceNET system')
    time.sleep(1000)

z = FNET.client_folder_init()
print('ForceNET - folder_init(client) ----',z)

z = FNET.create_wallet()
print('ForceNET - wallet(create) ----',z)

z = FNET.server_folder_init()
print('ForceNET - folder_init(server) ----',z)

z = FNET.wallet_init()
print('ForceNET - wallet(init) ----',z)





for i in range(10):
    z = FNET.download('blockchain')
    print('ForceNET - download(blockchain) ----',z)

    FNET.processing('blockchain_processing_0')
    FNET.processing('blockchain_processing_1')
    FNET.processing('blockchain_processing_2')
    FNET.processing('blockchain_processing_3')

    z = FNET.download('block_that_needs_mining')
    print('ForceNET - download(block_that_needs_mining) ----',z)

    print(' ')
    a = FNET.coin_balance_info()
    print('Your balance - ', a)

    FNET.mining()

    z = FNET.upload('blockchain')
    print('ForceNET - upload(blockchain) ----',z)

    z = FNET.upload('block_that_needs_mining')
    print('ForceNET - upload(block_that_needs_mining) ----',z)







































