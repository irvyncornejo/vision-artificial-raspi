import boto3

class Image:
    
    def __init__(self, fileName, bucket):
        self.client=boto3.client('rekognition')
        self.fileName = fileName
        self.bucket = bucket 
    
    def get_labels(self):
        response_label = self.client.detect_labels(
          Image={
              'S3Object':{
                'Bucket':self.bucket,
                'Name':self.fileName
              }
          }
        )
        return response_label
    
    def get_text(self):
        response_text = self.client.detect_text(
            Image={
              'S3Object':{
                'Bucket':self.bucket,
                'Name':self.fileName
              }
          }
        )
        return response_text
        

class Process:
    def __init__(self):
        self.parents = set()
    
    def __add(self, label):
        [self.parents.add(parent['Name']) for parent in label]
    
    def __sort(self, data):
        return sorted(data, key=lambda label: label['Confidence'], reverse=True)
    
    def load(self, res):
        data = [label for label in res["Labels"] if label['Confidence'] > 90]
        vehicles = [label['Name'] for label in data if label['Name'] in ['Car', 'Vehicle']]
        vehicle = lambda x: True if len(x) > 0 else False
        data = self.__sort(data)
        [self.__add(label['Parents']) for label in data]
    
        return{
            'data': data,
            'vehicle': vehicle(vehicles),
            'parents': list(self.parents)
        }
    
    def text_validate(self, text_in_image):
        plates = [text for text in text_in_image['TextDetections'] if text['Confidence'] > 90 and len(text['DetectedText']) == 5]
        return self.__sort(plates)