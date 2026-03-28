// ===== [Step 3] 스마트 화분: 비례-적분(PI) 제어 시스템 =====
// P 제어의 정상 상태 오차(미세하게 목표치에 영원히 도달하지 못하는 문제)를
// 과거 오차의 누적합(적분, Integral)으로 극복합니다.

// 핀 번호 할당
const int PIN_SENSOR_MOISTURE = A0;   
const int PIN_PWM_PUMP        = 5;    

// 제어기 튜닝 파라미터 지표
const int SETPOINT = 400;      // 목표 수분값 (SP)
const float Kp     = 0.5;      // 비례 이득
const float Ki     = 0.05;     // 적분 이득 (매초 누적되므로 작게 설정)

// 시스템 상태 변수 보관용
float integralSum = 0;         // 오차 누적합 변수
unsigned long lastTime = 0;    // 시간 편차 연산용

void setup() {
  pinMode(PIN_PWM_PUMP, OUTPUT);
  Serial.begin(9600);
  Serial.println("시스템 부팅 완료: PI 제어 모드");
}

void loop() {
  // 경과 시간 계산 연산 (dt)
  unsigned long currentTime = millis();
  float dt = (currentTime - lastTime) / 1000.0; // 밀리초 -> 초 단위 변환
  lastTime = currentTime;

  if (dt <= 0) return; // 첫 루프 등 시간차 0인 구간 방어

  // 1. 센서값 읽기
  int currentMoisture = analogRead(PIN_SENSOR_MOISTURE);
  int error = currentMoisture - SETPOINT;
  
  // 적분 조건부 계산 (건조할 때만 누적, 오차가 음수(너무 습함)이면 0으로 초기화)
  // 인테그럴 와인드업(Integral Windup) 억제 방지 기법
  if (error > 0) {
    integralSum += (error * dt);
  } else {
    integralSum = 0; 
  }

  // 2. PI 연산식 통합
  float p_term = Kp * error;
  float i_term = Ki * integralSum;
  int output = (int)(p_term + i_term);
  
  // 3. 출력 제한 설정 (0 ~ 255)
  if (output < 0) output = 0;
  if (output > 255) output = 255;
  
  // 4. 액추에이터 구동
  analogWrite(PIN_PWM_PUMP, output);
  
  // 5. 시계열 모니터링 출력
  Serial.print("측정: "); Serial.print(currentMoisture);
  Serial.print(" | 오차: "); Serial.print(error);
  Serial.print(" | P항: "); Serial.print(p_term, 1);
  Serial.print(" | I항: "); Serial.print(i_term, 1);
  Serial.print(" | 최종출력: "); Serial.println(output);

  delay(1000); // 1초 대기
}
