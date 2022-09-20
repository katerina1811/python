# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# line = "забвение, акваланг, торт, самозабвенный"
# words = line.split(' ')
# fragment = "абв"
# new_words = []
# for word in words:
#     if fragment not in word:
#         new_words.append(word)

# print(new_words)

# Создайте программу для игры в ""Крестики-нолики"".

# import pygame as pg
# import sys

# def check_win(mas, sign):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sign) == 3:
#             return sign
#     for col in range(3):
#         if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
#             return sign
#     if mas[0][0] == sign and mas[1][1] == sign and mas[2][2]:
#         return sign
#     if mas[0][2] == sign and mas[1][1] == sign and mas[2][0]:
#         return sign
#     if zeroes == 0:
#         return 'Piece'
#     return False


# pg.init()
# sizeblock = 100
# margine = 15
# width = heigth = sizeblock * 3 + margine * 4
# size_window = (width, heigth)
# screen = pg.display.set_mode(size_window)

# pg.display.set_caption('Крестики-нолики!')

# black = (0, 0, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)
# white = (255, 255, 255)
# mas = [[0] * 3 for i in range(3)]

# query = 0  
# game_over = False

# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()
#         elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
#             x_mouse, y_mouse = pg.mouse.get_pos()
#             col = x_mouse // (sizeblock + margine)
#             row = y_mouse // (sizeblock + margine)
#             if mas[row][col] == 0:
#                 if query % 2 == 0:
#                     mas[row][col] = 'x'
#                 else:
#                     mas[row][col] = 'o'
#                 query += 1

#         elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
#             game_over = False
#             mas = [[0] * 3 for i in range(3)]
#             query = 0
#             screen.fill(black)

#     if not game_over:
#         for row in range(3):
#             for col in range(3):
#                 if mas[row][col] == 'x':
#                     color = red
#                 elif mas[row][col] == 'o':
#                     color = green
#                 else:
#                     color = white
#                 x = col * sizeblock + (col + 1) * margine
#                 y = row * sizeblock + (row + 1) * margine
#                 pg.draw.rect(screen, color, (x, y, sizeblock, sizeblock))
#                 if color == red:
#                     pg.draw.line(screen, white, (x + 7, y + 7), (x + sizeblock - 7, y + sizeblock - 7), 3)
#                     pg.draw.line(screen, white, (x + 7, y + sizeblock - 7), (x + sizeblock - 7, y + 7), 3)
#                 elif color == green:
#                     pg.draw.circle(screen, white, (x + sizeblock // 2, y + sizeblock // 2), (sizeblock // 2 - 7), 3)
#         if (query - 1) % 2 == 0:
#             game_over = check_win(mas, 'x')
#         else:
#             game_over = check_win(mas, 'o')

#         if game_over:
#             screen.fill(black)
#             font = pg.font.SysFont('stxingkai', 80)
#             text1 = font.render(game_over, True, white)
#             text_rect = text1.get_rect()
#             text_x = screen.get_width() / 2 - text_rect.width / 2
#             text_y = screen.get_height() / 2 - text_rect.height / 2
#             screen.blit(text1, [text_x, text_y])

#     pg.display.update()

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data: 
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

outfile = open('sem5_out.txt', 'w', encoding='utf-8')
with open('sem5_in.txt', "r", encoding='utf-8') as rfile:
    for line in rfile:
        outfile.write(rle_encode(line))
outfile.close()


