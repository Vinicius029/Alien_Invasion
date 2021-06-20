class Setting():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""

    def __init__(self):
        self.width = 1000
        self.height = 700
        self.color = (230,230,230)
        self.ship_speed_factor = 2

        #Configuração dos projéteis
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3


