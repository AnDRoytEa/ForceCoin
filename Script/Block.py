import os
import ftplib
from  Script import Server
import  shutil
import time







def download_blockchain():
    i = 0
    z = 0
    print('--------------------')
    for i in range(Server.number_servers):                                           # Цикл от сервера №0 до последнего сервера
        try:
            ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])     # Подключение к серверу
            ftp.cwd('ForceCoin/Blockchain/')                                         # Переход в нужную деррикторию
            print('Успешно подключился к серверу', Server.host[i])
        except:
            print('Не удалось подключтся к серверу', host[i])
        for z in range(1000000000):                                                  # Цикл для скачнивания блока от 0 до последнего
            try:
                file_name = str(z) + '.txt'                                          # Имя фалйа
                my_file = open('Database/Blockchain_check/' + Server.host[i] + '/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)             # Скачивание файла
                print('SERVER', Server.host[i], 'блок', file_name, 'скачан')
                my_file.close()                                                      # Закрытие директории в которую должен быть скачан файл
            except:
                my_file.close()                                                      # Закрытие директории в которую должен быть скачан файл
                os.remove('Database/Blockchain_check/' + Server.host[i] + '/' + str(z) + '.txt')  # Удаление последнего бракованого блока
                print('SERVER', Server.host[i] ,'Все блоки скачаны')

                break
        print('--------------------')
        ftp.close()                                                                  # Отключение от сервера




    maxx = []                                                             # Максимальное количество блоков на сервере
    for i in range(Server.number_servers):
        blocks = []                                                       # Количество блоков на сервере
        for z in range(1000000000):
            try:
                blocks.append(int(os.listdir('Database/Blockchain_check/' + Server.host[i] + '/')[z][:-4]))
            except:
                maxx.append(max(blocks))
                break

    #print(maxx)
    #print(maxx.index(max(maxx)))
    for i in range(1000000000):                                           # Цикл для скачнивания блока от 0 до последнего
        try:
            shutil.copyfile('Database/Blockchain_check/' + Server.host[maxx.index(max(maxx))] + '/' + str(i) + '.txt', 'Database/Blockchain_processing/' + str(i) + '.txt')
            #print('Все супер')
        except:
            print('Копирование блоков в Blockchain_processint Завершено')
            print('--------------------')
            break


    for z in range(1000000000):
        try:
            file_z = open('Database/Blockchain_processing/' + str(z) + '.txt', 'r')
            file_z1 = open('Database/Blockchain_processing/' + str(z+1) + '.txt', 'r')

            block_z = file_z.readlines()
            block_z1 = file_z1.readlines()
            #print(block_z[5][11:])
            #print(block_z1[4][15:])

            if block_z[5][11:] == block_z1[4][15:]:
                shutil.copyfile('Database/Blockchain_processing/' + str(z) + '.txt','Blockchain/' + str(z) + '.txt')
                print('Блок номер', z, 'Добавлен в блокчейн')

        except:
            shutil.copyfile('Database/Blockchain_processing/' + str(z) + '.txt', 'Blockchain/' + str(z) + '.txt')
            print('Блок номер', z, 'Добавлен в блокчейн')
            break

        file_z.close()
        file_z1.close()













def download_block_that_needs_mining():
    global bbb
    i = 0
    bbb = len(os.listdir('BlockChain/'))
    for i in range(Server.number_servers):

        for z in range(bbb,1000000000):

            try:
                ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])  # Конект к серверу
                ftp.cwd('ForceCoin/Block_that_needs_mining/')
                file_name = str(z) + '.txt'  # Имя фалйа
                my_file = open('Database/Block_that_needs_mining_check/' + Server.host[i] + '/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)  # Скачивание файла
                print('SERVER', Server.host[i], 'Файл', file_name, 'скачан')
                ftp.close()
                my_file.close()
            except:
                my_file.close()
                print('SERVER', Server.host[i], 'блок', file_name, ' из Blockc_that_needs_mining НЕ скачан')
                os.remove('Database/Block_that_needs_mining_check/' + Server.host[i] + '/' + file_name)
                print('Ненужный блок удален')
                print('--------------------')
                break

    i = 0
    z = 0
    check_block_max = []
    for i in range(Server.number_servers):
        check_block = os.listdir('Database/Block_that_needs_mining_check/' + Server.host[i] + '/')
        for z in range(len(check_block)):
            check_block[z] = int(check_block[z][:-4])
        print(check_block)
        try:
            check_block_max.append(max(check_block))
        except:
            check_block_max.append(-1)
            check_block_max.append(-2)
        print(check_block_max)


        right_block_that_needs_mining = (check_block_max.index(max(check_block_max)) + 1)
        for i in range(bbb,1000000000):
            try:
                copy_block = ('Database/Block_that_needs_mining_check/' + Server.host[right_block_that_needs_mining] + '/') + str(i) + '.txt'
                print(copy_block)
                shutil.copyfile(copy_block, 'Block_that_needs_mining/' + str(i) + '.txt')
            except:
                print('Вроде все)')
                break














def create_bonus1000_block_that_needs_to_mining(user_recipient):
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


    i = 0
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
                f.writelines('sent_coin: 1000\n')
                f.writelines('user_recipient: ' + user_recipient +'\n')
                f.writelines('data: 02.03.2022\n')
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
                        print('SERVER', Server.host[i], 'не работает')


                i = 100
                break
            else:
                i = +1








