#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8);

const byte address[6] = "00001";

struct HiveMsg {
  byte x;
  char text[32];
};

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    Serial.println("Recieved...");
    HiveMsg m;
    radio.read(&m, sizeof(m));
    Serial.println(m.x);
    Serial.println(m.text);
  }
}
