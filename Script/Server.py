import ftplib
import time
import sys
import time
import sys
import os


global host, user, password, number_servers, i

host = ["93.125.18.33",         "91.106.207.15"]
user = ["androyt",              "androylu_12"]
password = ["Daniil_Rout132",   "Daniil_Rout132"]
number_servers = len(host)

i = 0



def connect():
    print('--------------------')
    connected_servers = number_servers
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  #Конект к серверу
            print('SERVER ' + host[i],'-----', 'Connected')
            ftp.close()
        except :
            print('SERVER ' + host[i],'-----', 'Not connected')
            connected_servers = connected_servers - 1
    if connected_servers == 0:
        print('Вам стоит скачать актуальную версию программы')
        quit()
    print('--------------------')


    folder_name = ['ForceCoin', 'ForceCoin/Database', 'ForceCoin/Blockchain', 'ForceCoin/Block_that_needs_mining']
    i = 0
    z = 0
    for z in range(number_servers):
        for i in range(len(folder_name)):
            try:
                ftp = ftplib.FTP(host[z], user[z], password[z])  # Конект к серверу
                ftp.mkd(folder_name[i])
                print('SERVER ' + host[z],'--', folder_name[i], '----- YES')
                ftp.close()
            except :
                print('SERVER ' + host[z],'--', folder_name[i], '----- NO')
    i = 0




def show_files(file_directory):
    print('--------------------')
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])
            ftp.cwd(file_directory)
            ftp.retrlines('NLST') #Показ файлов в директории
            ftp.close()
        except :
            print('SERVER ' + host[i], 'не работает')
        print('--------------------')



def download_folse_blockchain():
    global block_number
    block_number = 0
    for i in range(number_servers):
        for block_number in range(1000000000):
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
                ftp.cwd('ForceCoin/Blockchain/')
                #ftp.retrlines('NLST')  # Показ файлов в директории
                file_name = str(block_number) + '.txt'  # Имя фалйа
                my_file = open('Database/Blockchain_check/' + host[i] + '/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)  # Скачивание файла
                #print('SERVER',host[i], 'Файл', file_name, 'скачан')
                #print('--------------------')
                ftp.close()
                my_file.close()
            except :
                print('SERVER',host[i],'Все блоки скачаны')
                break
    print('--------------------')







def download_folse_block_that_needs_mining():
    global block_number
    block_number = 0
    for i in range(number_servers):
        for block_number in range(1000000000):
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
                ftp.cwd('ForceCoin/Block_that_needs_mining/')
                #ftp.retrlines('NLST')  # Показ файлов в директории
                file_name = str(block_number) + '.txt'  # Имя фалйа
                my_file = open('Database/Block_that_needs_mining_check/' + host[i] + '/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)  # Скачивание файла
                #print('SERVER',host[i], 'Файл', file_name, 'скачан')
                #print('--------------------')
                ftp.close()
                my_file.close()
            except :
                print('SERVER',host[i],'Все блоки которые нужно майнить не скачаны')
                break
    print('--------------------')









def upload_true_block_that_needs_mining():
    print('--------------------')
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])
            ftp.cwd('/ForceCoin/Block_that_needs_mining/')
            file_name = 'users.txt'  # Имя фала
            my_file = open('Database/' + file_name, 'rb')  # Директория фала
            ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
            print('Файл', file_name, 'загружен на сервер',host[i])
            ftp.close()
            my_file.close()
        except :
            print('SERVER',host[i],'не работает')



