from Script import Server
from Script import User
from Script import Block
import os
import hashlib
import sys
import ftplib



sys.stdout.write('Enter the wallet name: ')
wallet_name = input()
sys.stdout.write('Enter the wallet password: ')
wallet_password = input()

b = bytes(wallet_name + wallet_password, encoding='utf-8')
c = hashlib.sha256(b).hexdigest()


def start_mining():

    Block.download_block_that_needs_mining()

    i = 0
    block_that_needs_mining_directory = os.listdir('Block_that_needs_mining/')
    print(block_that_needs_mining_directory)
    for i in range(1000000000):
        try:
            block_that_needs_mining_directory[i] = int(block_that_needs_mining_directory[i][:-4])
        except:
            print('Переименование законченно')
            break
    minn = min(block_that_needs_mining_directory)
    data_to_hash = []
    for i in range(6):
        f = open('Block_that_needs_mining/' + str(minn) + '.txt', 'r')
        data_to_hash.append(f.readlines()[i])
        f.close()
    data_to_hash[0] = data_to_hash[0][13:]
    data_to_hash[1] = data_to_hash[1][11:]
    data_to_hash[2] = data_to_hash[2][16:]
    data_to_hash[3] = data_to_hash[3][6:]
    data_to_hash[0] = data_to_hash[0][:-1]
    data_to_hash[1] = data_to_hash[1][:-1]
    data_to_hash[2] = data_to_hash[2][:-1]
    data_to_hash[3] = data_to_hash[3][:-1]
    print(data_to_hash)









    i = 0
    block_that_needs_mining_directory = os.listdir('Blockchain/')
    print(block_that_needs_mining_directory)
    data_t = []
    for i in range(1000000000):
        try:
            block_that_needs_mining_directory[i] = int(block_that_needs_mining_directory[i][:-4])
        except:
            print('Переименование законченно')
            break
    maxx = max(block_that_needs_mining_directory)
    data_t = []
    for i in range(6):
        f = open('Blockchain/' + str(maxx) + '.txt', 'r')
        data_t.append(f.readlines()[i])
        f.close()
    previous_hash = data_t[5][11:]
    previous_hash = previous_hash[:-1]
    print(previous_hash)





    hash_b = bytes(data_to_hash[0]+data_to_hash[1]+data_to_hash[2]+data_to_hash[3], encoding='utf-8')
    hash = hashlib.sha256(hash_b).hexdigest()
    print(hash)

    f = open('Blockchain/' + str(minn) + '.txt', 'w')
    f.writelines('user_sender: ' + data_to_hash[0] + '\n')
    f.writelines('sent_coin: ' + data_to_hash[1] + '\n')
    f.writelines('user_recipient: ' + data_to_hash[2] + '\n')
    f.writelines('data: ' + data_to_hash[3] + '\n')
    f.writelines('previous_hash: ' + previous_hash + '\n')
    f.writelines('this_hash: ' + hash + '\n')
    f.writelines('miner_name: ' + c)
    f.close()

    for i in range(Server.number_servers):

        ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
        ftp.cwd('/ForceCoin/Blockchain/')
        file_name = str(minn) + '.txt'  # Имя фала
        my_file = open('Blockchain/' + file_name, 'rb')  # Директория фала
        ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
        print('Блок для майнинга', file_name, 'загружен на сервер', Server.host[i])
        ftp.close()
        my_file.close()





    block_that_needs_mining_directory = os.listdir('Block_that_needs_mining/')
    minn = min(block_that_needs_mining_directory)
    os.remove('Block_that_needs_mining/' + str(minn))
    for i in range(Server.number_servers):
        os.remove('Database/Block_that_needs_mining_check/' + Server.host[i] + '/' + str(minn))





    for i in range(Server.number_servers):
        try:
            ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
            ftp.cwd('/ForceCoin/Block_that_needs_mining/')
            file_name = str(minn) + '.txt'  # Имя фала
            ftp.delete(file_name)
        except:
            print('Чет пошло не так')





start_mining()