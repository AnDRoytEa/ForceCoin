from Script import Server
from Script import User
from Script import Block
import sys
import time


Server.connect()
User.create_base_folder()


sys.stdout.write('Enter the wallet name: ')
wallet_name = input()
sys.stdout.write('Enter the wallet password: ')
wallet_password = input()

User.login(wallet_name, wallet_password)

if User.j == 'n':
    print('Желаете создать кошелек с введенными данными? (y/n)')
    j = input()
    if j == 'y':
        User.create_new_login()
        Block.download_blockchain()
        Block.download_block_that_needs_mining()
        Block.create_bonus1000_block_that_needs_to_mining(User.c)


    else:
        print('Всего хорошего и до новых встреч!')
        quit()



