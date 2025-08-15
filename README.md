# Project Name PET

This project is inspired by the experience of my grandmother, who, despite her visual impairment, remains highly mobile and independent. However, she faces significant challenges with safely navigating pedestrian crossings due to her inability to see pedestrian traffic lights. The goal is to develop a practical and reliable digital aid to empower visually impaired pedestrians to cross streets safely and confidently.

The Pedestrian Traffic Light Detector is an intelligent guidance system specifically designed to assist visually impaired individuals in determining the current phase of pedestrian traffic lights at intersections. By using photograpic visual recognition, the system will notify users when it is safe to cross, when to wait.
Key Features
 Traffic Light Detection: Utilizes AI-powered computer vision to detect pedestrian traffic light colors (red, green) and has been trained on images from the US, Europe and Asia.
Feedback: Provides clear instructions to communicate the current light phase and such as the "walk" or "stop" status.

Objectives
Enhance pedestrian safety and confidence for visually impaired users.
Promote independent mobility for people with visual impairments.



Algorithm Explanation and How It Works
The Algorithm is trained to recognize the trafficlight colors based on an uploaded picture on vs code.
First you have to upload your image which will be tested according to this path: "/home/nvidia8/jetson-inference/python/training/classification/data/traffic_lights/test/green/01.JPG"                           You will have to adjust the name of your input image in the path on the script.
Make sure you’re in the right path while running the script “my_classification1.py” with “python3 my_classification1.py”.
When the classification is done, you will receive a printed message in the terminal, telling you if you’re allowed to cross and with what percentage the traffic light was recognized.


## Running this project

1. Add steps for running this project.
2. Make sure to include any required libraries that need to be installed for your project to run.

[[View a video explanation here](video link)](https://drive.google.com/file/d/1iBWRl6-b8WPPXRKmsdP-ZS_kU0s7UBrv/view?usp=drive_link)

