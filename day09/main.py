import pygame

import game


# pygame setup
def main():
    main_color = 'white'
    pygame.init()
    word = game.random_word_list()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    check_game = True
    mp = []
    msgX = game.msgX
    msgY = game.msgY
    word = game.random_word_list()
    game.button_texts = []
    game.buttons = []
    game.penalties = 0
    game.check_word = []
    score = game.get_data()['score']
    high_score = game.get_data()['high_score']
    hearts = 12

    # Charger et redimensionner l'image UNE seule fois
    image = pygame.image.load("Asset/Background/image.png")
    image = pygame.transform.scale(image, (1280, 720))

    # Charger et redimensionner l'image UNE seule fois
    image_loose = pygame.image.load("Asset/Background/death.png")
    image_loose = pygame.transform.scale(image_loose, (1280, 720))

    # flip() the display to put your work on screen
    pygame.display.set_caption('HANGMAN')
    pygame.display.flip()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(game.buttons):
                    if check_game:
                        if button.collidepoint(event.pos):
                            # Mettre à jour le score
                            game.userinput(game.button_texts[i], word)
                            msgX, msgY, check_game = game.check(word)
                            mp.append(game.button_texts[i])
                if pygame.Rect(480, 450, 200, 80).collidepoint(event.pos):
                    main()

            # afficher l’image de fond
        screen.blit(image, (0, 0))

        game.rect_alpha((30, 240), (370 + (len(word) * 30), 120))
        game.display('GUESS THE WORD :', (100, 360 - 70), main_color, 40)
        game.display(game.word_find(word), (400 - 10, 355 - 70), main_color, 50)
        game.keyboard(mp)

        if msgX != '':
            screen.blit(image, (0, 0))
            game.rect_alpha((200, 200), (750 + (len(word) * 15), 350))

            if msgX == 'YOU WIN!':
                game.display(f'{msgX}'.upper(), (470, 250), 'white', 80)
                game.display(f'{msgY}'.upper(), (250, 350), main_color, 30)
                game.button_interface('REPLAY', 'white', 'black', (490, 430), (200, 80))

            elif msgX == 'GAME OVER':
                screen.blit(image_loose, (0, 0))
                game.rect_alpha((200, 200), (750 + (len(word) * 15), 350))
                game.display(f'{msgX}'.upper(), (420, 230), 'red', 80)
                game.display(f'{msgY}'.upper(), (470, 350), main_color, 30)
                game.button_interface('REPLAY', 'white', 'black', (490, 430), (200, 80))

        game.rect_alpha((30, 20), (550, 60))
        game.display(f'SCORE: {score}'.upper(), (40, 40), main_color, 36)
        game.display(f'HIGN SCORE: {high_score}'.upper(), (200, 40), main_color, 36)
        game.display(f'HEARTS️: {hearts - game.penalties}'.upper(), (410, 40), main_color, 36)

        pygame.display.flip()
        pygame.time.delay(50)  # Juste pour ralentir un peu la mise à jour du score
    pygame.quit()


main()
