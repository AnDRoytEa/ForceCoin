import ftplib
import time
import sys
import time
import sys
import os


global host, user, password, number_servers, i

host = ["93.125.18.33",         "91.106.207.15"]
user = ["androytea21",          "androylu_12"]
password = ["Daniil_Rout132",   "Daniil_Rout132"]
number_servers = len(host)
i = 0


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def init():                                                                # Проверка подключения и создание папок на серверах
    global connected_servers, disconnected_servers, working_servers
    connected_servers = number_servers
    disconnected_servers = []
    working_servers = []
    print('--------------------')
    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  #Конект к серверу
            print('SERVER ' + host[i],'----', 'Connected')
            ftp.close()
            working_servers.append(i)
        except:
            print('SERVER ' + host[i],'----', 'Not connected')
            connected_servers = connected_servers - 1
            disconnected_servers.append(i)                                # Добавление id серверов которые не работают
    if connected_servers == 0:
        print('Вам стоит скачать актуальную версию программы')
        quit()
    print('--------------------')
    #print(connected_servers)
    #print(disconnected_servers)



    folder_name = ['OpenArts', 'OpenArts/Arts']
    i = 0
    z = 0
    for i in range(number_servers):
        #print(i)
        if i in disconnected_servers:                                     # Если сервер не работает то пропускаем его
            print('SERVER ' + host[i], '----', 'Not connected')
            continue
        else:
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
            except:
                print('SERVER ' + host[i], '----', 'Not connected')
            for z in range(len(folder_name)):
                try:
                    ftp.mkd(folder_name[z])
                    print('SERVER ' + host[i],'--', folder_name[z], '---- Папки успешно созданы')
                except :
                    pass
                    print('SERVER ' + host[i],'--', folder_name[z], '---- Папки уже существуют')
            ftp.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------














