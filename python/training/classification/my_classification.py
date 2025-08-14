import jetson_inference
import jetson_utils

# The command you provided:
# imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/green/01.jpg test.jpg

# We will replicate the behavior of this command in Python.
# We'll use the specific paths and parameters from your command.

# Define the paths and parameters
model_path = "/home/nvidia8/jetson-inference/python/training/classification/models/traffic_lights/resnet18.onnx"
labels_path = "/home/nvidia8/jetson-inference/python/training/classification/models/traffic_lights/labels.txt"
input_image_path = "/home/nvidia8/jetson-inference/python/training/classification/data/traffic_lights/test/green/01.jpg"
output_image_path = "/home/nvidia8/jetson-inference/python/training/classification/data/traffic_lights/light_test.jpg"

# Initialize the network, including the input and output blob names
net = jetson_inference.imageNet(
    model=model_path,
    labels=labels_path,
    input_blob="input_0",  # Matches the command-line argument
    output_blob="output_0" # Matches the command-line argument
)

# Load the input image
img = jetson_utils.loadImage(input_image_path)

if img is None:
    print(f"Error: Failed to load image from {input_image_path}")
else:
    # Perform the classification
    class_id, confidence = net.Classify(img)

    # Check if classification was successful
    if confidence > 0.0:
        class_label = net.GetClassLabel(class_id)
        
        # Overlay the classification text onto the image
        font = jetson_utils.cudaFont()
        font.OverlayText(img, text=f"{class_label} {confidence*100:.2f}%", x=5, y=5, color=font.White, background=font.Gray40)

        # Print the result to the terminal
        print(f"Classified as: {class_label} (ID: {class_id}) with confidence of {confidence*100:.2f}%")

        # Save the output image with the overlay
        jetson_utils.saveImage(output_image_path, img)
        print(f"Output image saved to {output_image_path}")

    else:
        print("Classification failed or confidence is too low.")
