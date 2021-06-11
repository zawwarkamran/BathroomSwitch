#include <ESP8266WiFi.h>
#include <aREST.h>

// D7 is the PIR sensor so we define the pin there
int PIRsensor = 13;
int motion = 0;

// Create the aREST instance
aREST rest = aREST();

#define LISTEN_PORT           80

WiFiServer server(LISTEN_PORT);

void setup(void) {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(PIRsensor, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin(9600);

  rest.variable("motion",&motion);
  rest.set_id("1");
  rest.set_name("motion_sensor_module");
  
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
  server.begin();
  Serial.println("server started");
  }
  
//void loop() {
//  Serial.println(WiFi.localIP());
//}


void loop() {

  long state = digitalRead(PIRsensor);
  
  if (state == HIGH){
    Serial.println("motion");
    digitalWrite(LED_BUILTIN, LOW);
    motion = 1;
    }
    else {
      Serial.println("no motion");
      digitalWrite(LED_BUILTIN, HIGH);
      motion = 0;
    }
    
  WiFiClient client = server.available();
  if (!client) {
  return;
  }
  while(!client.available()){
  delay(1);
  }
  rest.handle(client);
}
