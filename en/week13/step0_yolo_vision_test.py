import os
import cv2
from ultralytics import YOLO

# 1. Load model (omitting state output)
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "yolov8n.pt")
model = YOLO(model_path) 

# 2. Connect webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(1)

# Window name and settings
win_name = "YOLOv8 Agriculture Vision Test"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(win_name, cv2.WND_PROP_TOPMOST, 1) # Keep window on top

print("--- Real-time YOLO Object Detection Started ---")
print("- When the screen window appears, click on it and press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # 3. Model inference (verbose=False to prevent terminal text output)
    results = model.predict(frame, verbose=False, stream=True)

    # 4. Visualize results
    for r in results:
        annotated_frame = r.plot() 
        
    # Display on screen
    cv2.imshow(win_name, annotated_frame)

    # Press 'q' key to quit (OpenCV window must be selected)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
