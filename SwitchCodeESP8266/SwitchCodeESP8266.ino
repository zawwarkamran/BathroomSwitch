#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

// D7 is the PIR sensor so we define the pin there
int PIRsensor = 13;
int motion = 0;
WiFiClient wifiClient;

void setup(void) {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(PIRsensor, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin(9600);

  HTTPClient http;
  http.begin(wifiClient,"http://192.168.2.228:5000/a");
  
  WiFi.begin("edbtz", "sajwarcho202");
  WiFi.hostname("ESP8266Bathroom");

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("server started");
  }

void loop() {

  long state = digitalRead(PIRsensor);
  
  if (state == HIGH){
    Serial.println("motion");
    digitalWrite(LED_BUILTIN, LOW);
    http.GET();
    delay(1000);
    }

    else{
    Serial.println("no motion");
    digitalWrite(LED_BUILTIN, HIGH);
    }
}
