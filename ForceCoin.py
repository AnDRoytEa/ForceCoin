def window_1000_600():
    import pygame
    from pygame import gfxdraw
    from ctypes import windll
    import time

    pygame.init()
    screen = pygame.display.set_mode((1000, 600), pygame.NOFRAME)
    pygame.display.set_caption("LEGION")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 20)
    font = pygame.font.Font("Fonts/Buk.ttf", 30)
    legion = font.render("LEGION", True, [255, 55, 55])

    font = pygame.font.Font(None, 20)
    font = pygame.font.Font("Fonts/Buk.ttf", 30)
    tool_bar_open = font.render("-", True, [255, 55, 55])

    font = pygame.font.Font(None, 20)
    font = pygame.font.Font("Fonts/Buk.ttf", 40)
    settings_open = font.render("*", True, [255, 55, 55])

    font = pygame.font.Font(None, 20)
    font = pygame.font.Font("Fonts/Buk.ttf", 30)
    sender_open = font.render("S", True, [255, 55, 55])


    tool_bar_menu_stats = 'no'
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 960 and pygame.mouse.get_pos()[1] >= 0:
                    if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 40:
                        if tool_bar_menu_stats == 'yes':
                            print('2')
                            screen = pygame.display.set_mode((1000, 600), pygame.NOFRAME)
                            tool_bar_menu_stats = 'no'
                        else:
                            screen = pygame.display.set_mode((1000, 600))
                            tool_bar_menu_stats = 'yes'





            if pygame.mouse.get_pos()[0] >= 960 and pygame.mouse.get_pos()[1] >= 0:
                if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 40:
                    tool_bar_open_color = (45, 45, 45, 250)
                else:
                    tool_bar_open_color = (35, 35, 35, 250)
            else:
                tool_bar_open_color = (35, 35, 35, 250)




            if pygame.mouse.get_pos()[0] >= 920 and pygame.mouse.get_pos()[1] >= 0:
                if pygame.mouse.get_pos()[0] <= 960 and pygame.mouse.get_pos()[1] <= 40:
                    settings_color = (45, 45, 45, 250)
                else:
                    settings_color = (35, 35, 35, 250)
            else:
                settings_color = (35, 35, 35, 250)


            if pygame.mouse.get_pos()[0] >= 880 and pygame.mouse.get_pos()[1] >= 0:
                if pygame.mouse.get_pos()[0] <= 920 and pygame.mouse.get_pos()[1] <= 40:
                    sender_color = (45, 45, 45, 250)
                else:
                    sender_color = (35, 35, 35, 250)
            else:
                sender_color = (35, 35, 35, 250)




        screen.fill((22, 22, 22))

        pygame.gfxdraw.box(screen, pygame.Rect(0, 0, 1000, 40), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(0, 0, 5, 1000), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(0, 595, 1000, 600), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(995, 0, 1000, 600), (35, 35, 35, 255))

        screen.blit(legion, (42, 2))


        pygame.gfxdraw.box(screen, pygame.Rect(880, 0, 920, 40), sender_color)
        screen.blit(sender_open, (895, 2))

        pygame.gfxdraw.box(screen, pygame.Rect(920, 0, 960, 40), settings_color)
        screen.blit(settings_open, (932, 2))

        pygame.gfxdraw.box(screen, pygame.Rect(960, 0, 1000, 40), tool_bar_open_color)
        screen.blit(tool_bar_open, (973, 0))



        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)


def main_window_1000_600():
    from System.Source import ForceNET as FNET
    import pygame
    from pygame import gfxdraw
    from ctypes import windll
    import time

    pygame.init()
    screen = pygame.display.set_mode((1000, 600), pygame.NOFRAME)
    pygame.display.set_caption("ForceCoin")
    clock = pygame.time.Clock()

    coin = ''
    recipient = ''

    send_coin = 'no'
    tool_bar_menu_stats = 'no'
    run = True
    a = FNET.last_transactions()
    while run:




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            # ---------------------------------------------------------- нажатие на кнопку тулбара
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 960 and pygame.mouse.get_pos()[1] >= 0:
                    if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 40:
                        if tool_bar_menu_stats == 'yes':
                            screen = pygame.display.set_mode((1000, 600), pygame.NOFRAME)
                            tool_bar_menu_stats = 'no'
                        else:
                            screen = pygame.display.set_mode((1000, 600))
                            tool_bar_menu_stats = 'yes'
            # ---------------------------------------------------------- наведение на кнопку тулбара
            if pygame.mouse.get_pos()[0] >= 960 and pygame.mouse.get_pos()[1] >= 0:
                if pygame.mouse.get_pos()[0] <= 1000 and pygame.mouse.get_pos()[1] <= 40:
                    tool_bar_open_color = (45, 45, 45, 250)
                else:
                    tool_bar_open_color = (35, 35, 35, 250)
            else:
                tool_bar_open_color = (35, 35, 35, 250)
            # ---------------------------------------------------------- нажатие на кнопку тулбара








            # ---------------------------------------------------------- наведение на звездочку
            if pygame.mouse.get_pos()[0] >= 920 and pygame.mouse.get_pos()[1] >= 0:
                if pygame.mouse.get_pos()[0] <= 960 and pygame.mouse.get_pos()[1] <= 40:
                    settings_color = (45, 45, 45, 250)
                else:
                    settings_color = (35, 35, 35, 250)
            else:
                settings_color = (35, 35, 35, 250)
            # ---------------------------------------------------------- наведение на звездочку











        screen.fill((22, 22, 22))

        pygame.gfxdraw.box(screen, pygame.Rect(0, 0, 1000, 40), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(0, 0, 5, 1000), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(0, 595, 1000, 600), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(995, 0, 1000, 600), (35, 35, 35, 255))

        font = pygame.font.Font("Fonts/Buk.ttf", 30)
        legion = font.render("ForceCoin", True, [55, 30, 255])
        screen.blit(legion, (40, 0))


        pygame.gfxdraw.box(screen, pygame.Rect(960, 0, 40, 40), tool_bar_open_color)
        pygame.gfxdraw.box(screen, pygame.Rect(920, 0, 40, 40), settings_color)

        font = pygame.font.Font("Fonts/Buk.ttf", 30)
        tool_bar_open = font.render("-", True, [55, 30, 255])
        screen.blit(tool_bar_open, (973, 0))

        font = pygame.font.Font("Fonts/Buk.ttf", 40)
        settings_open = font.render("*", True, [55, 30, 255])
        screen.blit(settings_open, (932, 0))






        pygame.gfxdraw.box(screen, pygame.Rect(15, 50, 660, 200), (35, 35, 35, 255))   # поле где показывается балланс
        font = pygame.font.Font("Fonts/Buk.ttf", 80)
        balance = font.render(str(FNET.coin_balance_info()), True, [255, 255, 255])
        screen.blit(balance, (50, 90))
        font = pygame.font.Font("Fonts/Buk.ttf", 30)
        settings_open = font.render("ForceCoin", True, [200, 200, 200])
        screen.blit(settings_open, (453, 143))



        # ---------------------------------------------------------- нажатие на кнопку отправить монеты
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 15 and pygame.mouse.get_pos()[1] >= 310:
                if pygame.mouse.get_pos()[0] <= 195 and pygame.mouse.get_pos()[1] <= 360:
                    if send_coin == 'yes':
                        send_coin = 'no'
                        time.sleep(0.1)
                    else:
                        send_coin = 'yes'
                        time.sleep(0.1)
        # ---------------------------------------------------------- наведение на кнопку отправить монеты
        if pygame.mouse.get_pos()[0] >= 15 and pygame.mouse.get_pos()[1] >= 310:
            if pygame.mouse.get_pos()[0] <= 195 and pygame.mouse.get_pos()[1] <= 360:
                button_color = (45, 45, 45, 250)
            else:
                button_color = (35, 35, 35, 250)
        else:
            button_color = (35, 35, 35, 250)
        # ---------------------------------------------------------- наведение на кнопку отправить монеты
        if send_coin == 'yes':
            pygame.gfxdraw.box(screen, pygame.Rect(15, 310, 180, 50), button_color)  # кнопка отправить монет
            font = pygame.font.Font("Fonts/Buk.ttf", 30)
            send_coin_button = font.render("Close form", True, [55, 30, 255])
            screen.blit(send_coin_button, (25, 313))

            pygame.gfxdraw.box(screen, pygame.Rect(15, 370, 660, 190), (35, 35, 35, 250))  # Поле для ввода информации


            font = pygame.font.Font("Fonts/Buk.ttf", 30)
            send_coin_button = font.render("Enter resipient id:", True, [255, 255, 255])
            screen.blit(send_coin_button, (25, 390))
            pygame.gfxdraw.box(screen, pygame.Rect(300, 395, 100, 30), (45, 45, 45, 250))  # Поле для ввода id получателя

            send_coin_button = font.render(recipient, True, [255, 255, 255])
            screen.blit(send_coin_button, (320, 390))
            # ---------------------------------------------------------- наведение на поле для для ввода id получателя
            if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 395:
                if pygame.mouse.get_pos()[0] <= 400 and pygame.mouse.get_pos()[1] <= 425:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            recipient = recipient + event.unicode
                            #print(event.key)
                else:
                    pass
            else:
                pass
            # ---------------------------------------------------------- наведение на поле для ввода id получателя




            font = pygame.font.Font("Fonts/Buk.ttf", 30)
            send_coin_button = font.render("Count of coin:", True, [255, 255, 255])
            screen.blit(send_coin_button, (25, 430))
            pygame.gfxdraw.box(screen, pygame.Rect(240, 435, 200, 30), (45, 45, 45, 250))  # Поле для ввода количества монет

            send_coin_button = font.render(coin, True, [255, 255, 255])
            screen.blit(send_coin_button, (260, 430))
            # ---------------------------------------------------------- наведение на поле для ввода количества монет
            if pygame.mouse.get_pos()[0] >= 240 and pygame.mouse.get_pos()[1] >= 435:
                if pygame.mouse.get_pos()[0] <= 440 and pygame.mouse.get_pos()[1] <= 465:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            coin = coin + event.unicode
                            #print(event.key)
                else:
                    pass
            else:
                pass
            # ---------------------------------------------------------- наведение на поле для ввода количества монет







            # ---------------------------------------------------------- нажатие на кнопку подтвердить
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 15 and pygame.mouse.get_pos()[1] >= 500:
                    if pygame.mouse.get_pos()[0] <= 195 and pygame.mouse.get_pos()[1] <= 550:
                        recipient = FNET.address_by_id(int(recipient))
                        a = FNET.send_coin(coin, recipient)
                        z = FNET.upload('blockchain')
                        print('    ForceNET - upload(blockchain) ----', z)
                        z = FNET.upload('block_that_needs_mining')
                        print('    ForceNET - upload(block_that_needs_mining) ----', z)
                        print('')
            # ---------------------------------------------------------- наведение на кнопку подтвердить
            if pygame.mouse.get_pos()[0] >= 25 and pygame.mouse.get_pos()[1] >= 500:
                if pygame.mouse.get_pos()[0] <= 205 and pygame.mouse.get_pos()[1] <= 550:
                    confirm_color = (65, 65, 65, 250)
                else:
                    confirm_color = (45, 45, 45, 250)
            else:
                confirm_color = (45, 45, 45, 250)
            # ---------------------------------------------------------- наведение на кнопку подтвердить
            pygame.gfxdraw.box(screen, pygame.Rect(25, 500, 180, 50), confirm_color)  # кнопка отправить монет
            font = pygame.font.Font("Fonts/Buk.ttf", 30)
            send_coin_button = font.render("Confirm", True, [55, 30, 255])
            screen.blit(send_coin_button, (55, 503))




        else:
            coin = ''
            recipient = ''
            pygame.gfxdraw.box(screen, pygame.Rect(15, 310, 180, 50), button_color)  # кнопка отправить монет
            font = pygame.font.Font("Fonts/Buk.ttf", 30)
            send_coin_button = font.render("Send Coin", True, [55, 30, 255])
            screen.blit(send_coin_button, (40, 313))




        pygame.gfxdraw.box(screen, pygame.Rect(15, 260, 660, 40), (35, 35, 35, 255))  # поле где показывается инфа об аккаунте
        font = pygame.font.Font("Fonts/Buk.ttf", 20)
        account_info = font.render("Your account id: " + str(FNET.account_id(FNET.wallet_address)), True, [200, 200, 200])
        screen.blit(account_info, (30, 265))

        pygame.gfxdraw.box(screen, pygame.Rect(685, 50, 300, 535), (35, 35, 35, 255))  # поле где показывается последние транзакции
        font = pygame.font.Font("Fonts/Buk.ttf", 30)
        transactions = font.render("Transactions", True, [250, 250, 250])
        screen.blit(transactions, (750, 65))

        i = 70
        number = 0
        while i < 500:
            i = i + 55
            pygame.gfxdraw.box(screen, pygame.Rect(685, i, 300, 50), (30, 30, 30, 255))  # транзакция 1
            font = pygame.font.Font("Fonts/Buk.ttf", 17)

            try:
                if a[number][:2] == 'To':
                    settings_open = font.render("<", True, [250, 25, 25])
                else:
                    settings_open = font.render(">", True, [25, 250, 25])
                screen.blit(settings_open, (700, i + 4))
                settings_open = font.render(a[number], True, [250, 250, 250])
                screen.blit(settings_open, (720, i + 4))
                settings_open = font.render(a[number + 1], True, [250, 250, 250])
                screen.blit(settings_open, (720, i + 24))
                number = number + 2
            except:
                pass


        font = pygame.font.Font("Fonts/Buk.ttf", 20)
        settings_open = font.render("Copyright All rights reserved | This template is made with by LEGION", True, [110, 110, 110])
        screen.blit(settings_open, (15, 562))








        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)






def window_loading_300_100():
    import pygame
    from pygame import gfxdraw
    from ctypes import windll
    import time
    pygame.init()
    screen = pygame.display.set_mode((300, 100), pygame.NOFRAME)
    pygame.display.set_caption("ForceCoin")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 20)
    font = pygame.font.Font("Fonts/Buk.ttf", 30)

    fontt = pygame.font.Font(None, 20)
    fontt = pygame.font.Font("Fonts/Buk.ttf", 20)

    i = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        i = i + 1
        if i == 360:
            time.sleep(0.5)
            pygame.quit()
            run = False
            thread2.join()
            main_window_1000_600()



        screen.fill((22, 22, 22))

        #red = (255, 30, 30)
        red = (55, 30, 255)
        light_black = (35, 35, 35)
        black = (22, 22, 22)
        gray = (70, 70, 70)
        white = (200, 200, 200)

        #pygame.gfxdraw.aacircle(screen, 3, 3, 200, black)
        #pygame.gfxdraw.filled_circle(screen, 3, 3, 200, black)

        pygame.gfxdraw.pie(screen, 50, 60, 28, i, i * 2, red)
        pygame.gfxdraw.pie(screen, 50, 60, 27, i+1, i * 2, red)
        pygame.gfxdraw.pie(screen, 50, 60, 26, i+2, i * 2, red)
        pygame.gfxdraw.filled_circle(screen, 50, 60, 20, light_black)


        loading = font.render("Loading", True, red)
        screen.blit(loading, (105, 40))

        persent = font.render(str(i // 3.6), True, red)
        screen.blit(persent, (215, 40))


        pygame.gfxdraw.box(screen, pygame.Rect(0, 0, 300, 25), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(0, 0, 5, 100), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(0, 95, 300, 5), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(295, 0, 5, 100), (35, 35, 35, 255))

        legion = fontt.render("LEGION", True, red)
        screen.blit(legion, (10, -2))






        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

def forcecoin_loading():
    from System.Source import ForceNET as FNET
    import time
    import colorama
    from colorama import Fore, Back, Style

    colorama.init()
    a = FNET.server_init()
    if a == 'done':
        print('ForceNET - server_init() ----', Style.BRIGHT + Fore.GREEN + a + Style.RESET_ALL)
    else:
        print('ForceNET  - server_init() ----', Style.BRIGHT + Fore.RED + a + Style.RESET_ALL)

        print('You need update the ForceNET system')
        time.sleep(10000)

    z = FNET.client_folder_init()
    if z == 'done':
        print('ForceNET - folder_init(client) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
    else:
        print('ForceNET - folder_init(client) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)

    z = FNET.create_wallet()
    if z == 'done':
        print('ForceNET - wallet(create) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
    else:
        print('ForceNET - wallet(create) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)

    z = FNET.server_folder_init()
    if z == 'done':
        print('ForceNET - folder_init(server) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
    else:
        print('ForceNET - folder_init(server) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)

    z = FNET.wallet_init()
    if z == 'done':
        print('ForceNET - wallet(init) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
    else:
        print('ForceNET - wallet(init) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)

    z = FNET.download('blockchain')
    if z == 'done':
        print('ForceNET - download(blockchain) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
    else:
        print('ForceNET - download(blockchain) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)

    a = FNET.processing('blockchain_processing_0')
    print('ForceNET - blockchain_processing_0 ----', Style.BRIGHT + Fore.GREEN + str(a) + Style.RESET_ALL)

    b = FNET.processing('blockchain_processing_1')
    if a != b:
        print('ForceNET - blockchain_processing_1 ----', Style.BRIGHT + Fore.RED + str(a) + Style.RESET_ALL)
    else:
        print('ForceNET - blockchain_processing_1 ----', Style.BRIGHT + Fore.GREEN + str(a) + Style.RESET_ALL)

    c = FNET.processing('blockchain_processing_2')
    if b != c:
        print('ForceNET - blockchain_processing_2 ----', Style.BRIGHT + Fore.RED + str(a) + Style.RESET_ALL)
    else:
        print('ForceNET - blockchain_processing_2 ----', Style.BRIGHT + Fore.GREEN + str(a) + Style.RESET_ALL)

    d = FNET.processing('blockchain_processing_3')
    if c != d:
        print('ForceNET - blockchain_processing_3 ----', Style.BRIGHT + Fore.RED + str(a) + Style.RESET_ALL)
    else:
        print('ForceNET - blockchain_processing_3 ----', Style.BRIGHT + Fore.GREEN + str(a) + Style.RESET_ALL)

    z = FNET.download('block_that_needs_mining')
    if z == 'done':
        print('ForceNET - download(block_that_needs_mining) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
    else:
        print('ForceNET - download(block_that_needs_mining) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)

    z = FNET.upload('blockchain')
    if z == 'done':
        print('ForceNET - upload(blockchain) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
    else:
        print('ForceNET - upload(blockchain) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)

    z = FNET.upload('block_that_needs_mining')
    if z == 'done':
        print('ForceNET - upload(block_that_needs_mining) ----', Style.BRIGHT + Fore.GREEN + z + Style.RESET_ALL)
    else:
        print('ForceNET - upload(block_that_needs_mining) ----', Style.BRIGHT + Fore.RED + z + Style.RESET_ALL)

    print('крч все супер')

from threading import Thread
#, args=(100,)
thread1 = Thread(target=window_loading_300_100)
thread2 = Thread(target=forcecoin_loading)
thread1.start()
thread2.start()




#main_window_1000_600()
#window_loading_300_100()
























