import time
from datetime import datetime
from picamera import PiCamera



class Camara:
    """
    Clase que permite tener acceso a la pi-camara
    """
    def __init__(self):
        self.camera = PiCamera()
    
    def tomar_foto(self):
        """
        Función para hacer la captura usando la cámara, lo almacena en la carpeta temporal
        el nombre esta conpuesta por la palabra imagen y la fecha y hora de la caprura
        return:
            - url: String con la ruta en la que se puede tomar la foto
        """
        path = lambda x: f'/tmp/image{x}.jpg'
        hora = datetime.now()
        hora_string = hora.strftime('%d%m%Y%H%M%S')
        url = path(hora_string)
        self.camera.capture(url)
        time.sleep(1)
        return url