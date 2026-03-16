# Servo Control with Facial Recognition

An AI-powered computer vision project that performs real-time face recognition and automatically controls a servo motor using Arduino. The system detects and recognizes a person through a webcam and triggers a servo action, demonstrating integration between AI, IoT, and hardware automation.

## Overview

This project combines Computer Vision, Machine Learning, and IoT hardware to create a smart recognition-based automation system. When a recognized face appears in front of the camera, the system identifies the person and sends a command to Arduino UNO to rotate a servo motor.

The project demonstrates how AI-based identity recognition can be used in applications like:

Smart door access systems

Automated attendance systems

Security monitoring

Smart home automation

## Features

Real-time face detection and recognition

Automatic servo motor control

Integration with Arduino UNO

Firebase database integration for storing personnel data

Face encoding for faster recognition

Camera-based live video processing

## Technologies Used
## Programming

Python

AI / Computer Vision

OpenCV

face_recognition library

NumPy

IoT / Hardware

Arduino UNO

Servo Motor

PyFirmata

Cloud / Database

Firebase Realtime Database

Firebase Storage

Other Tools

CVZone

Pickle (for encoding storage)

## Project Structure
Servo-Control-with-Facial-Recognition
│
├── main.py
│   Runs the real-time face recognition and controls the servo motor.
│
├── EncodeGenerator.py
│   Generates facial encodings and uploads images to Firebase.
│
├── DataToDatabase.py
│   Uploads personnel information to Firebase database.
│
└── README.md
## How It Works

Face images are collected and stored in a dataset.

EncodeGenerator.py processes the images and generates face encodings.

Encodings are stored using Pickle for quick recognition.

main.py starts the webcam and detects faces in real time.

When a known face is detected:

The system verifies the identity

Sends a signal to Arduino

Arduino rotates the servo motor

## Installation

1. Clone the Repository
git clone https://github.com/yourusername/Servo-Control-with-Facial-Recognition.git
cd Servo-Control-with-Facial-Recognition

2. Install Dependencies
pip install opencv-python
pip install face-recognition
pip install numpy
pip install firebase-admin
pip install cvzone
pip install pyfirmata

3. Configure Firebase

Add your Firebase credentials:

serviceAccountKey.json

Update the following in the scripts:

databaseURL
storageBucket

4. Connect Arduino

Connect Arduino UNO to your computer

Update the port in main.py

Example:

port = 'COM5'

5. Run the System

Generate face encodings:

python EncodeGenerator.py

Upload data to Firebase:

python DataToDatabase.py

Start the recognition system:

python main.py

## Hardware Requirements

Arduino UNO

Servo Motor

USB Camera / Webcam

Jumper Wires

Computer

Applications

Smart security systems

AI-powered access control

Automated attendance systems

Smart home entry systems

Future Improvements

Deploy using edge AI devices like Raspberry Pi

Add multi-user recognition

Integrate mobile app notifications

Improve recognition accuracy using deep learning models

Add door lock control instead of servo motor
