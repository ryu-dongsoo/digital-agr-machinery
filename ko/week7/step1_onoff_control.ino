// ===== [Step 1] 스마트 화분: On/Off 제어 시스템 =====
// 토양이 건조하면 펌프를 켜고, 충분히 젖으면 펌프를 끕니다.

// 핀 번호 할당 (Hardware PinMap)
const int PIN_SENSOR_MOISTURE = A0;   // 토양 수분 센서 아날로그 입력
const int PIN_RELAY_PUMP      = 7;    // 워터 펌프 릴레이 제어 핀
const int PIN_LED_GREEN       = 3;    // 정상 상태 (충분) LED
const int PIN_LED_RED         = 4;    // 경고 상태 (건조) LED

// 제어 설정 임계값 (Hysteresis 적용)
// 참고: Tinkercad 센서는 값이 클수록 건조함(저항 증가)을 의미하는 경우가 많음
const int THRESHOLD_DRY  = 500;  // 500 이상이면 매우 건조함 (관수 시작)
const int THRESHOLD_WET  = 350;  // 350 이하이면 충분히 젖음 (관수 중지)

void setup() {
  // 핀 입출력 모드 설정
  pinMode(PIN_RELAY_PUMP, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_LED_RED, OUTPUT);
  
  // 시리얼 통신 초기화 (PC 모니터링용)
  Serial.begin(9600);
  Serial.println("시스템 부팅 완료: On/Off 제어 모드");
}

void loop() {
  // 1. 센서 데이터 취득 (PV: Process Variable)
  int currentMoisture = analogRead(PIN_SENSOR_MOISTURE);
  
  // 2. 모니터링 출력
  Serial.print("현재 수분 센서 값: ");
  Serial.println(currentMoisture);

  // 3. 제어 로직 (On/Off)
  if (currentMoisture > THRESHOLD_DRY) {
    // 건조 시 제어: 펌프 ON, 적색 경고
    digitalWrite(PIN_RELAY_PUMP, HIGH);
    digitalWrite(PIN_LED_RED, HIGH);
    digitalWrite(PIN_LED_GREEN, LOW);
  }
  else if (currentMoisture < THRESHOLD_WET) {
    // 적정 습도 시 제어: 펌프 OFF, 녹색 정상 표시
    digitalWrite(PIN_RELAY_PUMP, LOW);
    digitalWrite(PIN_LED_RED, LOW);
    digitalWrite(PIN_LED_GREEN, HIGH);
  }
  // ※ THRESHOLD_WET ~ THRESHOLD_DRY 사이 구간에서는 
  // 현재 펌프 상태(유지)를 변경하지 않음으로써 채터링 현상 방지

  // 1초 주기로 센싱 루프 실행
  delay(1000);
}
