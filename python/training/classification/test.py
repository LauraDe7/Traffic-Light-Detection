import cv2
import numpy as np

# Lade das ONNX-Modell
net = cv2.dnn.readNetFromONNX("traffic_light_model.onnx")

# Lade ein Testbild
image = cv2.imread('test_image.jpg') # Ersetze dies durch den Pfad zu einem deiner Testbilder
# Verkleinere das Bild auf die Größe, die dein Modell erwartet (z.B. 64x64)
input_image = cv2.resize(image, (64, 64))

# Normalisiere die Pixelwerte und konvertiere das Bild in einen Blob
blob = cv2.dnn.blobFromImage(input_image, 1.0, (64, 64), (0, 0, 0), swapRB=False, crop=False)

# Führe eine Vorhersage durch
net.setInput(blob)
output = net.forward()

# Die Klassennamen
class_names = ['red', 'green', 'yellow', 'white']

# Finde die Klasse mit der höchsten Wahrscheinlichkeit
class_id = np.argmax(output)
confidence = output[0][class_id]

predicted_class = class_names[class_id]

print(f"Das Modell hat die Farbe als {predicted_class} mit einer Wahrscheinlichkeit von {confidence:.2f} erkannt.")
