import datetime
import json
import random

import numpy as np
import pygame

screen = None
check_word = []


def button_interface(name, btn_color, txt_color, pos, size):
    # Définir la position et la taille du bouton
    button_rect = pygame.Rect(pos, size)

    # Police pour le texte
    font = pygame.font.Font(None, 36)
    # Dessiner le bouton
    pygame.draw.rect(screen, btn_color, button_rect)

    # Ajouter du texte sur le bouton
    text = font.render(name, True, txt_color)
    screen.blit(text, (button_rect.x + 50, button_rect.y + 25))


def button_menu(name, btn_color, txt_color, pos, size):
    button_interface('', 'black', 'white', (pos[0] - 5, pos[1] - 5), (size[0] + 10, size[1] + 10))
    button_interface(name, btn_color, txt_color, pos, size)


def rect_alpha(pos, size):
    s = pygame.Surface(size, pygame.SRCALPHA)
    s.fill((0, 0, 0, 128))
    screen.blit(s, pos)


def read_file(name):
    try:
        with open(name, 'r') as f:
            return json.load(f)
    except:
        return False


def write_file(name, content):
    with open(name, 'w') as f:
        json.dump(content, f, indent=2)


def get_data():
    data = read_file('Models/data.json')
    if not data:
        data = dict(score=0, high_score=0, date=datetime.date.today().strftime("%d/%m/%Y"))
    return data


def display(msg, pos, color, size):
    # Initialiser la police
    msg = f'{msg}'
    font = pygame.font.Font(None, size)
    # Calculer la position pour centrer le texte
    text = font.render(msg, True, color)
    screen.blit(text, pos)


def word_find(word):
    display = ''
    for i in word:
        if i in check_word:
            display += i
        else:
            display += '_ '
    return display


def random_word_list():
    word = []
    with open('Models/my_other_wordlist.txt') as f:
        for i in f.readlines():
            word.append(i.strip())
    return list(random.choice(word).upper())


def keyboard(mp=[]):
    global button_texts, buttons
    mp = np.unique(mp).tolist()

    button_texts = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']

    buttons = []

    x = 970
    y = 100
    index = 4
    new_button = []

    for j in button_texts:
        if j not in mp:
            new_button.append(j)
            button_texts = new_button

    for i in range(len(button_texts)):
        buttons.append(pygame.Rect(x, y, 50, 50))
        x += 60
        if i == index - 1:
            x = 970
            y += 60
            index += 4

    font = pygame.font.Font(None, 36)

    for i, button in enumerate(buttons):
        rect_alpha((button.x, button.y), (50, 50))

        text = font.render(button_texts[i], True, 'white')
        screen.blit(text, (button.x + 17, button.y + 13))


def userinput(user_input, word):
    global check_word, penalties
    if user_input in word:
        check_word.append(user_input)
    else:
        penalties += 1


def check(word):
    score = get_data()['score']
    msgX = ''
    msgY = ''
    x = ''.join(word)
    word_check = True
    check_game = True
    data = get_data()

    for i in word:
        if i not in check_word:
            word_check = False

    if word_check:
        check_game = False
        data = get_data()
        score += 1
        msgX = 'YOU WIN!'
        msgY = f"Best ever!!! You've guessed {x} in {score} high score."
        if data:
            if score > data['high_score']:
                data = dict(score=score, high_score=score, date=datetime.date.today().strftime("%d/%m/%Y"))
                write_file('Models/data.json', data)
            else:
                data['score'] = score
                write_file('Models/data.json', data)
                msgY = f"You've guessed '{x}' in {score} score.The record is {data['high_score']} high score."
        else:
            data = dict(score=score, high_score=score, date=datetime.date.today().strftime("%d/%m/%Y"))
            write_file('Models/data.json', data)

    elif penalties >= 12:
        data['score'] = 0
        write_file('Models/data.json', data)
        msgX = 'GAME OVER'
        msgY = f"The word was '{x}'."
        check_game = False

    return msgX, msgY, check_game
