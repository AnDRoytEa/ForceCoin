from Script import Server
from Script import Client
from Script import Blockchain
from Script import Block_that_needs_mining
from Script import Wallet
import os
import hashlib
import sys
import ftplib
import random
import time

Server.init()           # Проверка подключения и создание папок на серверах
Client.init()           # Создание папок на устройстве клиента

def login():
    global c
    try:
        f = open('Database/wallet.txt', 'r')                    # Чтение файла кошелька
        wallet_name = f.readlines(1)
        wallet_password = f.readlines(2)
        wallet_key = f.readlines(3)
        wallet_name = str(wallet_name[0][:-1])
        wallet_password = str(wallet_password[0][:-1])
        wallet_key = str(wallet_key[0][:-1])
        f.close()
        b = bytes(str(wallet_name) + str(wallet_password) + str(wallet_key), encoding='utf-8')
        c = hashlib.md5(b).hexdigest()
    except:
        #print('Файл с данными кошелька НЕ существует')
        sys.stdout.write('Enter the wallet name: ')
        wallet_name = input()
        sys.stdout.write('Enter the wallet password: ')
        wallet_password = input()

        f = open('Database/wallet.txt', 'w')                      # Создание файла данных кошелька
        f.writelines(wallet_name + '\n')
        f.writelines(wallet_password + '\n')
        f.writelines(str(random.randint(0,1000000)) + '\n')
        f.close()
        print('Ваш кошелек успешно создан')

        f = open('Database/wallet.txt', 'r')
        wallet_name = f.readlines(1)
        wallet_password = f.readlines(2)
        wallet_key = f.readlines(3)
        wallet_name = str(wallet_name[0][:-1])
        wallet_password = str(wallet_password[0][:-1])
        wallet_key = str(wallet_key[0][:-1])
        f.close()
        Wallet.login(wallet_name, wallet_password, wallet_key)

        Blockchain.download()                                      # Скачнивание блокчейна
        Block_that_needs_mining.clear()                            # Очистка блоков которые нужно майнить
        Block_that_needs_mining.download()                         # Скачнивание блоков которые нужно майнить
        Block_that_needs_mining.create_bonus1000(Wallet.c)         # Если пользователь в первых 100 дается бонус
        b = bytes(str(wallet_name) + str(wallet_password) + str(wallet_key), encoding='utf-8')
        c = hashlib.sha256(b).hexdigest()


login()




def start_mining():

    Blockchain.init()
    Block_that_needs_mining.clear()
    Block_that_needs_mining.download()

    block_that_needs_mining = os.listdir('Block_that_needs_mining/')
    blockchain = os.listdir('Blockchain/')
    for z in range(1000000000):
        try:
            blockchain[z] = int(blockchain[z][:-4])
        except:
            try:
                blockchain.append(blockchain[z-1])
            except:
                blockchain.append(-1)
                blockchain.append(-2)
            try:
                block_name = max(blockchain)
            except:
                block_name = -1
            break



    data_to_hash = []
    for i in range(6):
        try:
            f = open('Block_that_needs_mining/' + str(block_name+1) + '.txt', 'r')
        except:
            Block_that_needs_mining.create_4_block_if_nothing_to_mine()                                # Если блоки для майнинга закончились
            Block_that_needs_mining.download()
            time.sleep(1)



    try:
        file = open('Block_that_needs_mining/' + str(block_name + 1) + '.txt', 'r')
        block = file.readlines()
        file.close()
        block_type = block[0][12:-1]
        user_sender = block[1][13:-1]
        sent_coin = block[2][11:-1]
        user_recipient = block[3][16:-1]
        data = block[4][6:-1]
        previous_hash = block[5][15:-1]
        hash_key = block[6][10:-1]
        this_hash = block[7][11:-1]
        miner_name = c
        file.close()
        try:
            file = open('Blockchain/' + str(block_name) + '.txt', 'r')
            ph = file.readlines()
            file.close()
            previous_hash = ph[7][11:-1]
        except:
            previous_hash = '0'
            print('Предыдущего блока нет, этот блок будет первым')
    except:
        print('неа')
        quit()



    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #                                                          Подбор хэша с нулями в начале
    b = bytes(str(block_type) + str(user_sender) + str(sent_coin) + str(user_recipient) + str(data) + str(previous_hash) + str(miner_name), encoding='utf-8')
    this_hash = hashlib.sha256(b).hexdigest()
    while this_hash[:5] != '00000':
        hash_key = random.randint(0, 1000000000)
        b = bytes(str(block_type) + str(user_sender) + str(sent_coin) + str(user_recipient) + str(data) + str(previous_hash) + str(hash_key) +  str(miner_name), encoding='utf-8')
        this_hash = hashlib.sha256(b).hexdigest()
        print(this_hash)
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------



    f = open('Blockchain/' + str(block_name+1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(c))
    f.close()

    for i in range(Server.number_servers):
        f = open('Database/Blockchain_check/' + Server.host[i] + '/' + str(block_name + 1) + '.txt', 'w')
        f.writelines('block_type: ' + str(block_type) + '\n')
        f.writelines('user_sender: ' + str(user_sender) + '\n')
        f.writelines('sent_coin: ' + str(sent_coin) + '\n')
        f.writelines('user_recipient: ' + str(user_recipient) + '\n')
        f.writelines('data: ' + str(data) + '\n')
        f.writelines('previous_hash: ' + str(previous_hash) + '\n')
        f.writelines('hash_key: ' + str(hash_key) + '\n')
        f.writelines('this_hash: ' + str(this_hash) + '\n')
        f.writelines('miner_name: ' + str(c))
        f.close()

    f = open('Database/Blockchain_processing_1/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(c))
    f.close()

    f = open('Database/Blockchain_processing_2/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(c))
    f.close()

    f = open('Database/Blockchain_processing_3/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(c))
    f.close()

    print(block_type)
    print(user_sender)
    print(sent_coin)
    print(user_recipient)
    print(data)
    print(previous_hash)
    print(hash_key)
    print(this_hash)
    print(miner_name)





#    for i in range(Server.number_servers):
#        if i in Server.disconnected_servers:
#            print('SERVER ' + Server.host[i], '----', 'Not connected')
#            continue
#        else:
#            ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
#            ftp.cwd('/ForceCoin/Blockchain/')
#            file_name = str(block_name+1) + '.txt'  # Имя фала
#            my_file = open('Blockchain/' + file_name, 'rb')  # Директория фала
#            ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
#            print('Блок для майнинга', file_name, 'загружен на сервер', Server.host[i])
#            ftp.close()
#            my_file.close()

    os.remove('Block_that_needs_mining/' + str(block_name+1) + '.txt')
    for i in range(Server.number_servers):
        os.remove('Database/Block_that_needs_mining_check/' + Server.host[i] + '/' + str(block_name+1) + '.txt')




    i = 0
    for i in range(Server.number_servers):
        if i in Server.disconnected_servers:
            print('SERVER ' + Server.host[i], '----', 'Not connected')
            continue
        else:
            try:
                ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
                ftp.cwd('/ForceCoin/Block_that_needs_mining/')
                file_name = str(block_name+1) + '.txt' # Имя фала
                ftp.delete(file_name)
            except:
                print('Чет пошло не так')




for i in range(100):
    start_mining()