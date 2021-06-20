import pygame

class Ship():
    """Inicializa a espaçonave e define sua posição inicial."""

    def __init__(self, ai_setting, screen):
        # Carrega a imagem da espaçonave e obtém seu rect 
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load('imagens/space-invaders.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Armazenna um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

        self.moving_rigth = False
        self.moving_left = False


    def update(self):
        """Atualiza a posição da espaçonave de acordo com as flags de movimento."""

        if self.moving_rigth and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center




    def blitme(self):
        self.screen.blit(self.image, self.rect)

