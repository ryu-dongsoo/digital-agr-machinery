// ===== [Step 3] Smart Pot: Proportional-Integral (PI) Control System =====
// Overcomes the steady-state error of P control by accumulating past errors
// through integration (Integral term).

// Pin assignments
const int PIN_SENSOR_MOISTURE = A0;   
const int PIN_PWM_PUMP        = 5;    

// Controller tuning parameters
const int SETPOINT = 400;      // Target moisture value (SP)
const float Kp     = 0.5;      // Proportional Gain
const float Ki     = 0.05;     // Integral Gain (small since it accumulates every second)

// System state variables
float integralSum = 0;         // Accumulated error sum
unsigned long lastTime = 0;    // For time delta computation

void setup() {
  pinMode(PIN_PWM_PUMP, OUTPUT);
  Serial.begin(9600);
  Serial.println("System boot complete: PI Control Mode");
}

void loop() {
  // Calculate elapsed time (dt)
  unsigned long currentTime = millis();
  float dt = (currentTime - lastTime) / 1000.0; // milliseconds -> seconds
  lastTime = currentTime;

  if (dt <= 0) return; // Guard against zero time delta on first loop

  // 1. Read sensor value
  int currentMoisture = analogRead(PIN_SENSOR_MOISTURE);
  int error = currentMoisture - SETPOINT;
  
  // Conditional integration (accumulate only when dry; reset when too wet)
  // Anti-windup technique to prevent Integral Windup
  if (error > 0) {
    integralSum += (error * dt);
  } else {
    integralSum = 0; 
  }

  // 2. PI control computation
  float p_term = Kp * error;
  float i_term = Ki * integralSum;
  int output = (int)(p_term + i_term);
  
  // 3. Output clamping (0-255)
  if (output < 0) output = 0;
  if (output > 255) output = 255;
  
  // 4. Actuator drive
  analogWrite(PIN_PWM_PUMP, output);
  
  // 5. Time-series monitoring output
  Serial.print("PV: ");       Serial.print(currentMoisture);
  Serial.print(" | Error: "); Serial.print(error);
  Serial.print(" | P: ");     Serial.print(p_term, 1);
  Serial.print(" | I: ");     Serial.print(i_term, 1);
  Serial.print(" | Output: "); Serial.println(output);

  delay(1000);
}
