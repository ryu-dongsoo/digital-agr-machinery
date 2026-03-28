// ===== [Step 2] 스마트 화분: 비례(P) 제어 시스템 =====
// 오차(목표수분 - 현재수분)에 비례하여 펌프 모터의 회전 속도를 다르게 조절합니다.

// 핀 번호 할당
const int PIN_SENSOR_MOISTURE = A0;   
const int PIN_PWM_PUMP        = 5;    // 모터 속도 제어를 위해 PWM(~) 지원 핀 변경 (릴레이 대신 모터드라이버/트랜지스터 가정)

// 제어기 튜닝 파라미터
const int SETPOINT = 400;      // 목표 수분값 (SP)
const float Kp     = 0.5;      // 비례 이득 (Proportional Gain)

void setup() {
  pinMode(PIN_PWM_PUMP, OUTPUT);
  Serial.begin(9600);
  Serial.println("시스템 부팅 완료: P 제어 모드");
}

void loop() {
  // 1. 현재 센서값 확인
  int currentMoisture = analogRead(PIN_SENSOR_MOISTURE);
  
  // 2. 오차(Error) 계산
  // 센서값이 목표값보다 클 때(건조할 때) 양수(+) 오차 발생
  int error = currentMoisture - SETPOINT;
  
  // 3. P 제어 연산 (Output = Kp * error)
  int output = (int)(Kp * error);
  
  // 4. 출력값 가공 (모터 PWM 범위 0~255 내 강제)
  // 음수(충분히 젖음)이거나 255를 초과하는 수치 절삭 처리
  if (output < 0) {
    output = 0;
  } else if (output > 255) {
    output = 255;
  }
  
  // 5. 액추에이터 구동
  analogWrite(PIN_PWM_PUMP, output);
  
  // 6. 상태 모니터링 (정상 상태 오차 관찰용)
  Serial.print("목표: ");  Serial.print(SETPOINT);
  Serial.print(" | 측정: "); Serial.print(currentMoisture);
  Serial.print(" | 오차: ");   Serial.print(error);
  Serial.print(" | PWM출력: "); Serial.println(output);

  delay(1000);
}
