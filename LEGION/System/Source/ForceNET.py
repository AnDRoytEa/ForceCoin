import os
import time
import rsa
import ftplib
import base64
import shutil
import random
import hashlib
import zipfile



#os.chdir('../../')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def server_init():                                                                # Проверка подключения и создание папок на серверах
    global host, user, password, number_servers
    host = []
    user = []
    password = []
    for i in range(9):
        try:
            f = open('System/Database/Servers_data/' + str(i) + '.txt', 'r')
            host.append(f.readlines(1)[0][:-1])
            user.append(f.readlines(2)[0][:-1])
            password.append(f.readlines(3)[0])
            f.close()
        except:
            break

    non = 0
    ret = 'failed'
    for i in range(len(host)):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
            ftp.close()
            ret = 'done'
        except:
            host[i] = '0'
            user[i] = '0'
            password[i] = '0'
            non = non + 1
            pass

    for i in range(non):
        host.remove('0')
        user.remove('0')
        password.remove('0')

    number_servers = len(host)
    #print(number_servers)

    if ret == 'done':
        return 'done'
    else:
        return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def folder_init(place):
    if place == 'server':
        ret = 'failed'
        folder_name = ['LEGION',
                       'LEGION/Database',
                       'LEGION/Blockchain',
                       'LEGION/Block_that_needs_mining',
                       'LEGION/NFT']
        for i in range(number_servers):
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
                for z in range(len(folder_name)):
                    try:
                        ftp.mkd(folder_name[z])
                        ret = 'done'
                    except:
                        pass
                ftp.close()
            except:
                pass
        if ret == 'done':
            return 'done'
        else:
            return 'failed'



    if place == 'client':
        ret = 'failed'
        folder_name = ['System',
                       'System/Source',
                       'System/Blockchain',
                       'System/Block_that_needs_mining',
                       'System/Database',
                       'System/Database/NFT',
                       'System/Database/Wallet_keys',
                       'System/Database/Servers_data',
                       'System/Database/Blockchain_processing',
                       'System/Database/Block_that_needs_mining_processing',
                       'System/Database/Blockchain_processing/Blockchain_processing_0',
                       'System/Database/Blockchain_processing/Blockchain_processing_1',
                       'System/Database/Blockchain_processing/Blockchain_processing_2',
                       'System/Database/Blockchain_processing/Blockchain_processing_3']
        for i in range(len(folder_name)):
            try:
                os.mkdir(folder_name[i])
                ret = 'done'
            except:
                pass
                ret = 'done'
        if ret == 'done':
            return 'done'
        else:
            return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def wallet(option):
    global wallet_address, publicKey, privateKey
    if option == 'keys_init':
        try:
            f = open('System/Database/Wallet_keys/public_key.txt', 'r')  # Чтение файла кошелька
            key = f.readlines()
            f.close()
            publicKey = str(key[0] + key[1] + key[2] + key[3])
            publicKey = rsa.PublicKey.load_pkcs1(publicKey)
            wallet_address = key[1][:-1] + key[2][:-1]

            f = open('System/Database/Wallet_keys/private_key.txt', 'r')  # Чтение файла кошелька
            key = f.readlines()
            f.close()
            privateKey = str(key[0] + key[1] + key[2] + key[3] + key[4] + key[5] + key[6] + key[7] + key[8])
            privateKey = rsa.PrivateKey.load_pkcs1(privateKey)
            return 'done'
        except:
            return 'failed'

    if option == 'create_keys':
        try:
            f = open('System/Database/Wallet_keys/public_key.txt', 'r')  # Чтение файла кошелька
            f.close()
            f = open('System/Database/Wallet_keys/private_key.txt', 'r')  # Чтение файла кошелька
            f.close()
            return 'failed'
        except:
            try:
                publicKey, privateKey = rsa.newkeys(512)
                publicKey = publicKey.save_pkcs1().decode('utf8')
                privateKey = privateKey.save_pkcs1().decode('utf8')
                f = open('System/Database/Wallet_keys/public_key.txt', 'w')  # Создание файла данных кошелька, запись данных
                f.writelines(publicKey)
                f.close()
                f = open('System/Database/Wallet_keys/private_key.txt', 'w')  # Создание файла данных кошелька, запись данных
                f.writelines(privateKey)
                f.close()
                return 'done'
            except:
                return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def balance_info(option, wallet):
    if option == 'coin':
        balance = 0.00000000
        try:
            f = open('System/Database/Wallet_keys/public_key.txt', 'r')  # Чтение файла кошелька
            f.close()
        except:
            return 'failed'

        try:
            for i in range(1000000000):
                block = read_block('blockchain_processing_0', i)
                block_number = block[0]
                object_type = block[1]
                user_sender = block[2]
                sent_object = block[3]
                user_recipient = block[4]
                data = block[5]
                signature = block[6]
                hash_key = block[7]
                miner_name = block[8]
                previous_hash = block[9]
                this_hash = block[10]

                if miner_name == wallet:
                    balance = balance + 0.00030700

                if object_type == 'coin' and sent_object != '-':
                    if user_recipient == wallet:
                        balance = balance + float(sent_object)
                    if user_sender == wallet:
                        balance = balance - float(sent_object)
        except:
            pass

        if len(str(balance)) < 10:
            return balance
        if len(str(balance)) > 10:
            return str(balance)[:10]


    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def download(type):
    if type == 'blockchain':
        ret = 'failed'
        for i in range(number_servers):                                           # Цикл от сервера №0 до последнего сервера
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])               # Конект к серверу
                ftp.cwd('LEGION/Blockchain/')
                file_name = 'Blockchain.zip'                                     #Имя фалйа
                my_file = open('System/Database/' + file_name, 'wb')# Директория в котрую будет сохранен файл
                ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)             # Скачивание файла
                my_file.close()                                                # Закрытие директории в которую должен быть скачан файл
                ftp.close()                                                        # Отключение от сервера
                with zipfile.ZipFile('System/Database/' + file_name, 'r') as myzip:
                    os.chdir('System/Database/Blockchain_processing/Blockchain_processing_0')
                    myzip.extractall()

                os.chdir('../../../../')
                os.remove('System/Database/Blockchain.zip')
                ret = 'done'
            except:
                pass
        if ret == 'done':
            return 'done'
        else:
            return 'failed'



    if type == 'block_that_needs_mining':
        ret = 'failed'
        max_block_in_blockchain = max_block('blockchain')
        for i in range(number_servers):
            for z in range(max_block_in_blockchain + 1, 1000000000):
                try:
                    ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
                    ftp.cwd('LEGION/Block_that_needs_mining/')
                    file_name = str(z) + '.txt'  # Имя фалйа
                    my_file = open('System/Database/Block_that_needs_mining_processing/' + file_name, 'wb')  # Директория в котрую будет сохранен файл
                    ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)  # Скачивание файла блоков в папку сервера из которого они загруженны
                    my_file.close()
                    ftp.close()
                    ret = 'done'
                except:
                    my_file.close()
                    os.remove('System/Database/Block_that_needs_mining_processing/' + file_name)
                    break

        #обход проверки блоков которые нужно майнить
        max_block_in_blockchain = max_block('blockchain')
        for i in range(max_block_in_blockchain + 1, 1000000000):
            try:
                shutil.copyfile('System/Database/Block_that_needs_mining_processing/' + str(i) + '.txt', 'System/Block_that_needs_mining/' + str(i) + '.txt')
            except:
                break

        if ret == 'done':
            return 'done'
        else:
            return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def upload(type):
    if type == 'blockchain':
        os.chdir('System/Database/')
        with zipfile.ZipFile('Blockchain.zip', 'w') as myzip:
            os.chdir('../Blockchain/')

            for z in range(1000000000):
                try:
                    myzip.write(str(z) + '.txt')
                except:
                    break
        os.chdir('../../')
        ret = 'failed'
        for i in range(number_servers):
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
                ftp.cwd('LEGION/Blockchain/')
                file_name = 'Blockchain.zip'  # Имя фалйа
                my_file = open('System/Database/' + file_name, 'rb')  # Директория в котрую будет сохранен файл
                ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер  # Скачивание файла                              # Загрузка фала на сервер
                #print('Блок для майнинга', file_name, 'загружен на сервер', host[i])
                my_file.close()
                ftp.close()  # Отключение от сервера
                ret = 'done'
            except:
                pass
                try:
                    ftp.close()  # Отключение от сервера
                except:
                    pass
                #print('SERVER', host[i], 'не работает')
        try:
            os.remove('System/Database/Blockchain.zip')
        except:
            pass


    if type == 'block_that_needs_mining':
        maxx_block = max_block('blockchain')
        ret = 'failed'
        for i in range(number_servers):
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])
                ftp.cwd('LEGION/Block_that_needs_mining/')
            except:
                pass
            for z in range(maxx_block, 1000000000):
                try:
                    file_name = str(z + 1) + '.txt'  # Имя фала
                    my_file = open('System/Block_that_needs_mining/' + file_name, 'rb')  # Директория фала
                    ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер
                    #print('Блок для майнинга', file_name, 'загружен на сервер', host[i])
                    my_file.close()
                    ret = 'done'
                except:
                    #print('SERVER', host[i], 'не работает')
                    # ftp.close()
                    break
            # ftp.close()



    if ret == 'done':
        return 'done'
    else:
        return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def processing(type):
    if type == 'blockchain_processing_0':
        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_0/0.txt', 'System/Database/Blockchain_processing/Blockchain_processing_1/0.txt')
        for i in range(1, 1000000000):
            try:
                block = read_block('blockchain_processing_0', i-1)
                this_hashh = block[10]

                block = read_block('blockchain_processing_0', i)
                block_number = block[0]
                object_type = block[1]
                user_sender = block[2]
                sent_object = block[3]
                user_recipient = block[4]
                data = block[5]
                signature = block[6]
                hash_key = block[7]
                miner_name = block[8]
                previous_hash = block[9]
                this_hash = block[10]

                if this_hash[:5] == '00000':
                    b = bytes(str(block_number) + str(object_type) + str(user_sender) + str(sent_object) + str(user_recipient) + str(data) + str(signature) + str(hash_key) + str(miner_name) + str(previous_hash), encoding='utf-8')
                    block_hash = hashlib.sha256(b).hexdigest()
                    if block_hash == this_hash:
                        if previous_hash == this_hashh:
                            ret = 'done'
                            shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_0/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt')
                        else:
                            break
                    else:
                        break
                else:
                    break
            except:
                break
        if ret == 'done':
            return 'done'
        else:
            return 'failed'



    if type == 'blockchain_processing_1':
        for i in range(1000000000):
            try:
                block = read_block('blockchain_processing_1', i)
                block_number = block[0]
                object_type = block[1]
                user_sender = block[2]
                sent_object = block[3]
                user_recipient = block[4]
                data = block[5]
                signature = block[6]
                hash_key = block[7]
                miner_name = block[8]
                previous_hash = block[9]
                this_hash = block[10]

                if object_type == 'coin' and sent_object == '-':
                    shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt')
                    ret = 'done'
                else:
                    user_sender_balance = balance_info('coin', user_sender)
                    #print(user_sender_balance)
                    if object_type == 'coin':
                        if float(sent_object) > 0.00000000:
                            if user_sender_balance >= float(sent_object):
                                shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt')
                                ret = 'done'
                    else:
                        break
            except:
                #print(i, 'pizdec')
                break
        if ret == 'done':
            return 'done'
        else:
            return 'failed'

    if type == 'blockchain_processing_2':
        for i in range(1000000000):
            try:
                block = read_block('blockchain_processing_2', i)
                user_sender = block[2]
                sent_object = block[3]
                user_recipient = block[4]
                signature = block[6]
                if user_sender == 'block_if_nothing_to_mine' and sent_object == '-' and user_recipient == '-' and signature == '-':
                    shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt')
                    ret = 'done'
                else:
                    match = sign('check', '-', '-', str(i))
                    if match == 'yes':
                        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt')
                        ret = 'done'
                    else:
                        break
            except:
                break
        if ret == 'done':
            return 'done'
        else:
            return 'failed'

    if type == 'blockchain_processing_3':
        max_block_in_blockchain = max_block('blockchain')
        for i in range(max_block_in_blockchain + 1, 1000000000):
            try:
                ret = 'done'
                shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt','System/Blockchain/' + str(i) + '.txt')                
            except:
                break
        if ret == 'done':
            return 'done'
        else:
            return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------










#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def max_block(option):
    if option == 'blockchain':
        block_namee = []
        for i in range(len(os.listdir('System/Blockchain/'))):
            try:
                z = int(os.listdir('System/Blockchain/')[i][:-4])
                block_namee.append(z)
            except:
                print('Чет не так')
        try:
            maxx_block = max(block_namee)
        except:
            maxx_block = -1
        return maxx_block


    if option == 'block_that_needs_mining':
        block_namee = []
        for i in range(len(os.listdir('System/block_that_needs_mining/'))):
            try:
                z = int(os.listdir('System/block_that_needs_mining/')[i][:-4])
                block_namee.append(z)
            except:
                print('Чет не так')
        try:
            maxx_block = max(block_namee)
        except:
            maxx_block = -1
        return maxx_block
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def sign(option, message, key, id):
    if option == 'create':
        try:
            message = message.encode()
            signature = rsa.sign(message, key, 'SHA-1')
            signature = base64.b64encode(signature)
            signature = str(signature)[2:-1]
            return signature
        except:
            return 'failed'

    if option == 'check':
        #print('3')
        block = read_block('blockchain_processing_2', id)
        block_number = block[0]
        object_type = block[1]
        user_sender = block[2]
        sent_object = block[3]
        user_recipient = block[4]
        signature = block[6]
        #print('4')


        message = block_number + object_type + user_sender + sent_object + user_recipient
        sign = signature
        key = user_sender
        key = rsa.PublicKey.load_pkcs1(b'-----BEGIN RSA PUBLIC KEY-----\n' + key.encode('utf8') + b'\n-----END RSA PUBLIC KEY-----')
        #print(key)
        try:
            signature = base64.b64decode(sign)
            message = message.encode()
            answer = rsa.verify(message, signature, key)
            if answer == 'SHA-1':
                return 'yes'
            else:
                return 'failed'
        except:
            #print('asd')
            return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_new_block(type):
    if type == 'block_if_nothing_to_mine':
        max_block_in_blockchain = max_block('blockchain')
        max_block_in_block_that_needs_mining = max_block('block_that_needs_mining')
        #print(max_block_in_blockchain)
        #print(max_block_in_block_that_needs_mining)
        if max_block_in_block_that_needs_mining >= max_block_in_blockchain:
            block_num = max_block_in_block_that_needs_mining + 1
        else:
            block_num = max_block_in_blockchain + 1

        block_info = [str(block_num), 'coin', 'block_if_nothing_to_mine', '-', '-', '-', '-', '-', '-', '-', '-']
        create_block('block_that_needs_mining', block_info)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def read_block(type, block_id):
    block_info = []
    if type == 'block_that_needs_mining':
        file = open('System/Block_that_needs_mining/' + str(block_id) + '.txt', 'r')
        block = file.readlines()
        file.close()
        block_number = block[0][14:-1]
        object_type = block[1][13:-1]
        user_sender = block[2][13:-1]
        sent_object = block[3][13:-1]
        user_recipient = block[4][16:-1]
        data = block[5][6:-1]
        signature = block[6][11:-1]
        hash_key = block[7][10:-1]
        miner_name = block[8][12:-1]
        previous_hash = block[9][15:-1]
        this_hash = block[10][11:]
        file.close()
        block_info = [block_number, object_type, user_sender, sent_object, user_recipient, data, signature, hash_key, miner_name, previous_hash, this_hash]

    if type == 'blockchain':
        file = open('System/Blockchain/' + str(block_id) + '.txt', 'r')
        block = file.readlines()
        file.close()
        block_number = block[0][14:-1]
        object_type = block[1][13:-1]
        user_sender = block[2][13:-1]
        sent_object = block[3][13:-1]
        user_recipient = block[4][16:-1]
        data = block[5][6:-1]
        signature = block[6][11:-1]
        hash_key = block[7][10:-1]
        miner_name = block[8][12:-1]
        previous_hash = block[9][15:-1]
        this_hash = block[10][11:]
        file.close()
        block_info = [block_number, object_type, user_sender, sent_object, user_recipient, data, signature, hash_key, miner_name, previous_hash, this_hash]

    if type == 'blockchain_processing_0':
        file = open('System/Database/Blockchain_processing/Blockchain_processing_0/' + str(block_id) + '.txt', 'r')
        block = file.readlines()
        file.close()
        block_number = block[0][14:-1]
        object_type = block[1][13:-1]
        user_sender = block[2][13:-1]
        sent_object = block[3][13:-1]
        user_recipient = block[4][16:-1]
        data = block[5][6:-1]
        signature = block[6][11:-1]
        hash_key = block[7][10:-1]
        miner_name = block[8][12:-1]
        previous_hash = block[9][15:-1]
        this_hash = block[10][11:]
        file.close()
        block_info = [block_number, object_type, user_sender, sent_object, user_recipient, data, signature, hash_key, miner_name, previous_hash, this_hash]

    if type == 'blockchain_processing_1':
        file = open('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(block_id) + '.txt', 'r')
        block = file.readlines()
        file.close()
        block_number = block[0][14:-1]
        object_type = block[1][13:-1]
        user_sender = block[2][13:-1]
        sent_object = block[3][13:-1]
        user_recipient = block[4][16:-1]
        data = block[5][6:-1]
        signature = block[6][11:-1]
        hash_key = block[7][10:-1]
        miner_name = block[8][12:-1]
        previous_hash = block[9][15:-1]
        this_hash = block[10][11:]
        file.close()
        block_info = [block_number, object_type, user_sender, sent_object, user_recipient, data, signature, hash_key, miner_name, previous_hash, this_hash]

    if type == 'blockchain_processing_2':
        file = open('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(block_id) + '.txt', 'r')
        block = file.readlines()
        file.close()
        block_number = block[0][14:-1]
        object_type = block[1][13:-1]
        user_sender = block[2][13:-1]
        sent_object = block[3][13:-1]
        user_recipient = block[4][16:-1]
        data = block[5][6:-1]
        signature = block[6][11:-1]
        hash_key = block[7][10:-1]
        miner_name = block[8][12:-1]
        previous_hash = block[9][15:-1]
        this_hash = block[10][11:]
        file.close()
        block_info = [block_number, object_type, user_sender, sent_object, user_recipient, data, signature, hash_key, miner_name, previous_hash, this_hash]



    return block_info
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_block(type, block_info):
    if type == 'block_that_needs_mining':
        f = open('System/Block_that_needs_mining/' + str(block_info[0]) + '.txt', 'w')
        f.writelines('block_number: ' + block_info[0] + '\n')
        f.writelines('object_type: ' + block_info[1] + '\n')
        f.writelines('user_sender: ' + block_info[2] + '\n')
        f.writelines('sent_object: ' + block_info[3] + '\n')
        f.writelines('user_recipient: ' + block_info[4] + '\n')
        f.writelines('data: ' + block_info[5] + '\n')
        f.writelines('signature: ' + block_info[6] + '\n')
        f.writelines('hash_key: ' + block_info[7] + '\n')
        f.writelines('miner_name: ' + block_info[8] + '\n')
        f.writelines('previous_hash: ' + block_info[9] + '\n')
        f.writelines('this_hash: ' + block_info[10])
        f.close()

    if type == 'blockchain':
        f = open('System/blockchain/' + str(block_info[0]) + '.txt', 'w')
        f.writelines('block_number: ' + block_info[0] + '\n')
        f.writelines('object_type: ' + block_info[1] + '\n')
        f.writelines('user_sender: ' + block_info[2] + '\n')
        f.writelines('sent_object: ' + block_info[3] + '\n')
        f.writelines('user_recipient: ' + block_info[4] + '\n')
        f.writelines('data: ' + block_info[5] + '\n')
        f.writelines('signature: ' + block_info[6] + '\n')
        f.writelines('hash_key: ' + block_info[7] + '\n')
        f.writelines('miner_name: ' + block_info[8] + '\n')
        f.writelines('previous_hash: ' + block_info[9] + '\n')
        f.writelines('this_hash: ' + block_info[10])
        f.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





def delete(type, block_number):
    if type == 'block_that_needs_mining':
        ret = 'failed'
        for i in range(number_servers):
            try:
                ftp = ftplib.FTP(host[i], user[i], password[i])
                ftp.cwd('LEGION/Block_that_needs_mining/')
                file_name = str(block_number) + '.txt' # Имя фала
                ftp.delete(file_name)
                ftp.close()
                ret = 'done'
            except:
                print('Чет пошло не так')
        os.remove('System/Block_that_needs_mining/' + str(block_number) + '.txt')


    if ret == 'done':
        return 'done'
    else:
        return 'failed'


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mining():
    max_block_in_blockchain = max_block('blockchain')
    try:
        file = open('System/Block_that_needs_mining/' + str(max_block_in_blockchain + 1) + '.txt', 'r')
        block = file.readlines()
        file.close()
    except:
        create_new_block('block_if_nothing_to_mine')
        upload('block_that_needs_mining')


    block = read_block('block_that_needs_mining', max_block_in_blockchain + 1)
    block_number = block[0]
    object_type = block[1]
    user_sender = block[2]
    sent_object = block[3]
    user_recipient = block[4]
    data = block[5]
    signature = block[6]
    hash_key = block[7]

    if max_block_in_blockchain != -1:
        file = open('System/Blockchain/' + str(max_block_in_blockchain) + '.txt', 'r')
        block = file.readlines()
        file.close()
        previous_hash = block[10][11:]
        #file.close()
    else:
        previous_hash = '0'

    miner_name = wallet_address
    print(miner_name)

    b = bytes(str(block_number) + str(object_type) + str(user_sender) + str(sent_object) + str(user_recipient) + str(data) + str(signature) + str(hash_key) + str(miner_name) + str(previous_hash), encoding='utf-8')
    this_hash = hashlib.sha256(b).hexdigest()
    while this_hash[:5] != '00000':
        hash_key = random.randint(0, 1000000000)
        b = bytes(str(block_number) + str(object_type) + str(user_sender) + str(sent_object) + str(user_recipient) + str(data) + str(signature) + str(hash_key) + str(miner_name) + str(previous_hash), encoding='utf-8')
        this_hash = hashlib.sha256(b).hexdigest()


    block_info = [str(max_block_in_blockchain + 1), object_type, user_sender, sent_object, user_recipient, data, signature, str(hash_key), miner_name, previous_hash, this_hash]
    create_block('blockchain', block_info)


    delete('block_that_needs_mining', max_block_in_blockchain + 1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def send_coin(object, recipient):
    max_block_in_block_that_needs_mining = max_block('block_that_needs_mining')
    max_block_in_blockchain = max_block('blockchain')
    if max_block_in_block_that_needs_mining >= max_block_in_blockchain:
        signature = sign('create', str(max_block_in_block_that_needs_mining + 1) + 'coin' + wallet_address + str(object) + recipient, privateKey, '-')
        block_info = [str(max_block_in_block_that_needs_mining + 1), 'coin', wallet_address, object, recipient, '-', signature, '-', '-', '-', '-']
        create_block('block_that_needs_mining', block_info)
    else:
        signature = sign('create', str(max_block_in_blockchain + 1) + 'coin' + wallet_address + str(object) + recipient, privateKey, '-')
        block_info = [str(max_block_in_blockchain + 1), 'coin', wallet_address, object, recipient, '-', signature, '-', '-', '-', '-']
        create_block('block_that_needs_mining', block_info)



#wallet('keys_init')
#a = balance_info('coin', wallet_address)
#print(a)
#time.sleep(5)
#wallet('keys_init')
#send_coin('0.000097', wallet_address)
#a = balance_info('coin', wallet_address)
#print(a)

a = server_init()
print('ForceNET - server_init() ----',a);

z = folder_init('client')
print('ForceNET - folder_init(client) ----',z);

z = wallet('create_keys')
print('ForceNET - wallet(create_keys) ----',z);

if a == 'failed':
    print('You need update the ForceNET system')
    time.sleep(1000)

z = folder_init('server')
print('ForceNET - folder_init(server) ----',z);

z = wallet('keys_init')
print('ForceNET - wallet(keys_init) ----',z);

z = download('blockchain')
print('ForceNET - download(blockchain) ----',z);


processing('blockchain_processing_0')
processing('blockchain_processing_1')
processing('blockchain_processing_2')
processing('blockchain_processing_3')

z = download('block_that_needs_mining')
print('ForceNET - download(block_that_needs_mining) ----',z);

z = upload('blockchain')
print('ForceNET - upload(blockchain) ----',z);

z = upload('block_that_needs_mining')
print('ForceNET - upload(block_that_needs_mining) ----',z);


print(' ')
wallet('keys_init')
a = balance_info('coin', wallet_address)
print(a)


#time.sleep(1000)

mining()
upload('blockchain')
upload('block_that_needs_mining')














