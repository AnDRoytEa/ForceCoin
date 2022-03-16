import os
import ftplib
from Script import Server
from Script import Wallet
import  shutil
import time
import hashlib




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def download():                                                                # Скачивание всех блоков из блокчейна в свои папки
    i = 0
    z = 0

    lbi_blockchain = []
    blockchain_check = os.listdir('Blockchain/')
    for i in range(len(blockchain_check)):
        try:

            z = int(blockchain_check[i][:-4])
            lbi_blockchain.append(z)
        except:
            print('Чет не так')


    try:
        mbi_blockchain = max(lbi_blockchain)
    except:
        mbi_blockchain = -1

    print('--------------------')
    for i in range(Server.number_servers):                                           # Цикл от сервера №0 до последнего сервера
        try:
            ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])     # Подключение к серверу
            ftp.cwd('ForceCoin/Blockchain/')                                         # Переход в нужную деррикторию
            #print('Успешно подключился к серверу', Server.host[i])
        except:
            pass
            #print('Не удалось подключтся к серверу', host[i])
        for z in range(mbi_blockchain + 1, 1000000000):                                                  # Цикл для скачнивания блока от 0 до последнего
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
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    check_1()
    check_2()
    check_3()
    check_4()
    server_clean()
    upload()




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def check_1():                                                     # Нахождение папки с максимальным количеством блоков
    maxx = []                                                             # Максимальное количество блоков на сервере
    for i in range(Server.number_servers):
        blocks = []                                                       # Количество блоков на сервере
        for z in range(1000000000):
            try:
                blocks.append(int(os.listdir('Database/Blockchain_check/' + Server.host[i] + '/')[z][:-4]))
            except:
                try:
                    maxx.append(max(blocks))
                except:
                    maxx.append(0)
                    maxx.append(-1)
                break


    #print(maxx)
    #print(maxx.index(max(maxx)))
    for i in range(1000000000):                                           # Цикл для скачнивания блока от 0 до последнего
        try:
            shutil.copyfile('Database/Blockchain_check/' + Server.host[maxx.index(max(maxx))] + '/' + str(i) + '.txt', 'Database/Blockchain_processing_1/' + str(i) + '.txt')
            #print('Все супер')
        except:
            pass
            #print('Копирование блоков в Blockchain_processing Завершено')
            #print('--------------------')
            break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







def check_2():
    try:
        for z in range(1000000000):
            try:
                file = open('Database/Blockchain_processing_1/' + str(z) + '.txt', 'r')
                block = file.readlines()
                file.close()
                user_sender = block[0][13:-1]
                sent_coin =  block[1][11:-1]
                user_recipient = block[2][16:-1]
                data = block[3][6:-1]
                previous_hash = block[4][15:-1]
                hash_key = block[5][10:-1]
                this_hash = block[6][11:-1]
                miner_name = block[7][12:]
            except:
                break

            b = bytes(str(user_sender) + str(sent_coin) + str(user_recipient) + str(data) + str(previous_hash) + str(hash_key) + str(miner_name), encoding='utf-8')
            hash = hashlib.sha256(b).hexdigest()
            #print(this_hash)
            #print(hash)

            if hash == this_hash:
                if this_hash[:5] == '00000':
                    print('Хэш блока номер',z , 'праввильный')
                    shutil.copyfile('Database/Blockchain_processing_1/' + str(z) + '.txt', 'Database/Blockchain_processing_2/' + str(z) + '.txt')
            else:
                print('Хэш блока номер', z, 'не сходится, блок не правильный')
    except:
        print('неа')







def check_3():                                            # Проверка правильная ли последовательность хэшей у блоков
    try:
        shutil.copyfile('Database/Blockchain_processing_2/' + '0' + '.txt', 'Database/Blockchain_processing_3/' + '0' + '.txt')
        print('Блок номер','0 Добавлен в блокчейн')
    except:
        pass

    for z in range(1000000000):                                # Проверка блоков на правильность
        try:
            file_z = open('Database/Blockchain_processing_2/' + str(z) + '.txt', 'r')             # открытие блока под номером i
            file_z1 = open('Database/Blockchain_processing_2/' + str(z+1) + '.txt', 'r')          # открытие блока под номером i + 1

            block_z = file_z.readlines()
            block_z1 = file_z1.readlines()
            file_z.close()
            file_z1.close()
            #print(block_z[5][11:])
            #print(block_z1[4][15:])
            #print(block_z[1][11:][:-1])




            if block_z[6][11:] == block_z1[4][15:]:  # Цикл для проверки предыдущих хэшей блока
                if int(block_z1[1][11:-1]) > 0:
                    shutil.copyfile('Database/Blockchain_processing_2/' + str(z+1) + '.txt', 'Database/Blockchain_processing_3/' + str(z+1) + '.txt')
                    print('Блок номер', z+1, '----- предыдущий хэш и количество передаваемых монет правильное')
            else:

                break
        except:
            break
                # print('неа')
        file_z.close()
        file_z1.close()



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------













#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def check_4():                                                     # Нахождение папки с максимальным количеством блоков


    for i in range(1000000000):                                           # Цикл для скачнивания блока от 0 до последнего
        try:
            file = open('Database/Blockchain_processing_3/' + str(i) + '.txt', 'r')
            block = file.readlines()
            file.close()
            user_sender = block[0][13:-1]

            if user_sender == Wallet.c:
                try:
                    file = open('Database/My_block_that_needs_mining/' + str(i) + '.txt', 'r')
                    file.close()
                    shutil.copyfile('Database/Blockchain_processing_3/' + str(i) + '.txt','Blockchain/' + str(i) + '.txt')
                except:
                    print('С вашего счета пытались спиздить монетки')
                    break

            shutil.copyfile('Database/Blockchain_processing_3/' + str(i) + '.txt', 'Blockchain/' + str(i) + '.txt')

        except:
            break

        #print(user_sender)
        #print(Wallet.c)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
























def client_clean():
    for i in range(Server.number_servers):
        for z in range(1000000000):
            try:
                os.remove('Database/Blockchain_check/' + Server.host[i] + '/' + str(z) + '.txt')
                print('Из папки Database/Blockchain_check/', Server.host[i], 'блок', str(z) + '.txt', 'удален')
            except:
                break
    for z in range(1000000000):
        try:
            print(z)
            os.remove('Database/Blockchain_processing_1/' + str(z) + '.txt')
            os.remove('Database/Blockchain_processing_2/' + str(z) + '.txt')
            os.remove('Database/Blockchain_processing_3/' + str(z) + '.txt')
            print('Из папки Database/Blockchain_processing/', Server.host[i], 'блок', str(z) + '.txt', 'удален')
        except:
            break



def server_clean():
    for i in range(Server.number_servers):
        ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])  # Конект к серверу
        ftp.cwd('ForceCoin/Blockchain/')
        for z in range(1000000000):
            try:
                ftp.delete(str(z) + '.txt')
                print('SERVER', Server.host[i], 'блок', str(z) + '.txt', 'удален')
            except:
                break



def upload():
    for i in range(Server.number_servers):
        ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
        ftp.cwd('/ForceCoin/Blockchain/')
        for z in range(1000000000):
            try:
                file_name = str(z) + '.txt'                                                   # Имя фала
                my_file = open('Blockchain/' + file_name, 'rb')                               # Директория фала
                ftp.storbinary('STOR ' + file_name, my_file)                                  # Загрузка фала на сервер
                print('Блок для майнинга', file_name, 'загружен на сервер', Server.host[i])
                my_file.close()
            except:
                #print('SERVER', Server.host[i], 'не работает')
                break
        ftp.close()










