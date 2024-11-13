#include "DHTesp.h"
#define BUTTON_P 23 // Fósforo
#define BUTTON_K 13 // Potássio
const int DHT_PIN = 27; //DHT
const int LDR_PIN = 34; //LDR
const int RELAY_PIN = 4; // RELAY

DHTesp dhtSensor;

void setup() {
  pinMode(BUTTON_P, INPUT_PULLUP);
  pinMode(BUTTON_K, INPUT_PULLUP);
  pinMode(RELAY_PIN, OUTPUT);
  Serial.begin(115200);
  dhtSensor.setup(DHT_PIN, DHTesp::DHT22);
}

void loop() {
  int estadoP = digitalRead(BUTTON_P);
  int estadoK = digitalRead(BUTTON_K);

  TempAndHumidity data = dhtSensor.getTempAndHumidity();
  Serial.println("Temp: " + String(data.temperature, 2) + "°C");
  Serial.println("Humidity: " + String(data.humidity, 1) + "%");
  

  int ldrValue = analogRead(LDR_PIN);
  Serial.println("LDR Value: " + String(ldrValue)); 

  if (data.humidity < 30 || estadoP == LOW || estadoK == LOW || ldrValue > 2300) {
    digitalWrite(RELAY_PIN, HIGH);
    Serial.println("Bomba ligada.");
  } else {
    digitalWrite(RELAY_PIN, LOW); 
    Serial.println("Bomba desligada.");
  }

  delay(2000);

}
