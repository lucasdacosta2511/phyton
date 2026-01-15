import pygame
import time


pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r'C:\Users\lucas\OneDrive\Documentos\estudos\phyton\exercícios\teste.mp3')
pygame.mixer.music.play()
a = input('desligar:').strip().lower()

# Mantém o programa vivo enquanto a música toca
if a == 'sim':

    pygame.mixer.music.stop()
    print('Desligando')
else:
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)