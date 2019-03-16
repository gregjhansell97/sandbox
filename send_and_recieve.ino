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

const byte address[][6] = { "00001", "00002", "00003" };
int num = 1;

char roomID[] = "02-1920";
int max_occ = 4;
char input[32] = "";


void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  radio.begin();
  radio.openWritingPipe(address[0]);// other transmitter/reciever has swapped addresses
  radio.openReadingPipe(1, address[1]);
  radio.setPALevel(RF24_PA_MIN);
  //radio.stopListening();
}

void loop() {
  // 
  radio.stopListening();
  radio.write(&roomID, sizeof(roomID));
  Serial.print("Sent: ");
  Serial.println(num++);
  delay(1000);

  radio.startListening();
  while(!radio.available());
  radio.read(input, sizeof(input));
  Serial.println(input);

  checkBT();
}

int checkBT()
{
  if(Serial1.available())
  {
    Serial1.read(input, sizeof(input));
    if(strcmp(input, "help") == 0)
    {
      Serial1.println("1: Get Room ID");
      Serial1.println("2: Change Room ID");
      Serial1.println("3: Get Max Occupancy");
      Serial1.println("4: Change Max Occupancy");
    }
    else if (strcmp(input, "") == 0)
    {
      
    }
    else if (strcmp(input, "") == 0)
    {
      
    }
    return 0;// Bluetooth information recieved
  }
  else
  {
    return 1;// no Bluetooth Information
  }
  
}

