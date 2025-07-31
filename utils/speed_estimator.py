import time 

class SpeedEstimator:
    def __init__(self, pixel_per_meter, fps):
        self.line_positions = [250, 400]  # y-coordinates of the Line A and B
        self.cross_times = {}
        self.pixel_per_meter = pixel_per_meter
        self.fps = fps
        self.real_distance_m = abs(self.line_positions[1] - self.line_positions[0]) / pixel_per_meter

    def update(self, track_id, y, frame_count):
        if track_id not in self.cross_times:
            self.cross_times[track_id] = {"A": None, "B": None}
        if y < self.line_positions[0] and self.cross_times[track_id]["A"] is None:
            self.cross_times[track_id]["A"] = frame_count
        elif y > self.line_positions[1] and self.cross_times[track_id]["B"] is None:
            self.cross_times[track_id]["B"] = frame_count

    def calculate_speed(self, track_id):
        data = self.cross_times.get(track_id, {})
        if data.get("A") is not None and data.get("B") is not None:
            time_s = (data["B"] - data["A"]) / self.fps
            if time_s <= 0:
                return None
            speed = self.real_distance_m / time_s
            return round(speed * 3.6, 2)  # m/s to km/h
        return None