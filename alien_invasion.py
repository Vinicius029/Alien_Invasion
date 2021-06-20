import pygame

from pygame.sprite import Group

from settings import Setting
from ship import Ship
import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    ai_setting = Setting()
    

    screen = pygame.display.set_mode((ai_setting.width, ai_setting.height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(ai_setting, screen)
    bullets = Group()
    

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(ship, ai_setting, screen, bullets)  
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, bullets) 
        

run_game()