import base64
import requests
import json

class Imagen:
    def __init__(self, url):
        """
            Clase que envía la foto al endpoint que se define al inicio de la clases
            input:
                - URL: String con el end-point del api a consumir
        """
        self.url = url

    def __convertir_imagen(self, path):
        """
        Convierte la imagen a base 64 para poder enviarla al api
        Input:
            - Path: String con el valor de la ruta en donde está almacenada la imagen
            en local
        Out:
            - imagen: Bytes que tienen la imagen códificada
        """
        image = open(path, 'rb')
        image_read = image.read()
        image_64_encode = base64.encodestring(image_read)
        return image_64_encode.decode('ascii')

    def enviar(self, path):
        """
        Envía la imagen usando requests, la imagen se envía con una solicitud POST
        Input:
            - Path: String con el valor de la ruta en donde está almacenada la imagen
            en local
        Out:
            - Response: JSON  con la respuesta del API; con la información de los elementos
                encontrados en la imagen envíada
        """
        content = self.__convertir_imagen(path)
        
        body = {
            'autonomo': True,
            'name': path.split('/')[-1],
            'content': content
        }

        header = { 
            'Accept': 'application/json, text/plain',
            'Content-Type': 'application/json;charset=UTF-8'
        }

        r = requests.post(self.url, headers=header, data=json.dumps(body))
        
        return r.json()