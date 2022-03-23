﻿import shutil
import os
import hashlib
from Script import Server
from Script import Block_that_needs_mining
import ftplib







#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login(wallet_name, wallet_password, wallet_key):                                                # Попытка входа в кошелек
    b = bytes(str(wallet_name) + str(wallet_password) + str(wallet_key), encoding='utf-8')
    global c
    c = hashlib.md5(b).hexdigest()

    print('--------------------')
    for i in range(Server.number_servers):
        if i in Server.disconnected_servers:
            print('SERVER ' + Server.host[i], '----', 'Not connected')
            continue
        else:
            try:
                ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])                    # Конект к серверу
                ftp.cwd('ForceCoin/Database/')
                file_name = 'users.txt'  # Имя фалйа
                my_file = open('Database/Users_check/' + Server.host[i] + '/' + file_name, 'wb')        # Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)                                # Скачивание файла
                print('SERVER --',Server.host[i], 'Файл', file_name, '---- скачан')
                ftp.close()
                my_file.close()
            except :
                print('SERVER --',Server.host[i],'---- не работает')
    print('--------------------')


    users = []
    if Server.connected_servers > 1:                        # Если работает больше чем 1 сервер то выбираем самый большой USERS.TXT
        for i in range(Server.number_servers):
            try:
                file = open('Database/Users_check/' + Server.host[i] + '/users.txt', 'r')
                users.append(len(file.read()))
                file.close()
                file_name = users.index(max(users))
            except:
                file_name = i + 1

        #print(Server.host[users.index(max(users))])
        try:
            if len(open('Database/Users_check/' + Server.host[file_name] + '/users.txt', 'r').readlines()) < len(open('Database/users.txt', 'r').readlines()):
                print('Существующий файл c кошельками больше')
                shutil.copyfile('Database/users.txt', 'Database/Users_check/' + Server.host[file_name] + '/users.txt')
                print('sdf')
                upload()
            else:
                #print('sdf')
                pass
        except:
            shutil.copyfile('Database/Users_check/' + Server.host[users.index(max(users))] + '/users.txt', 'Database/users.txt')

    else:                                                  # Если работает меньше чем один сервер то выбираем USERS.TXT из первго рабочего сервера
        file_name = str(Server.host[Server.working_servers[0]])
        #print(file_name)
        shutil.copyfile('Database/Users_check/' + file_name + '/users.txt', 'Database/users.txt')




    f = open('Database/users.txt')
    z = f.readlines()
    print('Проверка имяни кошелька на доступность...')
    count = 0
    global login
    for line in z:
        if c+'\n' == line:
            count = count + 1
    f.close()
    if count > 0:
        print('Вы успешно вошли в свой кошелек!')
        login = 'YES'
    else:
        create()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

















#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create():                                                           # Создается новый кошелек


    f = open('Database/users.txt', 'a')
    f.writelines(c + '\n')
    f.close()
    print('Ваш кошелек был успешно создан!')

    print('--------------------')
    for i in range(Server.number_servers):
        if i in Server.disconnected_servers:
            print('SERVER ' + Server.host[i], '----', 'Not connected')
            continue
        else:
            try:
                ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
                ftp.cwd('/ForceCoin/Database/')
                file_name = 'users.txt'  # Имя фала
                my_file = open('Database/' + file_name, 'rb')  # Директория фала
                ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
                print('Файл', file_name, 'загружен на сервер',Server.host[i])
                ftp.close()
                my_file.close()
                Block_that_needs_mining.create_bonus1000
            except :
                print('SERVER',Server.host[i],'не работает')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

















#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def upload():                                                           # Загрузка users.txt на сервера с этого устройства
    print('--------------------')
    for i in range(Server.number_servers):
        print('SERVER ' + Server.host[i], '----', 'Not connected')
        if i in Server.disconnected_servers:
            continue
        else:
            try:
                ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])
                ftp.cwd('/ForceCoin/Database/')
                file_name = 'users.txt'  # Имя фала
                my_file = open('Database/' + file_name, 'rb')  # Директория фала
                ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
                print('Файл', file_name, 'загружен на сервер',Server.host[i])
                ftp.close()
                my_file.close()
            except :
                print('SERVER',Server.host[i],'не работает')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def balance_info(wallet_login):                                                              # Проверка баланса кошелька

    block = os.listdir('Blockchain/')
    for z in range(1000000000):
        try:
            block[z] = int(block[z][:-4])                 # Выбор названий блоков которые нужно проверить
        except:
            break
    global balance
    balance = 0



    for z in range(1000000000):                          # Проверка сколько монет мне переводили
        try:
            file = open('Blockchain/' + str(block[z]) + '.txt', 'r')
            lines = file.readlines()
            if lines[3][16:-1] == wallet_login:       # Если логин моего кошелька был в user_recipient то баланс = балас + количество отправляемых мне монет
                balance = balance + float(lines[2][11:])
                #print(file)
                #print('Вроде пару монет на кошельке есть')
            file.close()
        except:
            pass
            #print('С проверкой монет на кошельке чет не так')
            break



    for z in range(1000000000):                          # Проверка сколько монет я намайнил
        try:
            file = open('Blockchain/' + str(block[z]) + '.txt', 'r')
            lines = file.readlines()
            if lines[8][12:] == wallet_login:       # Если логин моего кошелька был в miner_name то баланс = балас + 37
                balance = balance + 0.1
                #print('Вроде пару монет на кошельке есть')
            file.close()
        except:
            pass
            #print('С проверкой монет на кошельке чет не так')
            break


    for z in range(1000000000):                          # Проверка сколько монет я тратил
        try:
            file = open('Blockchain/' + str(block[z]) + '.txt', 'r')
            lines = file.readlines()
            if lines[1][13:-1] == wallet_login:       # Если логин моего кошелька был в user_sender то баланс = балас - sent_coin
                balance = balance - float(lines[2][11:])
                #print('Вроде пару монет на кошельке есть')
            file.close()
        except:
            pass
            #print('С проверкой монет на кошельке чет не так')
            break



    try:
        balance = str(balance)[:-14]
        print('У вас на кошельке', float(balance), 'монет')
    except:
        print('У вас на кошельке 0.00 монет')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

