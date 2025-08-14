import jetson_inference
import jetson_utils
import os

MODEL_PATH = "/home/nvidia8/jetson-inference/python/training/classification/models/traffic_lights"
TEST_IMAGE = "/home/nvidia8/jetson-inference/python/training/classification/data/traffic_lights/test/green/copy1.jpg"

net = jetson_inference.imageNet(
    model=os.path.join(MODEL_PATH, "resnet18.onnx"),
    labels=os.path.join(MODEL_PATH, "labels.txt")
)

img = jetson_utils.loadImage(TEST_IMAGE)

class_id, confidence = net.Classify(img)
class_label = net.GetClassLabel(class_id)

print(f"Detected: {class_label} ({confidence*100:.2f}%)")

if class_label == "green":
    print("Green: You're allowed to cross")
elif class_label == "red":
    print("Red: Don't cross")
elif class_label == "white":
    print("White: You're allowed to cross")
else:
    print("Unknown color detected")
