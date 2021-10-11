import drivers
from time import sleep

from gpiozero import Button

from utils.camara import Camara
from utils.chimalli import Chimalli

camara = Camara()
chimalli = Chimalli()
display = drivers.Lcd()


if __name__=='__main__':
    pass