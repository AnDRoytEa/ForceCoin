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

    if ret == 'done':
        return 'done'
    else:
        return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def server_folder_init():
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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def client_folder_init():
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
    if ret == 'done':
        return 'done'
    else:
        return 'failed'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_wallet():
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
def wallet_init():
    global wallet_address, publicKey, privateKey
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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def coin_balance_info():
    balance = 0.00000000
    try:
        for i in range(1000000000):
            block = read_block('blockchain', i)
            object_type = block[1]
            user_sender = block[2]
            sent_object = block[3]
            user_recipient = block[4]
            miner_name = block[8]
            if miner_name == wallet_address:
                balance = balance + 0.00030700
            if object_type == 'coin' and user_recipient == wallet_address:
                balance = balance + float(sent_object)
            if object_type == 'coin' and user_sender == wallet_address:
                balance = balance - float(sent_object)
    except:
        pass
    balance = format(balance, '.8f')
    return balance
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def NFT_balance_info():
    balance = []
    try:
        for i in range(1000000000):
            block = read_block('blockchain', i)
            object_type = block[1]
            user_sender = block[2]
            sent_object = block[3]
            user_recipient = block[4]

            if object_type == 'NFT' and user_recipient == wallet_address and user_sender == wallet_address:
                balance.append(sent_object)
            if object_type == 'NFT' and user_recipient == wallet_address and user_sender != wallet_address:
                balance.append(sent_object)
            if object_type == 'NFT' and user_sender == wallet_address and user_recipient != wallet_address:
                balance.remove(sent_object)
    except:
        pass
    return balance
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





def processing_coin_balance_info(block_id, wallet):
    balance = 0.00000000
    try:
        f = open('System/Database/Wallet_keys/public_key.txt', 'r')  # Чтение файла кошелька
        f.close()
    except:
        return 'failed'
    try:
        for i in range(block_id):
            block = read_block('blockchain_processing_1', i)
            object_type = block[1]
            user_sender = block[2]
            sent_object = block[3]
            user_recipient = block[4]
            miner_name = block[8]
            if miner_name == wallet:
                balance = balance + 0.00030700
            if object_type == 'coin' and user_recipient == wallet:
                balance = balance + float(sent_object)
            if object_type == 'coin' and user_sender == wallet:
                balance = balance - float(sent_object)
    except:
        pass
    return balance

def processing_NFT_balance_info(block_id, wallet):
    balance = []
    try:
        for i in range(block_id):
            block = read_block('blockchain_processing_1', i)
            object_type = block[1]
            user_sender = block[2]
            sent_object = block[3]
            user_recipient = block[4]

            if object_type == 'NFT' and user_recipient == wallet and user_sender == wallet:
                balance.append(sent_object)
            if object_type == 'NFT' and user_recipient == wallet and user_sender != wallet:
                balance.append(sent_object)
            if object_type == 'NFT' and user_sender == wallet and user_recipient != wallet:
                balance.remove(sent_object)
    except:
        pass
    return balance





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
        try:
            shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_0/0.txt', 'System/Database/Blockchain_processing/Blockchain_processing_1/0.txt')
        except:
            pass
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
                            shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_0/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt')
                        else:
                            break
                    else:
                        break
                else:
                    break
            except:
                break
        return i-1



    if type == 'blockchain_processing_1':
        for i in range(1000000000):
            try:
                block = read_block('blockchain_processing_1', i)
                object_type = block[1]
                user_sender = block[2]
                sent_object = block[3]
                user_recipient = block[4]

                if object_type == 'coin':
                    if sent_object == '-':
                        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt')
                    else:
                        user_sender_balance = processing_coin_balance_info(i, user_sender)
                        if float(sent_object) > 0.00000000:
                            if user_sender_balance >= float(sent_object):
                                shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt')
                        else:
                            break

                if object_type == 'NFT':
                    user_sender_NFT = processing_NFT_balance_info(i, user_sender)
                    if user_sender == user_recipient:
                        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt')
                    if sent_object in user_sender_NFT:
                        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt')

            except:
                break
        return i-1



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
                else:
                    match = check_sign(str(i))
                    if match == 'yes':
                        shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_2/' + str(i) + '.txt', 'System/Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt')
                    else:
                        break
            except:
                break
        return i-1

    if type == 'blockchain_processing_3':
        max_block_in_blockchain = max_block('blockchain')
        for i in range(max_block_in_blockchain + 1, 1000000000):
            try:
                shutil.copyfile('System/Database/Blockchain_processing/Blockchain_processing_3/' + str(i) + '.txt','System/Blockchain/' + str(i) + '.txt')                
            except:
                break
        return i-1
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



def create_sign(message):
    try:
        message = message.encode()
        signature = rsa.sign(message, privateKey, 'SHA-1')
        signature = base64.b64encode(signature)
        signature = str(signature)[2:-1]
        return signature
    except:
        return 'failed'
def check_sign(id):
    block = read_block('blockchain_processing_2', id)
    block_number = block[0]
    object_type = block[1]
    user_sender = block[2]
    sent_object = block[3]
    user_recipient = block[4]
    signature = block[6]

    message = block_number + object_type + user_sender + sent_object + user_recipient
    sign = signature
    key = user_sender
    key = rsa.PublicKey.load_pkcs1(
        b'-----BEGIN RSA PUBLIC KEY-----\n' + key.encode('utf8') + b'\n-----END RSA PUBLIC KEY-----')
    try:
        signature = base64.b64decode(sign)
        message = message.encode()
        answer = rsa.verify(message, signature, key)
        if answer == 'SHA-1':
            return 'yes'
        else:
            return 'failed'
    except:
        return 'failed'


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
def read_block(type, block_id):
    block_info = []
    if type == 'block_that_needs_mining':
        file = open('System/Block_that_needs_mining/' + str(block_id) + '.txt', 'r')
    if type == 'blockchain':
        file = open('System/Blockchain/' + str(block_id) + '.txt', 'r')
    if type == 'blockchain_processing_0':
        file = open('System/Database/Blockchain_processing/Blockchain_processing_0/' + str(block_id) + '.txt', 'r')
    if type == 'blockchain_processing_1':
        file = open('System/Database/Blockchain_processing/Blockchain_processing_1/' + str(block_id) + '.txt', 'r')
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
        # ------------------------------------------------------ Создание блока для майнинга если нечего майнить
        max_block_in_blockchain = max_block('blockchain')
        max_block_in_block_that_needs_mining = max_block('block_that_needs_mining')
        if max_block_in_block_that_needs_mining >= max_block_in_blockchain:
            block_num = max_block_in_block_that_needs_mining + 1
        else:
            block_num = max_block_in_blockchain + 1
        block_info = [str(block_num), 'coin', 'block_if_nothing_to_mine', '-', '-', '-', '-', '-', '-', '-', '-']
        create_block('block_that_needs_mining', block_info)
        # ------------------------------------------------------ Создание блока для майнинга если нечего майнить
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
    print('ForceNET - mining ---- block №' + block_number, 'accepted')

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
    a = coin_balance_info()
    if a > object:
        max_block_in_block_that_needs_mining = max_block('block_that_needs_mining')
        max_block_in_blockchain = max_block('blockchain')

        if max_block_in_block_that_needs_mining >= max_block_in_blockchain:
            block_number = max_block_in_block_that_needs_mining + 1
        else:
            block_number = max_block_in_blockchain + 1
        block_number = str(block_number)

        signature = create_sign(block_number + 'coin' + wallet_address + str(object) + recipient) #################################################################
        block_info = [block_number, 'coin', wallet_address, object, recipient, '-', signature, '-', '-', '-', '-']
        create_block('block_that_needs_mining', block_info)
        return 'done'
    else:
        return 'failed'



def create_new_NFT(file_name):
    try:
        f = open('System/Database/NFT/' + file_name, 'r')
    except:
        return 'failed'

    for i in range(number_servers):
        try:
            ftp = ftplib.FTP(host[i], user[i], password[i])  # Конект к серверу
            ftp.cwd('LEGION/NFT/')
            my_file = open('System/Database/NFT/' + file_name, 'rb')  # Директория в котрую будет сохранен файл
            ftp.storbinary('STOR ' + file_name, my_file)  # Загрузка фала на сервер  # Скачивание файла                              # Загрузка фала на сервер
            my_file.close()
            ftp.close()  # Отключение от сервера
        except:
            break
            return 'failed'


    max_block_in_block_that_needs_mining = max_block('block_that_needs_mining')
    max_block_in_blockchain = max_block('blockchain')

    if max_block_in_block_that_needs_mining >= max_block_in_blockchain:
        block_number = max_block_in_block_that_needs_mining + 1
    else:
        block_number = max_block_in_blockchain + 1
    block_number = str(block_number)

    signature = sign('create', block_number + 'NFT' + wallet_address + file_name + wallet_address, privateKey, '-')
    block_info = [block_number, 'NFT', wallet_address, file_name, wallet_address, '-', signature, '-', '-', '-', '-']
    create_block('block_that_needs_mining', block_info)

    os.remove('System/Database/NFT/' + file_name)


    return 'done'
def send_NFT(object, recipient):
    a = NFT_balance_info()
    if object in a:
        max_block_in_block_that_needs_mining = max_block('block_that_needs_mining')
        max_block_in_blockchain = max_block('blockchain')

        if max_block_in_block_that_needs_mining >= max_block_in_blockchain:
            block_number = max_block_in_block_that_needs_mining + 1
        else:
            block_number = max_block_in_blockchain + 1
        block_number = str(block_number)

        signature = sign('create', block_number + 'NFT' + wallet_address + object + recipient, privateKey, '-')
        block_info = [block_number, 'NFT', wallet_address, object, recipient, '-', signature, '-', '-', '-', '-']
        create_block('block_that_needs_mining', block_info)
        return 'done'
    else:
        return 'failed'





def account_id(address):
    accounts = []
    for i in range(1000000000):
        try:
            file = open('System/Blockchain/' + str(i) + '.txt', 'r')
            block = file.readlines()
            file.close()
            block_number = block[0][14:-1]
            user_sender = block[2][13:-1]
            user_recipient = block[4][16:-1]
            miner_name = block[8][12:-1]
            #print(user_sender)
            if user_sender in accounts:
                pass
            else:
                accounts.append(user_sender)
            if user_recipient in accounts:
                pass
            else:
                accounts.append(user_recipient)
            if miner_name in accounts:
                pass
            else:
                accounts.append(miner_name)
        except:
            try:
                id = accounts.index(address)
            except:
                id = 'your account not activated'
            #print(accounts[2])
            return id
def address_by_id(id):
    accounts = []
    for i in range(1000000000):
        try:
            file = open('System/Blockchain/' + str(i) + '.txt', 'r')
            block = file.readlines()
            file.close()
            block_number = block[0][14:-1]
            user_sender = block[2][13:-1]
            user_recipient = block[4][16:-1]
            miner_name = block[8][12:-1]
            #print(user_sender)
            if user_sender in accounts:
                pass
            else:
                accounts.append(user_sender)
            if user_recipient in accounts:
                pass
            else:
                accounts.append(user_recipient)
            if miner_name in accounts:
                pass
            else:
                accounts.append(miner_name)
        except:
            address = accounts[id]
            return address


def last_transactions():
    transactions = []
    try:
        for i in range(max_block('blockchain'), max_block('blockchain') - 7, -1):
            file = open('System/Blockchain/' + str(i) + '.txt', 'r')

            block = file.readlines()
            file.close()
            block_number = block[0][14:-1]
            object_type = block[1][13:-1]
            user_sender = block[2][13:-1]
            sent_object = block[3][13:-1]
            user_recipient = block[4][16:-1]
            miner_name = block[8][12:-1]

            if object_type == 'coin':
                if wallet_address == user_recipient:
                    transactions.append('From: id_' + str(account_id(user_sender)))
                    transactions.append('coin: ' + sent_object)

                if wallet_address == user_sender:
                    transactions.append('To: id_' + str(account_id(user_recipient)))
                    transactions.append('coin: ' + sent_object)

                if wallet_address == miner_name:
                    transactions.append('From: Mining')
                    transactions.append('coin: 0.00030700')

        return transactions
    except:
        return transactions









print('')
print('|| ForceNET by LEGION has been loaded')
print('|| Protocol ForceNET (0.4)')
print('|| Support object: coin, NFT')
print(' ')






















