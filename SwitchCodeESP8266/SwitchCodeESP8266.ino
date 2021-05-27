int PIRsensor = 13;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(PIRsensor, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  long state = digitalRead(PIRsensor);
  if (state == HIGH){
    Serial.println("motion");
    digitalWrite(LED_BUILTIN, HIGH);
    }
    else {
      Serial.println("no motion");
      digitalWrite(LED_BUILTIN, LOW);
    }
}
