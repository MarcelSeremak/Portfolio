import sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from Hanoi.assets.classes.button import Button
from Hanoi.assets.classes.disc import Disc, Column
import pygame
from pygame import mixer

pygame.init()
mixer.init()
mixer.music.load("assets/muzyka.mp3")
mixer.music.play(-1)

background_color = (128, 229, 175)
window_size = (900, 500)

screen = pygame.display.set_mode(window_size)

game_font = pygame.font.Font("assets/Freedom-10eM.ttf", 100)
end_font = pygame.font.Font("assets/Freedom-10eM.ttf", 70)
button_font = pygame.font.Font("assets/Freedom-10eM.ttf", 30)
level_font = pygame.font.Font("assets/Freedom-10eM.ttf", 50)
columnt_font = pygame.font.Font("assets/Freedom-10eM.ttf", 20)
score_font = pygame.font.Font(None, 30)


def theEnd(discs, moves):
    """
    A function that turns on
    when you move of all disks on the last column
    """

    pygame.display.set_caption("Hanoi Tower / End")
    pygame.display.flip()
    while True:
        bg = pygame.image.load("assets/background.png")
        screen.blit(bg, (0, 0))

        menu_text = end_font.render("Congratulations", True, (255, 255, 255))
        shadow_menu_text = end_font.render("Congratulations", True, (0, 0, 0))
        screen.blit(shadow_menu_text, (window_size[0] // 2 - menu_text.get_width() // 2 - 7, 150))
        screen.blit(menu_text, (window_size[0] // 2 - menu_text.get_width() // 2, 150))

        # Write down the minimum number of moves on the end screen
        # in which you can complete a given level and
        # the number of moves in which the player completed the level
        if discs == 4:
            discs_text_record = score_font.render("Least possible moves is: 15", True, (255, 255, 255))
            shadow_discs_text_record = score_font.render(f"Least possible moves is: 15", True, (0, 0, 0))

        elif discs == 6:
            discs_text_record = score_font.render("Least possible moves is: 63", True, (255, 255, 255))
            shadow_discs_text_record = score_font.render(f"Least possible moves is: 63", True, (0, 0, 0))

        else:
            discs_text_record = score_font.render("Least possible moves is: 127", True, (255, 255, 255))
            shadow_discs_text_record = score_font.render(f"Least possible moves is: 127", True, (0, 0, 0))

        discs_text = score_font.render(f"You made it in: {moves} moves", True, (255, 255, 255))
        shadow_discs_text = score_font.render(f"You made it in: {moves} moves", True, (0, 0, 0))
        screen.blit(shadow_discs_text, (window_size[0] // 2 - discs_text.get_width() // 2 - 3, 250))
        screen.blit(discs_text, (window_size[0] // 2 - discs_text.get_width() // 2, 250))
        screen.blit(shadow_discs_text_record, (window_size[0] // 2 - discs_text_record.get_width() // 2 - 3, 300))
        screen.blit(discs_text_record, (window_size[0] // 2 - discs_text_record.get_width() // 2, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


def game(discs, level):
    """
    A function that triggers when the player selects difficulty level
    by pressing the button in the Main Menu
    """

    pygame.display.set_caption("Hanoi Tower / Game")
    pygame.display.flip()

    list_of_discs = [(180, 25), (160, 25), (140, 25), (120, 25), (100, 25), (80, 25), (60, 25)]
    list_of_colors = [(255, 0, 0),  (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]

    def drawColumns():
        """
        The drawColumns function draws three columns
        on the screen on which all disks will be placed
        """
        pygame.draw.rect(screen, (88, 66, 29), (100, 400, 200, 25))
        pygame.draw.rect(screen, (88, 66, 29), (350, 400, 200, 25))
        pygame.draw.rect(screen, (88, 66, 29), (600, 400, 200, 25))
        pygame.draw.rect(screen, (88, 66, 29), (190, 200, 20, 200))
        pygame.draw.rect(screen, (88, 66, 29), (440, 200, 20, 200))
        pygame.draw.rect(screen, (88, 66, 29), (690, 200, 20, 200))

        level_text = level_font.render(f"Level: {level.capitalize()}", True, (255, 255, 255))
        shadow_level_text = level_font.render(f"Level: {level.capitalize()}", True, (0, 0, 0))
        screen.blit(shadow_level_text, (window_size[0] // 2 - level_text.get_width() // 2 - 7, 60))
        screen.blit(level_text, (window_size[0] // 2 - level_text.get_width() // 2, 60))

    column1 = Column(200)
    column2 = Column(450)
    column3 = Column(700)
    isStartingPoint = True
    reserved = []
    moves = 0
    button1 = Button(100, 440, 200, 50, "Column", columnt_font)
    button2 = Button(350, 440, 200, 50, "Column", columnt_font)
    button3 = Button(600, 440, 200, 50, "Column", columnt_font)
    buttonMenu = Button(10, 10, 100, 30, "Menu", columnt_font)

    while True:

        mousepos = pygame.mouse.get_pos()
        bg = pygame.image.load("assets/background.png")
        screen.blit(bg, (0, 0))
        drawColumns()
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        buttonMenu.draw(screen)

        button1.check_collision(mousepos)
        button2.check_collision(mousepos)
        button3.check_collision(mousepos)
        buttonMenu.check_collision(mousepos)



        def is_clicked(self, event):
            return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

        if isStartingPoint:
            # If this is the first loop over while True
            # every disc will be added to the first column
            # and text about level will be written up on the screen
            if level == "easy":
                level_string = "Level: Easy"

            elif level == "medium":
                level_string = "Level: Medium"

            else:
                level_string = "Level: Hard"

            level_text = level_font.render(level_string, True, (255, 255, 255))
            shadow_level_text = level_font.render(level_string, True, (0, 0, 0))
            screen.blit(shadow_level_text, (window_size[0] // 2 - level_text.get_width() // 2 - 7, 60))
            screen.blit(level_text, (window_size[0] // 2 - level_text.get_width() // 2, 60))
            for i in range(discs):
                disc = Disc(list_of_discs[i][0], list_of_discs[i][1], list_of_colors[i])
                column1.add(disc)
            column1.drawDiscs(screen)
            isStartingPoint = False


        else:
            # If it's another loop in a row
            # checks the conditions if the player wants to move the disc from
            # reserved list, i.e. the disk raised to the top
            # or checks if the player wants to put the Reserved Disk on the
            # column using the column button under the column
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if column1.discs != []:
                    if column1.discs[-1].is_clicked(event) and reserved == []:
                        column1.discs[-1].get_above(screen)
                        reserved.append(column1.rem())

                if column2.discs != []:
                    if column2.discs[-1].is_clicked(event) and reserved == []:
                        column2.discs[-1].get_above(screen)
                        reserved.append(column2.rem())

                if column3.discs != []:
                    if column3.discs[-1].is_clicked(event) and reserved == []:
                        column3.discs[-1].get_above(screen)
                        reserved.append(column3.rem())

                if reserved != []:
                    if button1.is_clicked(event):
                        if column1.discs == []:
                            column1.add(reserved[0])
                            reserved.clear()
                            moves += 1
                        elif column1.discs[-1].width > reserved[0].width:
                            column1.add(reserved[0])
                            reserved.clear()
                            moves += 1
                    elif button2.is_clicked(event):
                        if column2.discs == []:
                            column2.add(reserved[0])
                            reserved.clear()
                            moves += 1
                        elif column2.discs[-1].width > reserved[0].width:
                            column2.add(reserved[0])
                            reserved.clear()
                            moves += 1
                    elif button3.is_clicked(event):
                        if column3.discs == []:
                            column3.add(reserved[0])
                            reserved.clear()
                            moves += 1
                        elif column3.discs[-1].width > reserved[0].width:
                            column3.add(reserved[0])
                            reserved.clear()
                            moves += 1

                if buttonMenu.is_clicked(event):
                    mainMenu()

            column1.drawDiscs(screen)
            column2.drawDiscs(screen)
            column3.drawDiscs(screen)

            if reserved != []:
                reserved[0].get_above(screen)

            # If all the discs are on the last column
            # program will activate theEnd function with
            # credits about player's score
            if len(column3.discs) == discs:
                theEnd(discs, moves)





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


def mainMenu():
    """
    The initial function, which is activated when the program starts,
    shows the Main Menu,
    where there are three difficulty levels to choose from: Easy, Medium, Hard
    """
    pygame.display.set_caption("Hanoi Tower / Menu")
    pygame.display.flip()


    while True:
        bg = pygame.image.load("assets/background.png")
        screen.blit(bg, (0, 0))
        menu_text = game_font.render("Main Menu", True, (255, 255, 255))
        shadow_menu_text = game_font.render("Main Menu", True, (0, 0, 0))
        screen.blit(shadow_menu_text, (window_size[0] // 2 - menu_text.get_width() // 2 - 7, 60))
        screen.blit(menu_text, (window_size[0] // 2 - menu_text.get_width() // 2, 60))

        easy_button = Button(100, 250, 200, 100, "Easy", button_font, color=(132, 233, 133), hover_color=(73, 202, 77))
        medium_button = Button(350, 250, 200, 100, "Medium", button_font, color=(209, 212, 128), hover_color=(252, 109, 0))
        hard_button = Button(600, 250, 200, 100, "Hard", button_font, color=(216, 93, 89), hover_color=(199, 14, 8))
        mouse_pos = pygame.mouse.get_pos()


        easy_button.check_collision(mouse_pos)
        medium_button.check_collision(mouse_pos)
        hard_button.check_collision(mouse_pos)

        easy_button.draw(screen)
        medium_button.draw(screen)
        hard_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif easy_button.is_clicked(event):
                game(discs=4, level="easy")

            elif medium_button.is_clicked(event):
                game(discs=6, level="medium")

            elif hard_button.is_clicked(event):
                game(discs=7, level="hard")

        pygame.display.flip()

mainMenu()

