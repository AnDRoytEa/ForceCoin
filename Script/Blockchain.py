import os
import ftplib
from Script import Server
import  shutil
import time






#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def download():                                                                # Скачивание всех блоков из блокчейна
    i = 0
    z = 0
    print('--------------------')
    for i in range(Server.number_servers):                                           # Цикл от сервера №0 до последнего сервера
        try:
            ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])     # Подключение к серверу
            ftp.cwd('ForceCoin/Blockchain/')                                         # Переход в нужную деррикторию
            #print('Успешно подключился к серверу', Server.host[i])
        except:
            pass
            #print('Не удалось подключтся к серверу', host[i])
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
                #print('SERVER', Server.host[i] ,'Все блоки скачаны')

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
            shutil.copyfile('Database/Blockchain_check/' + Server.host[maxx.index(max(maxx))] + '/' + str(i) + '.txt', 'Database/Blockchain_processing/' + str(i) + '.txt')
            #print('Все супер')
        except:
            pass
            #print('Копирование блоков в Blockchain_processing Завершено')
            #print('--------------------')
            break






    for z in range(1000000000):                                # Проверка блоков на правильность
        try:
            file_z = open('Database/Blockchain_processing/' + str(z) + '.txt', 'r')             # открытие блока под номером i
            file_z1 = open('Database/Blockchain_processing/' + str(z+1) + '.txt', 'r')          # открытие блока под номером i + 1

            block_z = file_z.readlines()
            block_z1 = file_z1.readlines()
            #print(block_z[5][11:])
            #print(block_z1[4][15:])

            if block_z[5][11:] == block_z1[4][15:]:                                              # Цикл для проверки предыдущих хэшей блока
                shutil.copyfile('Database/Blockchain_processing/' + str(z) + '.txt','Blockchain/' + str(z) + '.txt')
                print('Блок номер', z, 'Добавлен в блокчейн')

        except:
            try:
                shutil.copyfile('Database/Blockchain_processing/' + str(z) + '.txt', 'Blockchain/' + str(z) + '.txt')
                print('Блок номер', z, 'Добавлен в блокчейн')
            except:
                pass
                #print('неа')
            break


        file_z.close()
        file_z1.close()
    upload()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






def upload():
    for i in range(Server.number_servers):
        ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
        ftp.cwd('/ForceCoin/Blockchain/')
        for z in range(1000000000):
            try:
                file_name = str(z) + '.txt'                                                   # Имя фала
                my_file = open('Blockchain/' + file_name, 'rb')                               # Директория фала
                ftp.storbinary('STOR ' + file_name, my_file)                                  # Загрузка фала на сервер
                #print('Блок для майнинга', file_name, 'загружен на сервер', Server.host[i])
                my_file.close()
            except:
                #print('SERVER', Server.host[i], 'не работает')
                break
        ftp.close()










