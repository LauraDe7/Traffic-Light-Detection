import jetson_inference
import jetson_utils

net= jetson_inference.imageNet(
model= "/home/nvidia/jetson-inference/python/training/classification/models/traffic_lights/resnet18.onnx",
labels="/home/nvidia/jetson-inference/python/training/classification/models/traffic_lights/labels.txt",
)

img=jetson_utils.loadImage("jetson-inference/python/training/classification/data/traffic_lights/test/green/copy1.jpg")

class_id, confidence = net.Classify(img)
class_label = net.GetClassLabel(class_id)

if class_label == "green":
    print("Green; You're allowed to cross")
elif class_label == "red":
    print("Red: Don't cross")
elif class_label== "yellow":
    print("Yellow: The light will change soon")
elif class_label == "white":
    print("White= You're allowed to cross")
