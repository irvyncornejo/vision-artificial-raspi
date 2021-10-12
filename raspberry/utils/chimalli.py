import time

from gpiozero import RGBLED
from gpiozero import Buzzer
from gpiozero import DistanceSensor

class Chimalli:
    """
    Clase que contiene agrupado los componentes que están configurados
    en la shield chimalli
    """
    def __init__(self):
        self.flash = RGBLED(red=21, green=20, blue=19)
        self.colores = [(0.5, 1, 1), (1, 0.5, 1), (1, 1, 0.5)]
        self.buzzer = Buzzer(18)
        self.ultrasonico = DistanceSensor(16, 7)#echo, trigger

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
        
    def leer_ultrasonico(self):
        """
        Función que activa la lectura del sensor ultrasonico, la distancia la
        regresa en cm
        """
        time.sleep(1)
        cm = self.ultrasonico.distance * 100
        return cm
    
    