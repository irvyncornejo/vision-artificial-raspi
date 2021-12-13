from time import sleep

from gpiozero import Button

from utils.camara import Camara
from utils.chimalli import Chimalli

import I2C_LCD_driver

camara = Camara()
chimalli = Chimalli()
mylcd = I2C_LCD_driver.lcd()

if __name__=='__main__':
    while True:
        distancia = chimalli.leer_ultrasonico()
        print(distancia)
        mylcd.lcd_display_string(f'{distancia}', 1)
        sleep(1)
        mylcd.lcd_clear()
