import pygame
import sys
import pyautogui

pygame.init()

screen_width, screen_height = pyautogui.size()

win_width, win_height = screen_width / 2, screen_height / 2
win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("Move Hand")

background_color = (0, 255, 0)

scale = 0.5

hand_img = pygame.image.load("Hand.png")
hand_width, hand_height = hand_img.get_size()
hand_img = pygame.transform.smoothscale(pygame.image.load("Hand.png"), (int(hand_width*scale), int(hand_height*scale)))

anchor_x = 100
anchor_y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_x, mouse_y = pyautogui.position()

    hand_x = (mouse_x / screen_width) * win_width - anchor_x * scale
    hand_y = (mouse_y / screen_height) * win_height - anchor_y * scale

    win.fill(background_color)

    scaled_hand_width = int(hand_width * scale)
    scaled_hand_height = int(hand_height * scale)
    scaled_hand_img = pygame.transform.scale(hand_img, (scaled_hand_width, scaled_hand_height))
    
    win.blit(scaled_hand_img, (hand_x, hand_y))

    pygame.display.update()