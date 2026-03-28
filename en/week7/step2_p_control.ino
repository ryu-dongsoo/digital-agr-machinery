// ===== [Step 2] Smart Pot: Proportional (P) Control System =====
// Adjusts motor speed proportionally to the error (target moisture - current moisture).

// Pin assignments
const int PIN_SENSOR_MOISTURE = A0;   
const int PIN_PWM_PUMP        = 5;    // PWM-capable pin for motor speed control

// Controller tuning parameters
const int SETPOINT = 400;      // Target moisture value (SP)
const float Kp     = 0.5;      // Proportional Gain

void setup() {
  pinMode(PIN_PWM_PUMP, OUTPUT);
  Serial.begin(9600);
  Serial.println("System boot complete: P Control Mode");
}

void loop() {
  // 1. Read current sensor value
  int currentMoisture = analogRead(PIN_SENSOR_MOISTURE);
  
  // 2. Calculate Error
  // Positive error when sensor value exceeds setpoint (dry condition)
  int error = currentMoisture - SETPOINT;
  
  // 3. P Control computation (Output = Kp * error)
  int output = (int)(Kp * error);
  
  // 4. Clamp output to PWM range (0-255)
  if (output < 0) {
    output = 0;
  } else if (output > 255) {
    output = 255;
  }
  
  // 5. Actuator drive
  analogWrite(PIN_PWM_PUMP, output);
  
  // 6. Status monitoring (observe steady-state error)
  Serial.print("SP: ");      Serial.print(SETPOINT);
  Serial.print(" | PV: ");   Serial.print(currentMoisture);
  Serial.print(" | Error: "); Serial.print(error);
  Serial.print(" | PWM: ");   Serial.println(output);

  delay(1000);
}
