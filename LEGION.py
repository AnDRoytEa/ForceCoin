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
    import pygame
    from pygame import gfxdraw
    from ctypes import windll
    import time

    pygame.init()
    screen = pygame.display.set_mode((1000, 600), pygame.NOFRAME)
    pygame.display.set_caption("LEGION")
    clock = pygame.time.Clock()


    font = pygame.font.Font("Fonts/Buk.ttf", 30)
    legion = font.render("LEGION", True, [255, 30, 30])

    font = pygame.font.Font("Fonts/Buk.ttf", 30)
    tool_bar_open = font.render("-", True, [255, 30, 30])

    font = pygame.font.Font("Fonts/Buk.ttf", 40)
    settings_open = font.render("*", True, [255, 30, 30])



    table_status = 'no'
    tool_bar_menu_stats = 'no'
    appstore_status = 'no'
    forcenet_status = 'no'
    run = True



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
                            print('2')
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
        screen.blit(legion, (42, 2))


        pygame.gfxdraw.box(screen, pygame.Rect(960, 0, 40, 40), tool_bar_open_color)
        screen.blit(tool_bar_open, (973, 0))
        font = pygame.font.Font("Fonts/Buk.ttf", 30)
        tool_bar_open = font.render("-", True, [255, 30, 30])

        font = pygame.font.Font("Fonts/Buk.ttf", 40)
        settings_open = font.render("*", True, [255, 30, 30])
        pygame.gfxdraw.box(screen, pygame.Rect(920, 0, 40, 40), settings_color)
        screen.blit(settings_open, (932, 2))



















        if table_status == 'yes':




            # ---------------------------------------------------------- нажатие на закрыть меню
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 75:
                    if pygame.mouse.get_pos()[0] <= 315 and pygame.mouse.get_pos()[1] <= 105:
                        table_status = 'no'

            # ---------------------------------------------------------- наведение на закрыть меню
            if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 75:
                if pygame.mouse.get_pos()[0] <= 315 and pygame.mouse.get_pos()[1] <= 105:
                    table_color = (45, 45, 45, 250)
                else:
                    table_color = (35, 35, 35, 250)
            else:
                table_color = (35, 35, 35, 250)

            pygame.gfxdraw.box(screen, pygame.Rect(300, 75, 15, 30), table_color)  # кнопка чтоб открыть\спрятать полочку для приложений

            font = pygame.font.Font("Fonts/Buk.ttf", 20)
            loading = font.render("<", True, [255, 30, 30])
            screen.blit(loading, (302, 75))
            # ---------------------------------------------------------- нажатие на закрыть меню





            pygame.gfxdraw.box(screen, pygame.Rect(10, 45, 290, 545), (35, 35, 35, 255))  # полочка для приложений
            pygame.gfxdraw.box(screen, pygame.Rect(320, 45, 670, 545), (35, 35, 35, 255))  # главная полочка




            font = pygame.font.Font("Fonts/Buk.ttf", 40)
            Available_apps = font.render("Menu", True, [235, 235, 235])
            screen.blit(Available_apps, (110, 50))





            # ---------------------------------------------------------- открыть магазин приложений
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 130:
                    if pygame.mouse.get_pos()[0] <= 290 and pygame.mouse.get_pos()[1] <= 170:
                        appstore_status = 'yes'
                        forcenet_status = 'no'
            # ---------------------------------------------------------- наведение на открыть магазин приложений
            if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 130:
                if pygame.mouse.get_pos()[0] <= 290 and pygame.mouse.get_pos()[1] <= 170:
                    appstore_color = (45, 45, 45, 250)
                else:
                    appstore_color = (22, 22, 22, 250)
            else:
                appstore_color = (22, 22, 22, 250)

            pygame.gfxdraw.box(screen, pygame.Rect(20, 130, 270, 40), appstore_color)  # приложение 1
            font = pygame.font.Font("Fonts/Buk.ttf", 30)
            AppStore = font.render("App Store", True, [235, 235, 235])
            screen.blit(AppStore, (30, 130))
            # ---------------------------------------------------------- открыть магазин приложений








            # ---------------------------------------------------------- открыть системные приложения
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 180:
                    if pygame.mouse.get_pos()[0] <= 290 and pygame.mouse.get_pos()[1] <= 220:
                        forcenet_status = 'yes'
                        appstore_status = 'no'
            # ---------------------------------------------------------- наведение на системные приложения
            if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 180:
                if pygame.mouse.get_pos()[0] <= 290 and pygame.mouse.get_pos()[1] <= 220:
                    forcenet_color = (45, 45, 45, 250)
                else:
                    forcenet_color = (22, 22, 22, 250)
            else:
                forcenet_color = (22, 22, 22, 250)

            pygame.gfxdraw.box(screen, pygame.Rect(20, 180, 270, 40), forcenet_color)  # приложение 2
            font = pygame.font.Font("Fonts/Buk.ttf", 30)
            ForceNET = font.render("ForceNET", True, [235, 235, 235])
            screen.blit(ForceNET, (30, 180))
            # ---------------------------------------------------------- открыть системные приложения





            if appstore_status == 'yes':
                img = pygame.image.load('Images/1.jpg')
                img = pygame.image.load('Images/1.jpg').convert_alpha()
                img = pygame.transform.scale(img, (170, 200))
                screen.blit(img, (350, 135))


            if forcenet_status == 'yes':
                pygame.gfxdraw.box(screen, pygame.Rect(350, 100, 290, 200), (22, 22, 22, 255))  # forcecoin
                pygame.gfxdraw.box(screen, pygame.Rect(670, 100, 290, 200), (22, 22, 22, 255))  # openarts
                pygame.gfxdraw.box(screen, pygame.Rect(350, 330, 290, 200), (22, 22, 22, 255))   # sender



        else:


            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 75:
                    if pygame.mouse.get_pos()[0] <= 45 and pygame.mouse.get_pos()[1] <= 105:
                        table_status = 'yes'


            if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 75:
                if pygame.mouse.get_pos()[0] <= 45 and pygame.mouse.get_pos()[1] <= 105:
                    table_color = (45, 45, 45, 250)
                else:
                    table_color = (35, 35, 35, 250)
            else:
                table_color = (35, 35, 35, 250)


            pygame.gfxdraw.box(screen, pygame.Rect(30, 75, 15, 30), table_color)  # кнопка чтоб открыть\спрятать полочку для приложений
            font = pygame.font.Font("Fonts/Buk.ttf", 18)
            loading = font.render(">", True, [255, 30, 30])
            screen.blit(loading, (32, 77))



            pygame.gfxdraw.box(screen, pygame.Rect(10, 45, 20, 545), (35, 35, 35, 255))  # полочка для приложений
            pygame.gfxdraw.box(screen, pygame.Rect(50, 45, 940, 545), (35, 35, 35, 255))  # главная полочка












            if appstore_status == 'yes':

                img = pygame.image.load('Images/1.jpg')
                img = pygame.image.load('Images/1.jpg').convert_alpha()
                img = pygame.transform.scale(img, (170, 200))
                screen.blit(img, (70, 135))



















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
    pygame.display.set_caption("LEGION")
    clock = pygame.time.Clock()




    i = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        i = i + 1
        if i == 36:
            #time.sleep(0.5)
            pygame.quit()
            run = False
            main_window_1000_600()



        screen.fill((22, 22, 22))

        red = (255, 30, 30)
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

        font = pygame.font.Font(None, 20)
        font = pygame.font.Font("Fonts/Buk.ttf", 30)
        loading = font.render("Loading", True, red)
        screen.blit(loading, (115, 40))

        font = pygame.font.Font(None, 20)
        font = pygame.font.Font("Fonts/Buk.ttf", 30)
        persent = font.render(str(i // 3.6), True, red)
        screen.blit(persent, (215, 40))


        pygame.gfxdraw.box(screen, pygame.Rect(0, 0, 300, 25), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(0, 0, 5, 100), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(0, 95, 300, 5), (35, 35, 35, 255))
        pygame.gfxdraw.box(screen, pygame.Rect(295, 0, 5, 100), (35, 35, 35, 255))

        font = pygame.font.Font(None, 20)
        font = pygame.font.Font("Fonts/Buk.ttf", 20)
        legion = font.render("LEGION", True, red)
        screen.blit(legion, (30, 1))






        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)






window_loading_300_100()




















