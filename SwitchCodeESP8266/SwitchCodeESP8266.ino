#include <ESP8266WiFi.h>

int PIRsensor = 13;
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(PIRsensor, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  WiFi.begin("edbtz", "sajwarcho202");

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
}
//void loop() {
//  Serial.println(WiFi.localIP());
//}
void loop() {
  long state = digitalRead(PIRsensor);
  if (state == HIGH){
    Serial.println("motion");
    digitalWrite(LED_BUILTIN, LOW);
    }
    else {
      Serial.println("no motion");
      digitalWrite(LED_BUILTIN, HIGH);
    }
}
