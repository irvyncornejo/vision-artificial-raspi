import time

from gpiozero import RGBLED, Buzzer

class Chimalli:
    """
    Clase que contiene agrupado los componentes que están configurados
    en la shield chimalli
    """
    def __init__(self):
        self.flash = RGBLED(red=21, green=20, blue=19)
        self.colores = [(0.5, 1, 1), (1, 0.5, 1), (1, 1, 0.5)]
        self.buzzer = Buzzer(18)

    def genera_flash(self):
        for color in self.colores:
            self.flash.color = color
            time.sleep(1)

    def apaga_rgb(self):
        self.flash.color = (1, 1, 1)

    def enciende_rgb(self):
        self.flash.color = (0.75, 0.75, 0.75)
    
    def crear_alerta_sonido(self, tiempo):
        self.buzzer.on()
        time.sleep(tiempo)
        self.buzzer.off()
        time.sleep(tiempo)