import ftplib
import hashlib
import random

import sys
import os
import shutil
import zipfile


global host, user, password, number_servers
host = ["93.125.18.33",         "91.106.207.15"]
user = ["androytea21",          "androylu_12"]
password = ["Daniil_Rout132",   "Daniil_Rout132"]
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


    folder_name = ['RedDrops', 'RedDrops/Database', 'RedDrops/Blockchain', 'RedDrops/Block_that_needs_mining', "RedDrops/Arts"]
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
            for z in range(len(folder_name)):
                try:
                    ftp.mkd(folder_name[z])
                    #print('SERVER ' + host[i], '--', folder_name[z], '---- Папки успешно созданы')
                except:
                    pass
                    #print('SERVER ' + host[i], '--', folder_name[z], '---- Папки уже существуют')
            ftp.close()
        except:
            print('SERVER ' + host[i], '----', 'Not connected')
    print('--------------------')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Wallet():
    global wallet_hash

    try:
        f = open('../Database/wallet.txt', 'r')                    # Чтение файла кошелька
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

        f = open('../Database/wallet.txt', 'w')                      # Создание файла данных кошелька, запись данных
        f.writelines(wallet_name + '\n')
        f.writelines(wallet_password + '\n')
        f.writelines(str(random.randint(0,1000000)) + '\n')
        f.close()
        print('Ваш кошелек успешно создан')

        f = open('../Database/wallet.txt', 'r')                      # Чтение данных из  кошелька
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
            my_file = open('../Database/' + file_name, 'wb')               # Директория в котрую будет сохранен файл
            ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)             # Скачивание файла
            #print('SERVER', host[i], 'блоки', file_name[:-4], 'скачан')
            my_file.close()                                                # Закрытие директории в которую должен быть скачан файл
            ftp.close()                                                        # Отключение от сервера

            with zipfile.ZipFile('../Database/' + file_name, 'r') as myzip:
                os.chdir('../Database/Blockchain_check/')
                myzip.extractall()

            os.chdir('../')
            os.chdir('../')
            os.chdir('Script/')
            os.remove('../Database/Blockchain.zip')
        except:
            my_file.close()                                                      # Закрытие директории в которую должен быть скачан файл
            ftp.close()
            os.remove('../Database/Blockchain.zip')
            #print('SERVER', host[i], 'Все блоки скачаны')


    print('--------------------')








    for i in range(1000000000):                                           # Цикл для копирования блоков из первого работающего сервера
        try:
            shutil.copyfile('../Database/Blockchain_check/' + str(i) + '.txt', '../Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt')
            #print('Все супер')
        except:
            pass
            #print('Копирование блоков в Blockchain_processing_1 Завершено')
            #print('--------------------')
            break
    print('--------------------')


    try:
        for z in range(1000000000):
            try:
                file = open('../Database/Blockchain_processing/Blockchain_processing_1/' + str(z) + '.txt', 'r')
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
                    #print('Хэш блока номер',z , 'праввильный')
                    shutil.copyfile('../Database/Blockchain_processing/Blockchain_processing_1/' + str(z) + '.txt', '../Database/Blockchain_processing/Blockchain_processing_2/' + str(z) + '.txt')
            else:
                pass
                #print('Хэш блока номер', z, 'не сходится, блок не правильный')
    except:
        pass
        #print('неа')
    #print('Копирование блоков в Blockchain_processing_2 Завершено')
    #print('--------------------')






    try:
        shutil.copyfile('../Database/Blockchain_processing/Blockchain_processing_2/' + '0' + '.txt', '../Database/Blockchain_processing/Blockchain_processing_3/' + '0' + '.txt')
        #print('Блок номер','0 Добавлен в блокчейн')
    except:
        pass

    for z in range(1000000000):                                # Проверка блоков на правильность
        try:
            file_z = open('../Database/Blockchain_processing/Blockchain_processing_2/' + str(z) + '.txt', 'r')             # открытие блока под номером i
            file_z1 = open('../Database/Blockchain_processing/Blockchain_processing_2/' + str(z+1) + '.txt', 'r')          # открытие блока под номером i + 1

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
                        shutil.copyfile('../Database/Blockchain_processing/Blockchain_processing_2/' + str(z + 1) + '.txt', '../Database/Blockchain_processing/Blockchain_processing_3/' + str(z + 1) + '.txt')
                        #print('Блок номер', z + 1, '----- предыдущий хэш и количество передаваемых монет правильное')
                except:
                    pass
                try:
                    if sent_coin == "-":
                        shutil.copyfile('../Database/Blockchain_processing/Blockchain_processing_2/' + str(z + 1) + '.txt', '../Database/Blockchain_processing/Blockchain_processing_3/' + str(z + 1) + '.txt')
                        #print('Блок номер', z + 1, '----- предыдущий хэш и количество передаваемых монет правильное')
                except:
                    pass
            else:
                #print('Копирование блоков в Blockchain_processing_3 Завершено')
                break


        except:
            #print('Копирование блоков в Blockchain_processing_3 Завершено')
            break

                # print('неа')

        file_z.close()
        file_z1.close()
    print('--------------------')





    for i in range(1000000000):                                           # Цикл для скачнивания блока от 0 до последнего
        #print(i)
        try:
            file = open('../Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt', 'r')
            block = file.readlines()
            file.close()
            user_sender = block[1][13:-1]
            #print(i)
            if user_sender == wallet_hash:

                try:
                    file = open('../Database/My_blocks/' + str(i) + '.txt', 'r')
                    file.close()
                    shutil.copyfile('../Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt', '../Blockchain/' + str(i) + '.txt')
                    #print('Все ок')
                except:
                    print('С вашего счета пытались спиздить монетки')
                    break
            else:
                shutil.copyfile('../Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt', '../Blockchain/' + str(i) + '.txt')

        except:
            #print('Копирование блоков в Blockchain Завершено')
            break

        #print(user_sender)
        #print(Wallet.c)
    #print('--------------------')



    os.chdir('../Database/')
    with zipfile.ZipFile('Blockchain.zip', 'w') as myzip:
        os.chdir('../Blockchain/')

        for z in range(1000000000):
            try:
                myzip.write(str(z) + '.txt')
            except:
                break
    os.chdir('../Script')



    #print('00000000000000000000000000000000000000000000')
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
            ftp.cwd('RedDrops/Blockchain/')
            file_name = 'Blockchain.zip'  # Имя фалйа
            my_file = open('../Database/' + file_name, 'rb')  # Директория в котрую будет сохранен файл
            ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер  # Скачивание файла                              # Загрузка фала на сервер
            #print('Блок для майнинга', file_name, 'загружен на сервер', host[i])
            my_file.close()
            ftp.close()  # Отключение от сервера
        except:
            ftp.close()  # Отключение от сервера
            #print('SERVER', host[i], 'не работает')


   #print('--------------------')

    try:
        os.remove('../Database/Blockchain.zip')
    except:
        pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Art_info(wallet_login):                                                              # Проверка баланса кошелька
    # Выбор названий блоков которые нужно проверить

    global balance, arts_name
    balance = 0

    arts_name = []


    for z in range(1000000000):                          # Проверка сколько монет мне переводили
        try:
            file = open('../Blockchain/' + str(z) + '.txt', 'r')
            block = file.readlines()
            block_type = block[0][12:-1]
            user_recipient = block[3][16:-1]
            data = block[4][6:-1]
            user_sender = block[1][13:-1]
            if block_type == 'Art':
                if user_recipient == wallet_login:       # Если логин моего кошелька был в user_recipient то баланс = балас + количество отправляемых мне монет
                    arts_name.append(data)

                    for z in range(1000000000):  # Цикл для скачнивания блока от 0 до последнего
                        try:
                            ftp = ftplib.FTP(host[z], user[z], password[z])  # Конект к серверу
                            ftp.cwd('RedDrops/Arts')
                            file_name = data  # Имя фалйа
                            my_file = open('../Database/My_arts/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                            ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)  # Скачивание файла
                            print('SERVER', host[z], 'арт', file_name, 'скачан')
                            my_file.close()
                        except:
                            break

                    #print(file)
                    #print('Вроде пару монет на кошельке есть')
            file.close()
        except:
            pass
            #print('С проверкой монет на кошельке чет не так')
            break




    for z in range(1000000000):                          # Проверка сколько монет я тратил
        try:
            file = open('../Blockchain/' + str(z) + '.txt', 'r')
            block = file.readlines()
            block_type = block[0][12:-1]
            user_recipient = block[3][16:-1]
            data = block[4][6:-1]
            user_sender = block[1][13:-1]
            if block_type == 'Art':
                if user_sender == wallet_login:       # Если логин моего кошелька был в user_sender то баланс = балас - sent_coin
                    arts_name.remove(data)
                    os.remove('../Database/My_arts/' + data)
                    #print('Вроде пару монет на кошельке есть')
            file.close()
        except:
            pass
            #print('С проверкой монет на кошельке чет не так')
            break




    print('Ваши арты', arts_name)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Block_that_needs_mining():                                                                # Скачивание блоков для майнинга



    minn_block = os.listdir('../Block_that_needs_mining')
    for z in range(1000000000):
        try:
            minn_block[z] = int(minn_block[z][:-4])
        except:
            break
    #print(minn_block)

    try:
        for z in range(min(minn_block),1000000000):
            try:
                os.remove(os.path.join('../Block_that_needs_mining', str(z) + '.txt'))
            except:
                break
    except:
        pass
    #print('Отчищен block_that_needs_mining')


    global bbb
    i = 0
    bbb = len(os.listdir('../Blockchain/'))

    blockchain = os.listdir('../Blockchain/')
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
                my_file = open('../Block_that_needs_mining/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)                                            # Скачивание файла блоков в папку сервера из которого они загруженны
                #print('SERVER', host[i], 'Файл', file_name, 'скачан')
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
    os.remove('../Block_that_needs_mining/' + file_name)

    print('--------------------')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


















#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Create_art(user_sender, user_recipient, sent_coin):                           # Создание блока для майнинга в котором осуществляется перевод монет
    lbi_blockchain = []                     #last_block_in_blockchain
    lbi_block_that_needs_mining = []        #last_block_in_block_that_needs_mining
    mbi_blockchain = -1                     #max_block_in_blockchain
    mbi_block_that_needs_mining = -1        #max_block_in_block_that_needs_mining

    for i in range(number_servers):

        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])
            ftp.cwd('RedDrops/Arts/')
            file_name = sent_coin  # Имя фала
            my_file = open(file_name, 'rb')  # Директория фала
            ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
            print('Арт', file_name, 'загружен на сервер', host[i])
            ftp.close()
            my_file.close()
        except:
            print('SERVER', host[i], 'не работает')
            break



    i = 0
    blockchain_check = os.listdir('../Blockchain/')
    for i in range(len(blockchain_check)):
        try:

            z = int(blockchain_check[i][:-4])
            lbi_blockchain.append(z)
        except:
            print('Чет не так')

    i = 0
    block_that_needs_mining_check = os.listdir('../Block_that_needs_mining/')
    for i in range(len(block_that_needs_mining_check)):
        try:

            z = int(block_that_needs_mining_check[i][:-4])
            lbi_block_that_needs_mining.append(z)
        except:
            print('Чет не так')

    try:
        mbi_blockchain = max(lbi_blockchain)
    except:
        mbi_blockchain = -1
    try:
        mbi_block_that_needs_mining = max(lbi_block_that_needs_mining)
    except:
        mbi_block_that_needs_mining = -1

    if mbi_blockchain > mbi_block_that_needs_mining:
        block_name = mbi_blockchain
    else:
        block_name = mbi_block_that_needs_mining




    f = open('../Block_that_needs_mining/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: Art\n')
    f.writelines('user_sender: ' + '-' + '\n')
    f.writelines('sent_coin: -' + '\n')
    f.writelines('user_recipient: ' + user_recipient +'\n')
    f.writelines('data: ' + str(sent_coin) + '\n')
    f.writelines('previous_hash:\n')
    f.writelines('hash_key:\n')
    f.writelines('this_hash:\n')
    f.writelines('miner_name:')
    f.close()
    print('блок номер', str(block_name + 1), 'добавлен в очередь для майнинга')


    f = open('../Database/My_blocks/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: Art\n')
    f.writelines('user_sender: ' + '-' + '\n')
    f.writelines('sent_coin: -' + '\n')
    f.writelines('user_recipient: ' + user_recipient +'\n')
    f.writelines('data: ' + str(sent_coin) + '\n')
    f.writelines('previous_hash:\n')
    f.writelines('hash_key:\n')
    f.writelines('this_hash:\n')
    f.writelines('miner_name:')
    f.close()
    print('блок номер', str(block_name + 1), 'добавлен в очередь для майнинга')


    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])
            ftp.cwd('RedDrops/Block_that_needs_mining/')
            file_name = str(block_name + 1) + '.txt'                                       # Имя фала
            my_file = open('../Block_that_needs_mining/' + file_name, 'rb')                   # Директория фала
            ftp.storbinary('STOR ' + file_name, my_file)                                   # Загрузка фала на сервер
            print('Блок для майнинга', file_name, 'загружен на сервер', host[i])
            ftp.close()
            my_file.close()
        except:
            print('SERVER', host[i], 'не работает')
            break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------










#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Give_art(user_sender, user_recipient, sent_coin):                           # Создание блока для майнинга в котором осуществляется перевод монет
    lbi_blockchain = []                     #last_block_in_blockchain
    lbi_block_that_needs_mining = []        #last_block_in_block_that_needs_mining
    mbi_blockchain = -1                     #max_block_in_blockchain
    mbi_block_that_needs_mining = -1        #max_block_in_block_that_needs_mining

    if user_sender == user_recipient:
        quit()

    for i in range(number_servers):

        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])
            ftp.cwd('RedDrops/Arts/')
            file_name = sent_coin  # Имя фала
            my_file = open(file_name, 'rb')  # Директория фала
            ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
            print('Арт', file_name, 'загружен на сервер', host[i])
            ftp.close()
            my_file.close()
        except:
            print('SERVER', host[i], 'не работает')
            break



    i = 0
    blockchain_check = os.listdir('../Blockchain/')
    for i in range(len(blockchain_check)):
        try:

            z = int(blockchain_check[i][:-4])
            lbi_blockchain.append(z)
        except:
            print('Чет не так')

    i = 0
    block_that_needs_mining_check = os.listdir('../Block_that_needs_mining/')
    for i in range(len(block_that_needs_mining_check)):
        try:

            z = int(block_that_needs_mining_check[i][:-4])
            lbi_block_that_needs_mining.append(z)
        except:
            print('Чет не так')

    try:
        mbi_blockchain = max(lbi_blockchain)
    except:
        mbi_blockchain = -1
    try:
        mbi_block_that_needs_mining = max(lbi_block_that_needs_mining)
    except:
        mbi_block_that_needs_mining = -1

    if mbi_blockchain > mbi_block_that_needs_mining:
        block_name = mbi_blockchain
    else:
        block_name = mbi_block_that_needs_mining





    f = open('../Block_that_needs_mining/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: Art\n')
    f.writelines('user_sender: ' + user_sender + '\n')
    f.writelines('sent_coin: -' + '\n')
    f.writelines('user_recipient: ' + user_recipient +'\n')
    f.writelines('data: ' + str(sent_coin) + '\n')
    f.writelines('previous_hash:\n')
    f.writelines('hash_key:\n')
    f.writelines('this_hash:\n')
    f.writelines('miner_name:')
    f.close()
    print('блок номер', str(block_name + 1), 'добавлен в очередь для майнинга')


    f = open('../Database/My_blocks/' + str(block_name + 1) + '.txt', 'w')
    f.writelines('block_type: Art\n')
    f.writelines('user_sender: ' + user_sender + '\n')
    f.writelines('sent_coin: -' + '\n')
    f.writelines('user_recipient: ' + user_recipient +'\n')
    f.writelines('data: ' + str(sent_coin) + '\n')
    f.writelines('previous_hash:\n')
    f.writelines('hash_key:\n')
    f.writelines('this_hash:\n')
    f.writelines('miner_name:')
    f.close()
    print('блок номер', str(block_name + 1), 'добавлен в очередь для майнинга')


    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])
            ftp.cwd('RedDrops/Block_that_needs_mining/')
            file_name = str(block_name + 1) + '.txt'                                       # Имя фала
            my_file = open('../Block_that_needs_mining/' + file_name, 'rb')                   # Директория фала
            ftp.storbinary('STOR ' + file_name, my_file)                                   # Загрузка фала на сервер
            print('Блок для майнинга', file_name, 'загружен на сервер', host[i])
            ftp.close()
            my_file.close()
        except:
            print('SERVER', host[i], 'не работает')
            break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------








Server()
Wallet()
Blockchain()
Block_that_needs_mining()
Art_info(wallet_hash)
print(wallet_hash)






#--------------------------------------------------------------------------
#                 Загрузка арта на срвера
sys.stdout.write('Хотите загрузить арт? (y/n) : ')
y_or_no = input()
if y_or_no == 'y':
    sys.stdout.write('Введите название арта: ')
    art_name = input()
    Blockchain()
    Block_that_needs_mining()
    Create_art(wallet_hash, wallet_hash, art_name)
#--------------------------------------------------------------------------








#--------------------------------------------------------------------------
#                 Передача арта другому пользователю
sys.stdout.write('Хотите передать арт? (y/n) : ')
y_or_no = input()
if y_or_no == 'y':
    sys.stdout.write('Кому хотите отправить арт?: ')
    user_recipient = input()
    sys.stdout.write('Введите название арта: ')
    art_name = input()
    Blockchain()
    Block_that_needs_mining()
    Give_art(wallet_hash, user_recipient, art_name)
#--------------------------------------------------------------------------








