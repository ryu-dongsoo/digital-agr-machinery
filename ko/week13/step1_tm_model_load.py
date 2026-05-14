import cv2
import numpy as np
# tensorflow 및 keras 설치 필요 (pip install tensorflow)
from tensorflow.keras.models import load_model

# 1. 모델 및 라벨 로드
# Teachable Machine에서 'Tensorflow -> Keras'로 다운로드한 파일을 같은 폴더에 넣어야 합니다.
try:
    model = load_model("keras_model.h5", compile=False)
    class_names = open("labels.txt", "r", encoding="utf-8").readlines()
except:
    print("[오류] keras_model.h5 또는 labels.txt 파일을 찾을 수 없습니다.")
    print("티쳐블 머신에서 모델을 내보내기한 후 실습 폴더에 복사해주세요.")
    exit()

# 2. 웹캠 연결
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 3. 이미지 전처리 (모델 입력 규격에 맞게 변환)
    # 티쳐블 머신 모델은 보통 224x224 이미지를 입력으로 받습니다.
    image = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1 # 정규화 (Normalization)

    # 4. 모델 예측 (Inference)
    prediction = model.predict(image, verbose=0)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # 5. 결과 화면 표시
    label = f"{class_name}: {np.round(confidence_score * 100)}%"
    color = (0, 255, 0) if index == 0 else (0, 0, 255) # 클래스 0(정상)이면 초록색
    
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Teachable Machine - Plant vs Weed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
