import cv2
import os

class QrReader:
    def __init__(self, file):
        self.data = None
        
        if not os.path.exists(file):
            print(f"La carpeta '{file}' no existe.")
            return
        
        image = cv2.imread(file)
        detector = cv2.QRCodeDetector()
        data, points, _ = detector.detectAndDecode(image)
        if data:
            self.data = data

    def get_data(self):
        return self.data
