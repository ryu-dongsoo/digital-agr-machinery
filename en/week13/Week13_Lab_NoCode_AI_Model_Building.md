# Week 13 Lab: Building a Crop/Weed Detection Model using No-Code AI

## 📺 Reference Video
- **Recommended**: [Google Teachable Machine Guide](https://youtu.be/T2qQGqZxkD0)
- Please watch the video before the lab to familiarize yourself with the data collection and training interface.

---

## 🎯 Lab Overview
- **Objective**: Skip the complex implementation process of deep learning architectures (CNN) and build an AI model that distinguishes between crops and weeds in real-time using a web browser-based no-code tool.
- **Lab Format**: Image Classification model training using Google Teachable Machine
- **Key Concepts**: Class Definition, Data Collection (Webcam), Hyperparameters (Epoch, Batch), Real-time Inference

---

## 🛠 [Step 1] Lab Preparation and Environment Access
1. Make sure your laptop's **Webcam** is working properly.
2. Open the Chrome browser and go to the [Teachable Machine](https://teachablemachine.withgoogle.com/train/image) website.
3. Click the `Get Started` button and select `Image Project` -> `Standard image model`.

---

## 📸 [Step 2] Dataset Construction
The performance of agricultural AI is determined by the quality of the data. Define the three classes below and collect data.

1. **Class 1 (Normal Crop)**: 
   - Show actual plants or flower leaves in front of the webcam.
   - Press the `Hold to Record` button to capture more than 200 images from various angles, distances, and directions.
2. **Class 2 (Weed Proxy)**: 
   - Prepare an object to assume as a weed (e.g., colored paper model, pen, or a different kind of leaf).
   - Collect data so that features clearly distinguishable from the crop are revealed.
3. **Class 3 (Background)**: 
   - Capture an empty background without any objects. (To prevent the model from mistaking an empty screen for a specific class)

---

## ⚙️ [Step 3] Model Training
This is the process of training the neural network based on the collected data.

1. Click the `Train Model` button.
2. **Adjust Advanced Settings**:
   - **Epochs**: Set how many times the model will repeatedly learn the entire dataset. (Default: 50)
   - **Batch Size**: The size of the image batch to learn at one time.
3. Do not close the browser tab or switch to another window while training is in progress.

---

## 🎯 [Step 4] Real-time Inference and Performance Test
When training is complete, a real-time webcam screen will appear in the `Preview` window on the right.

1. **Check Recognition Rate**: Alternately show the crop and weed models and check if the probability bar graph at the bottom moves accurately.
2. **Edge Case Test**: 
   - Partially cover a leaf with your hand. (Occlusion situation)
   - Turn off or dim the lighting to observe the change in recognition rate.
   - Show a new, untrained object and see how the model judges it.

---

## 💻 [Step 5] [Advanced] YOLO Real-time Object Detection Experience (`step0_yolo_vision_test.py`)
Run YOLOv8, the state-of-the-art object detection algorithm learned in the 2nd session, in a Python environment. Check the performance of the AI recognizing potted plants without separate training.

1. Install the required libraries in the terminal.
   ```bash
   pip install ultralytics opencv-python
   ```
2. Run `step0_yolo_vision_test.py` and show various objects in front of the webcam.

---

## 💻 [Step 6] [Advanced] Porting the Trained Model to Python (`step1_tm_model_load.py`)
Learn how to bring the "no-code model" made in Teachable Machine into actual "Python code" and run it.

1. Click the `Export Model` button at the top right of Teachable Machine.
2. Select `Tensorflow` -> `Keras` and click `Download my model`.
3. Copy the `keras_model.h5` and `labels.txt` files inside the downloaded zip file into the current lab folder (`week13/`).
4. Run `step1_tm_model_load.py` to check if the model you made works properly in Python.

---

## 📝 [Step 7] Result Analysis and Report Writing
Write the [Week 13 Lab Report] based on the lab results. Be sure to include answers to the following questions.

- **Data Bias**: When a specific object (e.g., my finger) continues to be captured in the background, does the phenomenon of judging it as a weed just by looking at that object occur?
- **Generalization Performance**: Does the model guess correctly when shown another plant that 'looks similar' to the plant I trained?
- **Field Application**: If this model is mounted on an actual autonomous spraying robot (See & Spray), what additional sensors or lighting devices would be needed?

---

### 💡 Tips
- If the model's performance is low, try collecting more data or making the background simpler.
- Models completed in Teachable Machine can be exported in the form of **TensorFlow.js** or **Keras(.h5)** through the `Export Model` button and mounted on actual apps or hardware.
