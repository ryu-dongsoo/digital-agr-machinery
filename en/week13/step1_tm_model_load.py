import cv2
import numpy as np
# tensorflow and keras installation required (pip install tensorflow)
from tensorflow.keras.models import load_model

# 1. Load model and labels
# The files downloaded as 'Tensorflow -> Keras' from Teachable Machine must be in the same folder.
try:
    model = load_model("keras_model.h5", compile=False)
    class_names = open("labels.txt", "r", encoding="utf-8").readlines()
except:
    print("[Error] keras_model.h5 or labels.txt file not found.")
    print("Please export the model from Teachable Machine and copy it to the lab folder.")
    exit()

# 2. Connect webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # 3. Image preprocessing (Convert to fit the model input specifications)
    # Teachable Machine models usually take 224x224 images as input.
    image = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1 # Normalization

    # 4. Model Prediction (Inference)
    prediction = model.predict(image, verbose=0)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # 5. Display result screen
    label = f"{class_name}: {np.round(confidence_score * 100)}%"
    color = (0, 255, 0) if index == 0 else (0, 0, 255) # Green if class 0 (Normal)
    
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Teachable Machine - Plant vs Weed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
