import cv2
from ultralytics import YOLO

# 1. 모델 로드 (상태 출력 생략   

# 2. 웹캠 연결
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(1)

# 창 이름 및 설정
win_name = "YOLOv8 Agriculture Vision Test"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(win_name, cv2.WND_PROP_TOPMOST, 1) # 창을 맨 위로 유지

print("--- 실시간 YOLO 객체 탐지 시작 ---")
print("- 화면 창이 뜨면 클릭 후 'q'를 눌러 종료하세요.")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # 3. 모델 추론 (verbose=False로 터미널 텍스트 출력 방지)
    results = model.predict(frame, verbose=False, stream=True)

    # 4. 결과 시각화
    for r in results:
        annotated_frame = r.plot() 
        
    # 화면 표시
    cv2.imshow(win_name, annotated_frame)

    # 'q' 키를 누르면 종료 (OpenCV 창이 선택된 상태여야 함)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
