#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8);  

//  radio :  Arduino
// ===================
//   V+   :  3.3V
//   GND  :  GND
//   CSN  :  Pin 8 
//   CE   :  Pin 7
//   MOSI :  Pin 11
//   SCK  :  Pin 13
//   MISO :  Pin 12
//   IRQ  :  No Connection

#include <ArduinoJson.h>

const byte address[][6] = { "00001", "00002", "00003" };
int num = 1;

// const uint8_t* json = "{\"roomID\":23,\"occupied\":1}";


char json[128];


void setup() {
    Serial.begin(9600);
    radio.begin();
    radio.openWritingPipe(address[0]);
    radio.setPALevel(RF24_PA_MIN);


    const size_t capacity = JSON_OBJECT_SIZE(2);
    DynamicJsonDocument doc(capacity);

    doc["roomID"] = 23;
    doc["occupied"] = 1;

    serializeJson(doc, json);
}

void loop() {
  radio.write(json, strlen(json));
  Serial.print("Sent: ");
  Serial.print(num++);
  Serial.print("\tSize: ");
  Serial.println(strlen(json));
  delay(1000);
}

