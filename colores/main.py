import subprocess
import json

def tomar_foto():
    pass

def enviar_colores():
    pass

def hacer_solicitud():
    respuesta = subprocess.run(["node", "index.js", "morado.jpeg"], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True)
    print(type(respuesta.stdout))
    print(json.loads(respuesta.stdout))

if __name__=='__main__':
    hacer_solicitud()