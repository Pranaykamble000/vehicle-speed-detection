from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)

    def update(self, detections, frame):
        tracks = []
        for det in detections:
            if det["class_id"] in [2, 3, 5, 7]:
                # car, motorcycle, bus, truck
                tracks.append([list(det["bbox"]), det["confidence"]])
        tracked_objects = self.tracker.update_tracks(tracks, frame=frame)
        output = []
        for track in tracked_objects:
            if not track.is_confirmed():
                continue
            bbox = track.to_ltrb()
            output.append({
                "track_id": track.track_id if hasattr(track, 'track_id') else track.tracked_id,
                "bbox": bbox
            })
        return output
