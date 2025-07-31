
import cv2
import yaml
from detectors.yolo_detector import YOLODetector 
from trackers.deep_sort_trackers import Tracker
from utils.speed_estimator import SpeedEstimator
from utils.drawing import draw_lines
from datetime import datetime
import csv

# Load configuration settings
with open("config/settings.yaml", "r") as file:
    config = yaml.safe_load(file)

# Initialize modules
detector = YOLODetector(model_path= config["model_path"])
tracker = Tracker()
cap = cv2.VideoCapture(0)
# Real-time webcam input

fps =cap.get(cv2.CAP_PROP_FPS) or 30

# Fallback to 30 FPS if unknown 
estimator = SpeedEstimator(pixel_per_meter=config["pixel_per_meter"], fps=fps)
frame_count = 0

# Log to CSV
def log_speed(track_id, speed):
    with open(config["log_file"], "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), track_id, speed])

# Real-time loop 
while True:

    ret, frame = cap.read()
    if not ret or frame is None:
        print("Frame not captured. Skipping...")
        continue
    # Increase brightness & contrast
    frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=30)

    detections = detector.detect(frame)
    tracks = tracker.update(detections, frame)

    for obj in tracks:
        x1, y1, x2, y2 = map(int, obj["bbox"])
        track_id = obj["track_id"]

        # Debug: print y1 and line positions
        print(f"Track ID: {track_id}, y1: {y1}, line_a_y: {config['line_a_y']}, line_b_y: {config['line_b_y']}")

        estimator.update(track_id, y1, frame_count)
        speed = estimator.calculate_speed(track_id)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
        cv2.putText(frame, f"ID:{track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

        if speed:
            print(f"Speed calculated for Track ID {track_id}: {speed} km/h")
            cv2.putText(frame, f"{speed} km/h", (x1, y2 + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            log_speed(track_id, speed)

    draw_lines(frame, config["line_a_y"], config["line_b_y"])
    cv2.imshow("Vehicle Speed Detection(real-time)", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        # ESC key to break
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()