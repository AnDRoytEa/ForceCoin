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


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def init():                                                                # Проверка подключения и создание папок на серверах
    print('--------------------')
    connected_servers = number_servers
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  #Конект к серверу
            print('SERVER ' + host[i],'----', 'Connected')
            ftp.close()
        except :
            print('SERVER ' + host[i],'----', 'Not connected')
            connected_servers = connected_servers - 1
    if connected_servers == 0:
        print('Вам стоит скачать актуальную версию программы')
        quit()



    folder_name = ['ForceCoin', 'ForceCoin/Database', 'ForceCoin/Blockchain', 'ForceCoin/Block_that_needs_mining']
    i = 0
    z = 0
    for i in range(number_servers):
        ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
        for z in range(len(folder_name)):
            try:
                ftp.mkd(folder_name[z])
                #print('SERVER ' + host[i],'--', folder_name[z], '---- YES')
            except :
                pass
                #print('SERVER ' + host[i],'--', folder_name[z], '---- NO')
        ftp.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------














