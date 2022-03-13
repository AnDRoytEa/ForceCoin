import os
import ftplib
from Script import Server
import  shutil
import time
from datetime import date






#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clear():                                                                # Удаление старых блоков для майнинга
    minn_block = os.listdir('Block_that_needs_mining')
    for z in range(1000000000):
        try:
            minn_block[z] = int(minn_block[z][:-4])
        except:
            break
    print(minn_block)

    try:
        for z in range(min(minn_block),1000000000):
            try:
                os.remove(os.path.join('Block_that_needs_mining', str(z) + '.txt'))
            except:
                break
    except:
        pass

    try:
        for i in range(Server.number_servers):
            for z in range(min(minn_block),1000000000):
                try:
                    os.remove(os.path.join('Database/Block_that_needs_mining_check/' + Server.host[i], str(z) + '.txt'))
                except:
                    break
    except:
        pass

    print('Отчищен block_that_needs_mining')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------














#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def download():                                                                # Скачивание блоков для майнинга
    global bbb
    i = 0
    bbb = len(os.listdir('BlockChain/'))

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

    print('--------------------')
    for i in range(Server.number_servers):

        for z in range(block_name+1,1000000000):

            try:
                ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])                                # Конект к серверу
                ftp.cwd('ForceCoin/Block_that_needs_mining/')
                file_name = str(z) + '.txt'  # Имя фалйа
                my_file = open('Database/Block_that_needs_mining_check/' + Server.host[i] + '/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)                                            # Скачивание файла блоков в папку сервера из которого они загруженны
                print('SERVER', Server.host[i], 'Файл', file_name, 'скачан')
                ftp.close()
                my_file.close()
            except:
                my_file.close()
                print('SERVER', Server.host[i], 'блок', file_name, ' из Blockc_that_needs_mining НЕ скачан')
                os.remove('Database/Block_that_needs_mining_check/' + Server.host[i] + '/' + file_name)
                #print('Ненужный блок удален')
                break
    print('--------------------')

    i = 0
    z = 0
    check_block_max = []
    for i in range(Server.number_servers):                                                          # Цикл для проверки на каком из серверов больше блоков для майнинга
        check_block = os.listdir('Database/Block_that_needs_mining_check/' + Server.host[i] + '/')
        for z in range(len(check_block)):
            check_block[z] = int(check_block[z][:-4])
        #print(check_block)
        try:
            check_block_max.append(max(check_block))                                         # Вычисление максимального количества блоков в папке сервера с которого блоки скачаны
        except:
            check_block_max.append(-1)
            check_block_max.append(-2)
        #print(check_block_max)


        right_block_that_needs_mining = (check_block_max.index(max(check_block_max)) + 1)
        for i in range(block_name+1,1000000000):                                                    # Цикл для одобрения блоков и добавления их в папку block_that_needs_mining
            try:
                copy_block = ('Database/Block_that_needs_mining_check/' + Server.host[right_block_that_needs_mining] + '/') + str(i) + '.txt'
                #print(copy_block)
                shutil.copyfile(copy_block, 'Block_that_needs_mining/' + str(i) + '.txt')          # Копирование правильных блоков
            except:
                #print('Вроде все)')
                break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






















#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_bonus1000(user_recipient):                                   # Бонус в размере 94 манет для первых 100 пользователей сети
    lbi_blockchain = []                     #last_block_in_blockchain
    lbi_block_that_needs_mining = []        #last_block_in_block_that_needs_mining
    mbi_blockchain = -1                     #max_block_in_blockchain
    mbi_block_that_needs_mining = -1        #max_block_in_block_that_needs_mining

    i = 0
    blockchain_check = os.listdir('Blockchain/')
    for i in range(len(blockchain_check)):
        try:

            z = int(blockchain_check[i][:-4])
            lbi_blockchain.append(z)
        except:
            print('Чет не так')

    i = 0
    block_that_needs_mining_check = os.listdir('Block_that_needs_mining/')
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


    current_date = date.today()
    f = open('Database/users.txt')
    z = f.readlines()
    print('Проверка имяни кошелька на доступность...')
    count = 0
    while i != 100:
        for line in z:
            if user_recipient + '\n' == line:
                print("Вы в первой сотне")

                f = open('Block_that_needs_mining/' + str(block_name + 1) + '.txt', 'w')
                f.writelines('user_sender: Bonus1000\n')
                f.writelines('sent_coin: 94\n')
                f.writelines('user_recipient: ' + user_recipient +'\n')
                f.writelines('data: ' + str(current_date) + '\n')
                f.writelines('previous_hash:\n')
                f.writelines('this_hash:\n')
                f.writelines('miner_name:')
                f.close()
                print('блок номер', str(block_name + 1), 'добавлен в очередь для майнинга')

                i = 0
                for i in range(Server.number_servers):
                    try:
                        ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
                        ftp.cwd('/ForceCoin/Block_that_needs_mining/')
                        file_name = str(block_name + 1) + '.txt'  # Имя фала
                        my_file = open('Block_that_needs_mining/' + file_name, 'rb')  # Директория фала
                        ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
                        print('Блок для майнинга', file_name, 'загружен на сервер', Server.host[i])
                        ftp.close()
                        my_file.close()
                    except:
                        pass
                        print('SERVER', Server.host[i], 'не работает')


                i = 100
                break
            else:
                i = +1
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------













































#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create(user_sender, user_recipient, sent_coin):                           # Создание блока для майнинга в котором осуществляется перевод монет
    lbi_blockchain = []                     #last_block_in_blockchain
    lbi_block_that_needs_mining = []        #last_block_in_block_that_needs_mining
    mbi_blockchain = -1                     #max_block_in_blockchain
    mbi_block_that_needs_mining = -1        #max_block_in_block_that_needs_mining

    i = 0
    blockchain_check = os.listdir('Blockchain/')
    for i in range(len(blockchain_check)):
        try:

            z = int(blockchain_check[i][:-4])
            lbi_blockchain.append(z)
        except:
            print('Чет не так')

    i = 0
    block_that_needs_mining_check = os.listdir('Block_that_needs_mining/')
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


    current_date = date.today()
    f = open('Database/users.txt')
    z = f.readlines()
    print('Проверка имяни кошелька на доступность...')
    count = 0
    while i != 100:
        for line in z:
            if user_recipient + '\n' == line:
                print("Вы в первой сотне")

                f = open('Block_that_needs_mining/' + str(block_name + 1) + '.txt', 'w')
                f.writelines('user_sender: ' + user_sender + '\n')
                f.writelines('sent_coin: ' + str(sent_coin) + '\n')
                f.writelines('user_recipient: ' + user_recipient +'\n')
                f.writelines('data: ' + str(current_date) + '\n')
                f.writelines('previous_hash:\n')
                f.writelines('this_hash:\n')
                f.writelines('miner_name:')
                f.close()
                print('блок номер', str(block_name + 1), 'добавлен в очередь для майнинга')

                i = 0
                for i in range(Server.number_servers):
                    try:
                        ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
                        ftp.cwd('/ForceCoin/Block_that_needs_mining/')
                        file_name = str(block_name + 1) + '.txt'                                       # Имя фала
                        my_file = open('Block_that_needs_mining/' + file_name, 'rb')                   # Директория фала
                        ftp.storbinary('STOR ' + file_name, my_file)                                   # Загрузка фала на сервер
                        print('Блок для майнинга', file_name, 'загружен на сервер', Server.host[i])
                        ftp.close()
                        my_file.close()
                    except:
                        print('SERVER', Server.host[i], 'не работает')
                        break


                i = 100
                break
            else:
                i = +1
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------