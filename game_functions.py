import sys
import pygame
from bullet import Bullet


def check_events(ship, ai_setting, screen, bullets): #bullets
    # Inicia o laço principal do jogo
    for event in pygame.event.get():
        """Responde a eventos de pressionamento de teclas e de mouse"""
        if event.type == pygame.QUIT:
            sys.exit()
 
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting,screen, ship, bullets)
            

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
                    
                
def check_keydown_events(event,ai_setting, screen, ship, bullets): 
    """Responde a pressionamentos de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.rect.centerx += 1
        ship.moving_rigth = True
            
    elif event.key == pygame.K_LEFT:
        ship.rect.centerx -= 1
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen,ship, bullets)
        


        


def check_keyup_events(event, ship):
    """Responde a soltura da tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_rigth = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False 



        
def update_screen(ai_setting, screen, ship, bullets):  #bullets
    """Atualiza as imagens na tela e alterna para a nova tela."""  
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_setting.color)
   
    # Redesenha todos os projéteis atras da espaconave e dos aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Deixa a tela mais recente vísivel
    pygame.display.flip() 


def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: 
            bullets.remove(bullet)
    

def fire_bullet(ai_setting, screen,ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    if len(bullets) < ai_setting.bullets_allowed:
            new_bullet = Bullet(ai_setting, screen, ship)
            bullets.add(new_bullet)       