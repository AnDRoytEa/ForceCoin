import shutil
import hashlib
import ftplib

import sys
import os
import zipfile

global host, user, password, number_servers
host = ["93.125.18.33",         "91.106.207.15"]
user = ["androut",          "androylu_12"]
password = ["Daniil_Rout132",   "Daniil_Rout132"]
number_servers = len(host)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def init():                                                                # Создание папок на устройстве клиента
    print('--------------------')
    folder_name = ['System',
                   'System/Blockchain',
                   'System/Block_that_needs_mining',
                   'System/Database',
                   'System/Database/My_arts',
                   'System/Database/My_docs',
                   'System/Database/My_Blocks',
                   'System/Database/Blockchain_check',
                   'System/Database/Blockchain_check',
                   'System/Database/Blockchain_processing',
                   'System/Database/Blockchain_processing/Blockchain_processing_1',
                   'System/Database/Blockchain_processing/Blockchain_processing_2',
                   'System/Database/Blockchain_processing/Blockchain_processing_3']

    for i in range(len(folder_name)):
        try:
            os.mkdir(folder_name[i])
            print('Папка --', folder_name[i], '---- Успешно создана')
        except :
            pass
            #print('Папка --', folder_name[i], '---- уже существует')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------














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
            pass
            #my_file.close()                                                      # Закрытие директории в которую должен быть скачан файл
            #ftp.close()
            #os.remove('../Database/Blockchain.zip')
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
            pass
            #ftp.close()  # Отключение от сервера
            #print('SERVER', host[i], 'не работает')


   #print('--------------------')

    try:
        os.remove('../Database/Blockchain.zip')
    except:
        pass
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
def Coin_info(wallet_login):                                                              # Проверка баланса кошелька


    #wallet_login = wallet_login + '\n'

    block = os.listdir('../Blockchain/')
    for z in range(1000000000):
        try:
            block[z] = int(block[z][:-4])                 # Выбор названий блоков которые нужно проверить
        except:
            break
    global balance
    balance = 0.000000



    for z in range(1000000000):                          # Проверка сколько монет мне переводили
        try:
            file = open('../Blockchain/' + str(z) + '.txt', 'r')
            lines = file.readlines()
            if lines[0][12:-1] == 'Coin':
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
            file = open('../Blockchain/' + str(z) + '.txt', 'r')
            lines = file.readlines()
            if lines[8][12:] == wallet_login:       # Если логин моего кошелька был в miner_name то баланс = балас + 37
                balance = balance + 0.000301
                #print('Вроде пару монет на кошельке есть')
            file.close()
        except:
            pass
            #print('С проверкой монет на кошельке чет не так')
            break


    for z in range(1000000000):                          # Проверка сколько монет я тратил
        try:
            file = open('../Blockchain/' + str(z) + '.txt', 'r')
            lines = file.readlines()
            if lines[0][12:-1] == 'Coin':
                if lines[1][13:-1] == wallet_login:       # Если логин моего кошелька был в user_sender то баланс = балас - sent_coin
                    balance = balance - float(lines[2][11:])
                    #print('Вроде пару монет на кошельке есть')
                file.close()
        except:
            pass
            #print('С проверкой монет на кошельке чет не так')
            break


    try:
        #print(len(str(balance)))
        if len(str(balance)) > 8:
            balance = str(balance)[:8]
    except:
        pass

    try:
        print('У вас на кошельке', balance, 'монет')
    except:
        print('У вас на кошельке 0.000000 монет')
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


    for z in range(1000000000):
        try:
            if arts_name[z] in os.listdir('../Database/My_arts/'):
                continue
            else:
                try:
                    ftp = ftplib.FTP(host[1], user[1], password[1])  # Конект к серверу
                    ftp.cwd('RedDrops/Arts')
                    file_name = arts_name[z]  # Имя фалйа
                    my_file = open('../Database/My_arts/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                    ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)  # Скачивание файла
                    print('Арт', file_name, 'скачан')
                    my_file.close()
                except:
                    pass
                    break
        except:
            break

    print('Ваши арты', arts_name)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------















































init()
def Balance():
    os.chdir('System/Script/')
    global coin, arts, loading
    loading = 0
    init()
    loading = loading + 14.2
    Server()
    loading = loading + 14.2
    Wallet()
    loading = loading + 14.2
    Blockchain()
    loading = loading + 14.2
    Block_that_needs_mining()
    loading = loading + 14.2
    Coin_info(wallet_hash)
    coin = balance
    loading = loading + 14.2
    Art_info(wallet_hash)
    arts = arts_name
    loading = loading + 14.2


















import time
import random
import pygame

global FPS

pygame.init()
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w // 2
HEIGHT = infoObject.current_h // 2
#WIDTH = 720 // 2
#HEIGHT = 1280 // 2
pygame.quit()
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно

global screen, clock
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wallet")
clock = pygame.time.Clock()






def Startt():







    i = 0
    picture = pygame.image.load("ForceCoin.png").convert_alpha()
    picture = pygame.transform.scale(picture, (WIDTH // 2.2, WIDTH // 2.2))
    while i != 100:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screen.fill((17,17,17))

        #monospace Comic Sans MS
        picture.set_alpha(i)
        screen.blit(picture, (WIDTH // 3.55, HEIGHT // 40))

        myfont = pygame.font.SysFont('Comic Sans MS', HEIGHT//10)
        textsurface = myfont.render('ForceCoin', False, WHITE)
        textsurface.set_alpha(i)
        screen.blit(textsurface, (WIDTH // 2.65, HEIGHT // 1.2))

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
        i = i+1


    i = 100
    while i != 0:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screen.fill((17,17,17))

        #monospace Comic Sans MS
        picture.set_alpha(i)
        screen.blit(picture, (WIDTH // 3.55, HEIGHT // 40))

        myfont = pygame.font.SysFont('Comic Sans MS', HEIGHT//10)
        textsurface = myfont.render('ForceCoin', False, WHITE)
        textsurface.set_alpha(i)
        screen.blit(textsurface, (WIDTH // 2.65, HEIGHT // 1.2))

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
        i = i-1





    i = 0
    picture = pygame.image.load("OpenArts.png").convert_alpha()
    picture = pygame.transform.scale(picture, (WIDTH // 1.35, WIDTH // 2.3))
    while i != 100:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screen.fill((17,17,17))

        #monospace Comic Sans MS
        picture.set_alpha(i)
        screen.blit(picture, (WIDTH // 7.2, HEIGHT // 35))

        myfont = pygame.font.SysFont('Comic Sans MS', HEIGHT//10)
        textsurface = myfont.render('OpenArts', False, WHITE)
        textsurface.set_alpha(i)
        screen.blit(textsurface, (WIDTH // 2.65, HEIGHT // 1.2))

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
        i = i+1


    i = 100
    while i != 0:
        clock.tick(FPS)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screen.fill((17,17,17))

        #monospace Comic Sans MS
        picture.set_alpha(i)
        screen.blit(picture, (WIDTH // 7.2, HEIGHT // 35))

        myfont = pygame.font.SysFont('Comic Sans MS', HEIGHT//10)
        textsurface = myfont.render('OpenArts', False, WHITE)
        textsurface.set_alpha(i)
        screen.blit(textsurface, (WIDTH // 2.65, HEIGHT // 1.2))

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
        i = i-1



    th = Thread(target=Balance)
    th.start()
    time.sleep(0.1)




    while loading < 90:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)

        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((17,17,17))

        myfont = pygame.font.SysFont('Comic Sans MS', HEIGHT//15)
        textsurface = myfont.render('Loading ' + str(loading)[:2] + '%', False, WHITE)
        screen.blit(textsurface, (WIDTH // 2.5, HEIGHT // 1.35))

        pygame.draw.rect(screen, BLUE, (WIDTH // 12, HEIGHT // 1.2, WIDTH // 1.2, 40))
        pygame.draw.rect(screen, [17, 17, 17], (WIDTH // 11, HEIGHT // 1.18, WIDTH // 1.22, 28))
        pygame.draw.rect(screen, GREEN, (WIDTH // 11, HEIGHT // 1.18, loading * 6, 28))



        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    BLC()


os.listdir('../../')
def BLC():

    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 230:
                    if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 280:
                        pygame.quit()
                        quit()
                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 90:
                    if pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] <= 140:
                        run = True
                        while run:
                            clock.tick(FPS)
                            pygame.display.update()
                            pygame.display.flip()
                            continue_button = pygame.draw.rect(screen, (0, 244, 0), (150, 160, 100, 50));
                            for event in pygame.event.get():
                                # check for closing window
                                if event.type == pygame.QUIT:
                                    running = False
                                    pygame.quit()
                                    quit()




        screen.fill((17,17,17))

        #monospace Comic Sans MS

        myfont = pygame.font.SysFont('monospace', 25)
        textsurface = myfont.render('ForceCoin: ' + str(coin) + '', False, WHITE)
        screen.blit(textsurface, (10, 10))
        myfont = pygame.font.SysFont('monospace', 25)
        textsurface = myfont.render('OpenArts: ' + str(arts) + '', False, WHITE)
        screen.blit(textsurface, (10,40))

        # После отрисовки всего, переворачиваем экран


        #try:
        print(arts)
        picture = pygame.image.load("../Database/My_arts/" + arts[0]).convert_alpha()
        picture = pygame.transform.scale(picture, (WIDTH // 1.35, WIDTH // 2.3))
        picture.set_alpha(100)
        screen.blit(picture, (WIDTH // 2, HEIGHT // 2))
        print(arts)
        #except:
           # pass













        start_button = pygame.draw.rect(screen, (0, 0, 240), (150, 90, 100, 50));

        #continue_button = pygame.draw.rect(screen, (0, 244, 0), (150, 160, 100, 50));

        quit_button = pygame.draw.rect(screen, (244, 0, 0), (150, 230, 100, 50));



















        pygame.display.flip()
    pygame.quit()








from threading import Thread



Startt()
#run = True
#if run == True:
#    th = Thread(target=Startt)
#    th.start()








