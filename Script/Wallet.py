import shutil
import os
import hashlib
from Script import Server
import ftplib








#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login(wallet_name, wallet_password):                                          # Попытка входа в кошелек
    b = bytes(wallet_name + wallet_password, encoding='utf-8')
    global c
    c = hashlib.sha256(b).hexdigest()

    print('--------------------')
    for i in range(Server.number_servers):
        try:
            ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])  # Конект к серверу
            ftp.cwd('ForceCoin/Database/')
            file_name = 'users.txt'  # Имя фалйа
            my_file = open('Database/Users_check/' + Server.host[i] + '/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
            ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)  # Скачивание файла
            print('SERVER --',Server.host[i], 'Файл', file_name, '---- скачан')
            ftp.close()
            my_file.close()
        except :
            print('SERVER --',Server.host[i],'---- не работает')
    print('--------------------')

    users = []
    for i in range(Server.number_servers):
        file = open('Database/Users_check/' + Server.host[i] + '/users.txt', 'r')
        users.append(len(file.read()))
        file.close()
        file_name = users.index(max(users))
    shutil.copyfile('Database/Users_check/' + Server.host[file_name] + '/users.txt', 'Database/users.txt')

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
        print('Такого кошелька не существует...')
        login = 'NO'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

















#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create():                                                           # Если попытка входа в кошелек не удолась, предлагается создать новый
    f = open('Database/users.txt', 'a')
    f.writelines(c + '\n')
    f.close()
    print('Ваш кошелек был успешно создан!')

    print('--------------------')
    for i in range(Server.number_servers):
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
            block[z] = int(file[z][:-4])                 # Выбор названий блоков которые нужно проверить
        except:
            break
    global balance
    balance = 0

    for z in range(1000000000):                          # Проверка сколько монет мне переводили
        try:
            file = open('Blockchain/' + str(block[z]), 'r')
            lines = file.readlines()
            if lines[2][16:-1] == wallet_login:       # Если логин моего кошелька был в user_recipient то баланс = балас + количество отправляемых мне монет
                balance = balance + int(lines[1][11:])
            file.close()
        except:
            pass
            #print('Все блоки проверенны')
            break



    for z in range(1000000000):                          # Проверка сколько монет я намайнил
        try:
            file = open('Blockchain/' + str(block[z]), 'r')
            lines = file.readlines()
            if lines[6][12:] == wallet_login:       # Если логин моего кошелька был в miner_name то баланс = балас + 37
                balance = balance + 37
            file.close()
        except:
            pass
            #print('Все блоки проверенны')
            break


    for z in range(1000000000):                          # Проверка сколько монет я тратил
        try:
            file = open('Blockchain/' + str(block[z]), 'r')
            lines = file.readlines()
            if lines[0][13:-1] == wallet_login:       # Если логин моего кошелька был в user_sender то баланс = балас - sent_coin
                balance = balance - int(lines[1][11:])
            file.close()
        except:
            pass
            #print('Все блоки проверенны')
            break

    print('У вас на кошельке', balance, 'монет')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

