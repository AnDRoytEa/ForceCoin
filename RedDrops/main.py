import shutil
import os
import hashlib
import ftplib







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













init()

















