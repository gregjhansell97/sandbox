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
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}
void loop() {
  Serial.println("sending");
  HiveMsg m = {2, "hello world\0"};
  //const char text[] = "Hello World";
  radio.write(&m, sizeof(m));
  delay(1000);
}
