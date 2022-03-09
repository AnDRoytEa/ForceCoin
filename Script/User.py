import shutil
import os
import hashlib
from Script import Server
import ftplib





def login(wallet_name, wallet_password):
    b = bytes(wallet_name + wallet_password, encoding='utf-8')
    global c
    c = hashlib.sha256(b).hexdigest()


    i = 0
    print('--------------------')
    for i in range(Server.number_servers):
        try:
            ftp = ftplib.FTP(Server.host[i], Server.user[i], Server.password[i])  # Конект к серверу
            ftp.cwd('ForceCoin/Database/')
            file_name = 'users.txt'  # Имя фалйа
            my_file = open('Database/Users_check/' + Server.host[i] + '_' + file_name, 'wb')  # Директория в котрую будет сохранен файл
            ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)  # Скачивание файла
            print('SERVER',Server.host[i], 'Файл', file_name, 'скачан')
            ftp.close()
            my_file.close()
        except :
            print('SERVER',Server.host[i],'не работает')
    print('--------------------')



    users_check = os.listdir('Database/Users_check/')
    i = 0
    index = []
    for i in range(len(users_check)):
        file = open('Database/Users_check/' + users_check[i], 'r')
        z = len(file.read())
        index.append(z)
        file.close()
    i = 0
    for i in range(len(users_check)):
        file = open('Database/Users_check/' + users_check[i], 'r')
        z = len(file.read())
        if max(index) == z:
            file_name = users_check[i]
            break
            file.close()
    shutil.copyfile('Database/Users_check/' + file_name, 'Database/users.txt')



    f = open('Database/users.txt')
    z = f.readlines()
    print('Проверка имяни кошелька на доступность...')
    count = 0
    global j
    for line in z:
        if c+'\n' == line:
            count = count + 1
    f.close()
    if count > 0:
        print('Вы успешно вошли в свой кошелек!')
        j = ''
    else:
        print('Такого кошелька не существует...')
        j = 'n'





def create_new_login():
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











def create_base_folder():
    print('--------------------')
    folder_name = ['Database', 'Blockchain', 'Block_that_needs_mining', 'Database/Users_check', 'Database/Blockchain_check', 'Database/Block_that_needs_mining_check' ,'Database/Blockchain_processing']
    i = 0
    for i in range(len(folder_name)):
        try:
            os.mkdir(folder_name[i])
            print('Папка', folder_name[i], 'Успешно создана')
        except :
            print('Папка', folder_name[i], 'уже существует')
    for i in range(Server.number_servers):
        try:
            os.mkdir('Database/Blockchain_check/' + Server.host[i])
            print('Папка', Server.host[i], 'Успешно создана')
        except :
            print('Папка Database/Blockchain_check/' + Server.host[i], 'уже существует')
    for i in range(Server.number_servers):
        try:
            os.mkdir('Database/Block_that_needs_mining_check/' + Server.host[i])
            print('Папка Database/Block_that_needs_mining_check/', Server.host[i], 'Успешно создана')
        except :
            print('Папка Database/Block_that_needs_mining_check/' + Server.host[i], 'уже существует')










def remove_unnecessary_checking_block():
    block_folder = os.listdir('Database/Blockchain_check/')
    i = 0
    z = 0
    block_name = 0
    for i in range(len(block_folder)):
        for block_name in range(3):
            file = open('Database/Blockchain_check/' + Server.host[i] + '/' + str(block_name) + '.txt', 'r')
            len_file = len(file.read())
            if len_file == 0:
                file.close()
                os.remove('Database/Blockchain_check/' + Server.host[i] + '/' + str(block_name) + '.txt')
                print('Ненужный блок удален удален')
                print('--------------------')


