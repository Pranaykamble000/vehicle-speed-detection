import cv2 
def draw_lines(frame, line_a_y, line_b_y):
    height, width = frame.shape[:2]
    cv2.line(frame, (0, line_a_y), (width, line_a_y), (255, 0, 0), 2)
    cv2.line(frame, (0, line_b_y), (width, line_b_y), (0, 255, 0), 2)