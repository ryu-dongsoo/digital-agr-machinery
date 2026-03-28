// ===== [Step 1] Smart Pot: On/Off Control System =====
// Turns the pump ON when soil is dry, OFF when sufficiently moist.

// Pin assignments (Hardware PinMap)
const int PIN_SENSOR_MOISTURE = A0;   // Soil moisture sensor (analog input)
const int PIN_RELAY_PUMP      = 7;    // Water pump relay control
const int PIN_LED_GREEN       = 3;    // Normal status (sufficient) LED
const int PIN_LED_RED         = 4;    // Warning status (dry) LED

// Control thresholds (with Hysteresis)
// Note: In Tinkercad, higher sensor values indicate drier soil (increased resistance)
const int THRESHOLD_DRY  = 500;  // Above 500 = very dry (start irrigation)
const int THRESHOLD_WET  = 350;  // Below 350 = sufficiently moist (stop irrigation)

void setup() {
  // Configure pin I/O modes
  pinMode(PIN_RELAY_PUMP, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_LED_RED, OUTPUT);
  
  // Initialize serial communication (for PC monitoring)
  Serial.begin(9600);
  Serial.println("System boot complete: On/Off Control Mode");
}

void loop() {
  // 1. Read sensor data (PV: Process Variable)
  int currentMoisture = analogRead(PIN_SENSOR_MOISTURE);
  
  // 2. Monitoring output
  Serial.print("Current moisture sensor value: ");
  Serial.println(currentMoisture);

  // 3. Control logic (On/Off)
  if (currentMoisture > THRESHOLD_DRY) {
    // Dry condition: Pump ON, Red LED warning
    digitalWrite(PIN_RELAY_PUMP, HIGH);
    digitalWrite(PIN_LED_RED, HIGH);
    digitalWrite(PIN_LED_GREEN, LOW);
  }
  else if (currentMoisture < THRESHOLD_WET) {
    // Adequate moisture: Pump OFF, Green LED normal
    digitalWrite(PIN_RELAY_PUMP, LOW);
    digitalWrite(PIN_LED_RED, LOW);
    digitalWrite(PIN_LED_GREEN, HIGH);
  }
  // Note: In the dead band between THRESHOLD_WET and THRESHOLD_DRY,
  // the current pump state is maintained to prevent chattering.

  // Sensing loop at 1-second interval
  delay(1000);
}
