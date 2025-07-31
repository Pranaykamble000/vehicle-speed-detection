from ultralytics import YOLO
import numpy as np

class YOLODetector:
    def __init__(self, model_path="models/yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):
        if frame is None or not isinstance(frame, np.ndarray):
            raise ValueError("Invalid frame passed to YOLODetector")

        # Run YOLO prediction
        results = self.model.predict(source=frame, conf=0.4, verbose=False)
        detections = []
        if results and hasattr(results[0], 'boxes') and results[0].boxes is not None:
            boxes = results[0].boxes.data.cpu().numpy()
            for box in boxes:
                x1, y1, x2, y2, score, class_id = box
                detections.append({
                    "bbox": [float(x1), float(y1), float(x2), float(y2)],
                    "confidence": float(score),
                    "class_id": int(class_id)
                })
        return detections