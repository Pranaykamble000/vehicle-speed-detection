# Vehicle Speed Detection in Real-Time

## Overview

This project detects vehicles and estimates their speed in real time using a video stream. It uses the **Ultralytics YOLOv8** model for vehicle detection, **Deep SORT** for tracking vehicles, and **OpenCV** for real-time video capture and processing. The speed of each vehicle is estimated based on the movement of the object between frames, calculated in meters per second or other units (such as km/h) using a pixel-to-distance conversion factor. 

The project is designed to work with live video feeds or pre-recorded videos, providing real-time annotations overlaid on the video to display the estimated speed of detected vehicles.

## Technologies & Libraries

- **Ultralytics YOLOv8** – Object detection for vehicle classification.
- **OpenCV** – Real-time video capture and processing.
- **NumPy** – Efficient numerical computation for processing frames.
- **Pandas** – Data manipulation for tracking vehicles and logging speeds.
- **FilterPy** – Kalman filter for smoothing vehicle trajectories.
- **SciPy** – For additional scientific calculations in speed estimation.
- **lap** – Linear assignment problem solver for multi-object tracking.
- **scikit-image** – Enhancements and image processing techniques.
- **DeepSORT** – Deep learning-based tracking algorithm.
- **PyYAML** – For configuration file parsing.

## Setup

### Prerequisites

Ensure you have Python 3.7 or higher installed. It's recommended to create a virtual environment for the project.

### Steps to Set Up the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pranaykamble000/vehicle-speed-detection.git
   cd vehicle-speed-detection


2. **Create Virtual Environment**:
    python -m venv venv
   venv\Scripts\activate
pip install -r requirements.txt
       deactivate

   python vehicle_speed_detection.py --input 0 --output video/output_video.mp4

### Key Points to Remember:
- **Activate the virtual environment** before installing dependencies.
- Use **`pip freeze > requirements.txt`** to generate the list of installed libraries if needed.
- Copy the exact **code blocks** provided above into your `README.md`.

Let me know if you need any further clarification!




   
