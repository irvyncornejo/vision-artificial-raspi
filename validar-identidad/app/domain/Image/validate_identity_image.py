import base64

class ValidateIdentityImage:
    
    def convert_imagen(self, path):
        image = open(path, 'rb')
        image_read = image.read()
        image_64_encode = base64.encodestring(image_read)
        return image_64_encode.decode('ascii')
    
    def convert_video(self, path):
        pass