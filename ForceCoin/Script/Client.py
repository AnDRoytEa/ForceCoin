import shutil
import os
import hashlib
from Script import Server
import ftplib



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def init():                                                                # Создание папок на устройстве клиента
    print('--------------------')
    folder_name = ['Database', 'Blockchain', 'Block_that_needs_mining', 'Database/Users_check', 'Database/Blockchain_check', 'Database/Block_that_needs_mining_check', 'Database/Blockchain_processing_1', 'Database/Blockchain_processing_2', 'Database/Blockchain_processing_3', 'Database/My_block_that_needs_mining']

    for i in range(len(folder_name)):
        try:
            os.mkdir(folder_name[i])
            #print('Папка --', folder_name[i], '---- Успешно создана')
        except :
            pass
            #print('Папка --', folder_name[i], '---- уже существует')

    for i in range(Server.number_servers):
        try:
            os.mkdir('Database/Blockchain_check/' + Server.host[i])
            #print('Папка -- Database/Blockchain_check/' + Server.host[i], '---- Успешно создана')
        except :
            pass
            #print('Папка -- Database/Blockchain_check/' + Server.host[i], '---- уже существует')

    for i in range(Server.number_servers):
        try:
            os.mkdir('Database/Block_that_needs_mining_check/' + Server.host[i])
            #print('Папка -- Database/Block_that_needs_mining_check/' + Server.host[i], '---- Успешно создана')
        except :
            pass
            #print('Папка -- Database/Block_that_needs_mining_check/' + Server.host[i], '---- уже существует')

    for i in range(Server.number_servers):
        try:
            os.mkdir('Database/Users_check/' + Server.host[i])
            #print('Папка -- Database/Users_check/' + Server.host[i], '---- Успешно создана')
        except :
            pass
            #print('Папка -- Database/Users_check/' + Server.host[i], '---- уже существует')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------








