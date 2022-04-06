import os
import hashlib
import sys
import ftplib
import random
import time
import zipfile
import shutil
from threading import Thread



global host, user, password, number_servers
host = ["93.125.18.33"]
user = ["androut"]
password = ["Daniil_Rout132"]
number_servers = len(host)




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Server():                                                                # Проверка подключения и создание папок на серверах

    b = number_servers
    print('--------------------')
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  #Конект к серверу
            print('SERVER ' + host[i],'----', 'Connected')
            ftp.close()
        except:
            print('SERVER ' + host[i],'----', 'Not connected')                              # Добавление id серверов которые не работают
            b = b - 1
    if b == 0:
        print('Вам стоит скачать актуальную версию программы')
        quit()
    print('--------------------')


    folder_name = ['RedDrops', 'RedDrops/Database', 'RedDrops/Blockchain', 'RedDrops/Block_that_needs_mining']
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
            for z in range(len(folder_name)):
                try:
                    ftp.mkd(folder_name[z])
                    print('SERVER ' + host[i], '--', folder_name[z], '---- Папки успешно созданы')
                except:
                    pass
                    print('SERVER ' + host[i], '--', folder_name[z], '---- Папки уже существуют')
            ftp.close()
        except:
            print('SERVER ' + host[i], '----', 'Not connected')
    print('--------------------')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Wallet():
    global wallet_hash

    try:
        f = open('System/Database/wallet.txt', 'r')                    # Чтение файла кошелька
        wallet_name = f.readlines(1)
        wallet_password = f.readlines(2)
        wallet_key = f.readlines(3)
        wallet_name = str(wallet_name[0][:-1])
        wallet_password = str(wallet_password[0][:-1])
        wallet_key = str(wallet_key[0][:-1])
        f.close()
        print('Файл с данными кошелька существует')

        wallet_hash = bytes(str(wallet_name) + str(wallet_password) + str(wallet_key), encoding='utf-8')
        wallet_hash = hashlib.md5(wallet_hash).hexdigest()
        print(wallet_hash)
    except:
        print('Файл с данными кошелька НЕ существует')
        sys.stdout.write('Enter the wallet name: ')
        wallet_name = input()
        sys.stdout.write('Enter the wallet password: ')
        wallet_password = input()

        f = open('System/Database/wallet.txt', 'w')                      # Создание файла данных кошелька, запись данных
        f.writelines(wallet_name + '\n')
        f.writelines(wallet_password + '\n')
        f.writelines(str(random.randint(0,1000000)) + '\n')
        f.close()
        print('Ваш кошелек успешно создан')

        f = open('System/Database/wallet.txt', 'r')                      # Чтение данных из  кошелька
        wallet_name = str(f.readlines(1)[0][:-1])
        wallet_password = str(f.readlines(2)[0][:-1])
        wallet_key = str(f.readlines(3)[0][:-1])
        f.close()


        wallet_hash = bytes(str(wallet_name) + str(wallet_password) + str(wallet_key), encoding='utf-8')
        wallet_hash = hashlib.md5(wallet_hash).hexdigest()
        print(wallet_hash)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Blockchain():                                                                # Скачивание всех блоков из блокчейна в свои папки

    print('--------------------')
    for i in range(number_servers):                                           # Цикл от сервера №0 до последнего сервера
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])               # Конект к серверу
            ftp.cwd('RedDrops/Blockchain/')
            file_name = 'Blockchain.zip'                                     #Имя фалйа
            my_file = open('System/Database/' + file_name, 'wb')               # Директория в котрую будет сохранен файл
            ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)             # Скачивание файла
            print('SERVER', host[i], 'блоки', file_name[:-4], 'скачан')
            my_file.close()                                                # Закрытие директории в которую должен быть скачан файл
            ftp.close()                                                        # Отключение от сервера

            with zipfile.ZipFile('System/Database/' + file_name, 'r') as myzip:
                os.chdir('System/Database/Blockchain_check/')
                myzip.extractall()

            os.chdir('../')
            os.chdir('../')
            os.chdir('../')
            os.remove('System/Database/Blockchain.zip')
        except:
            pass
            #my_file.close()                                                      # Закрытие директории в которую должен быть скачан файл
            #ftp.close()
            #os.remove('System/Database/Blockchain.zip')
            #print('SERVER', host[i], 'Все блоки скачаны')


    print('--------------------')








    for i in range(1000000000):                                           # Цикл для копирования блоков из первого работающего сервера
        try:
            shutil.copyfile('System/Database/Blockchain_check/' + file_name + '/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt')
            print('Все супер')
        except:
            pass
            print('Копирование блоков в Blockchain_processing_1 Завершено')
            #print('--------------------')
            break
    print('--------------------')


    try:
        for z in range(1000000000):
            try:
                file = open('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(z) + '.txt', 'r')
                block = file.readlines()
                file.close()
                block_type = block[0][12:-1]
                user_sender = block[1][13:-1]
                sent_coin =  block[2][11:-1]
                user_recipient = block[3][16:-1]
                data = block[4][6:-1]
                previous_hash = block[5][15:-1]
                hash_key = block[6][10:-1]
                this_hash = block[7][11:-1]
                miner_name = block[8][12:]
                file.close()
            except:
                break


            b = bytes(str(block_type) + str(user_sender) + str(sent_coin) + str(user_recipient) + str(data) + str(previous_hash) + str(hash_key) +  str(miner_name), encoding='utf-8')
            hash = hashlib.sha256(b).hexdigest()

            #print(hash)
            #print(this_hash)



            if hash == this_hash:
                if this_hash[:5] == '00000':
                    print('Хэш блока номер',z , 'праввильный')
                    shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(z) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_2/' + str(z) + '.txt')
            else:
                print('Хэш блока номер', z, 'не сходится, блок не правильный')
    except:
        print('неа')
    print('Копирование блоков в Blockchain_processing_2 Завершено')
    print('--------------------')






    try:
        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_2/' + '0' + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_3/' + '0' + '.txt')
        print('Блок номер','0 Добавлен в блокчейн')
    except:
        pass

    for z in range(1000000000):                                # Проверка блоков на правильность
        try:
            file_z = open('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(z) + '.txt', 'r')             # открытие блока под номером i
            file_z1 = open('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(z+1) + '.txt', 'r')          # открытие блока под номером i + 1

            block_z = file_z.readlines()
            block_z1 = file_z1.readlines()
            file_z.close()
            file_z1.close()

            sent_coin = block_z1[2][11:-1]

            #print(block_z[5][11:])
            #print(block_z1[4][15:])
            #print(block_z[1][11:][:-1])

            if block_z[7][11:] == block_z1[5][15:]:  # Цикл для проверки предыдущих хэшей блока



                try:
                    if float(sent_coin) > 0.0:
                        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(z + 1) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_3/' + str(z + 1) + '.txt')
                        print('Блок номер', z + 1, '----- предыдущий хэш и количество передаваемых монет правильное')
                except:
                    pass
                try:
                    if sent_coin == "-":
                        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(z + 1) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_3/' + str(z + 1) + '.txt')
                        print('Блок номер', z + 1, '----- предыдущий хэш и количество передаваемых монет правильное')
                except:
                    pass
            else:
                print('Копирование блоков в Blockchain_processing_3 Завершено')
                break


        except:
            print('Копирование блоков в Blockchain_processing_3 Завершено')
            break

                # print('неа')

        file_z.close()
        file_z1.close()
    print('--------------------')





    for i in range(1000000000):                                           # Цикл для скачнивания блока от 0 до последнего
        try:
            file = open('System/Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt', 'r')
            block = file.readlines()
            file.close()
            user_sender = block[1][13:-1]

            if user_sender == Wallet.c:
                print(i)
                try:
                    file = open('System/Database/My_blocks' + str(i) + '.txt', 'r')
                    file.close()
                    shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt', 'System/Blockchain/' + str(i) + '.txt')
                except:
                    print('С вашего счета пытались спиздить монетки')
                    break
            else:
                shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt', 'System/Blockchain/' + str(i) + '.txt')

        except:
            print('Копирование блоков в Blockchain Завершено')
            break

        #print(user_sender)
        #print(Wallet.c)
    print('--------------------')











    os.chdir('System/Database/')
    with zipfile.ZipFile('Blockchain.zip', 'w') as myzip:
        os.chdir('../Blockchain/')

        for z in range(1000000000):
            try:
                myzip.write(str(z) + '.txt')
            except:
                break
    os.chdir('../')
    os.chdir('../')

    print('00000000000000000000000000000000000000000000')
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
            ftp.cwd('RedDrops/Blockchain/')
            file_name = 'Blockchain.zip'  # Имя фалйа
            my_file = open('System/Database/' + file_name, 'rb')  # Директория в котрую будет сохранен файл
            ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер  # Скачивание файла                              # Загрузка фала на сервер
            print('Блок для майнинга', file_name, 'загружен на сервер', host[i])
            my_file.close()
            ftp.close()  # Отключение от сервера
        except:
            #ftp.close()  # Отключение от сервера
            print('SERVER', host[i], 'не работает')

    print('--------------------')


    try:
        os.remove('System/Database/Blockchain.zip')
    except:
        pass





    try:
        ftp = ftplib.FTP(host[0], user[0], password[0])  # Конект к серверу
        ftp.cwd('/www/53450.vhost.cloudpark.tech/')
    except:
        pass
    for z in range(1000000000):
        try:
            file_name = str(z) + '.txt'  # Имя фалйа
            my_file = open('System/Blockchain/' + file_name, 'rb')  # Директория в котрую будет сохранен файл
            ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
            print('Блок для майнинга', file_name, 'загружен на сервер', host[i])
            my_file.close()
                
        except:
            #ftp.close()  # Отключение от сервера
            print('SERVER', host[i], 'не работает')
            ftp.close()  # Отключение от сервера
            break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Block_that_needs_mining():                                                                # Скачивание блоков для майнинга



    minn_block = os.listdir('System/Block_that_needs_mining')
    for z in range(1000000000):
        try:
            minn_block[z] = int(minn_block[z][:-4])
        except:
            break
    #print(minn_block)

    try:
        for z in range(min(minn_block),1000000000):
            try:
                os.remove(os.path.join('System/Block_that_needs_mining', str(z) + '.txt'))
            except:
                break
    except:
        pass
    #print('Отчищен block_that_needs_mining')



    global bbb
    bbb = len(os.listdir('System/Blockchain/'))

    blockchain = os.listdir('System/Blockchain/')
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

    print('--------------------')
    for i in range(number_servers):
        for z in range(block_name+1,1000000000):
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
                ftp.cwd('RedDrops/Block_that_needs_mining/')
                file_name = str(z) + '.txt'  # Имя фалйа
                my_file = open('System/Block_that_needs_mining/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)                                            # Скачивание файла блоков в папку сервера из которого они загруженны
                print('SERVER', host[i], 'Файл', file_name, 'скачан')
                my_file.close()
                ftp.close()
            except:
                try:
                    my_file.close()
                except:
                    pass
                #print('SERVER', Server.host[i], 'блок', file_name, ' из Blockc_that_needs_mining НЕ скачан')
                #print('Ненужный блок удален')
                break
    os.remove('System/Block_that_needs_mining/' + file_name)

    print('--------------------')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------












#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_block_if_nothing_to_mine():                           # Создание блока для майнинга если других блоков для майнинга не существует

    block_namee = []
    for i in range(len(os.listdir('System/Blockchain/'))):
        try:

            z = int(os.listdir('System/Blockchain/')[i][:-4])
            block_namee.append(z)
        except:
            print('Чет не так')
    try:
        maxx_block = max(block_namee)
    except:
        maxx_block = -1




    if len(os.listdir('System/Block_that_needs_mining/')) == 0:
        for z in range(maxx_block, maxx_block + 1): # Создание 2 блоков если нечего майнить
            f = open('System/Block_that_needs_mining/' + str(z + 1) + '.txt', 'w')
            f.writelines('block_type: Coin' + '\n')
            f.writelines('user_sender: ' + 'block_if_nothing_to_mine' + '\n')
            f.writelines('sent_coin: ' + '-' + '\n')
            f.writelines('user_recipient: ' + '-' + '\n')
            f.writelines('data: ' + '-' + '\n')
            f.writelines('previous_hash:\n')
            f.writelines('hash_key:\n')
            f.writelines('this_hash:\n')
            f.writelines('miner_name:')
            f.close()
            print('блок номер', str(z + 1), 'добавлен в очередь для майнинга')




        for i in range(number_servers):
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])
                ftp.cwd('RedDrops/Block_that_needs_mining/')
            except:
                pass
            for z in range(maxx_block, 1000000000):
                try:
                    file_name = str(z + 1) + '.txt'                        # Имя фала
                    my_file = open('System/Block_that_needs_mining/' + file_name, 'rb')   # Директория фала
                    ftp.storbinary('STOR ' + file_name, my_file)                   # Загрузка фала на сервер
                    print('Блок для майнинга', file_name, 'загружен на сервер', host[i])
                    my_file.close()
                except:
                    print('SERVER', host[i], 'не работает')
                    #ftp.close()
                    break
            #ftp.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




def Start_mining():
    global block_name
    Blockchain()
    Block_that_needs_mining()


    block_that_needs_mining = os.listdir('System/Block_that_needs_mining/')
    blockchain = os.listdir('System/Blockchain/')
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
            f = open('System/Block_that_needs_mining/' + str(block_name+1) + '.txt', 'r')
        except:
            create_block_if_nothing_to_mine()                                # Если блоки для майнинга закончились
            Block_that_needs_mining()
            time.sleep(1)



    try:
        file = open('System/Block_that_needs_mining/' + str(block_name + 1) + '.txt', 'r')
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
        miner_name = wallet_hash
        file.close()
        try:
            file = open('System/Blockchain/' + str(block_name) + '.txt', 'r')
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



    f = open('System/Blockchain/' + str(block_name+1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(wallet_hash))
    f.close()


    f = open('System/Database/Blockchain_check/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(wallet_hash))
    f.close()

    f = open('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(wallet_hash))
    f.close()

    f = open('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(wallet_hash))
    f.close()

    f = open('System/Database/Blockchain_processing/Blockchain_processing_3/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: ' + str(block_type) + '\n')
    f.writelines('user_sender: ' + str(user_sender) + '\n')
    f.writelines('sent_coin: ' + str(sent_coin) + '\n')
    f.writelines('user_recipient: ' + str(user_recipient) + '\n')
    f.writelines('data: ' + str(data) + '\n')
    f.writelines('previous_hash: ' + str(previous_hash) + '\n')
    f.writelines('hash_key: ' + str(hash_key) + '\n')
    f.writelines('this_hash: ' + str(this_hash) + '\n')
    f.writelines('miner_name: ' + str(wallet_hash))
    f.close()

    #print(block_type)
    #print(user_sender)
    #print(sent_coin)
    #print(user_recipient)
    #print(data)
    #print(previous_hash)
    #print(hash_key)
    #print(this_hash)
    #print(miner_name)







    os.remove('System/Block_that_needs_mining/' + str(block_name+1) + '.txt')





    i = 0
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])
            ftp.cwd('RedDrops/Block_that_needs_mining/')
            file_name = str(block_name+1) + '.txt' # Имя фала
            ftp.delete(file_name)
            ftp.close()
        except:
            print('Чет пошло не так')








Server()
Wallet()
for i in range(100):




    Start_mining()













