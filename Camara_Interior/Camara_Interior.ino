#include <SoftwareSerial.h>

#define Alarma 5
#define Bocina 6



SoftwareSerial Alarma(3, 2); //SIM800L Tx & Rx is connected to Arduino #3 & #2


void getEstado(String SerialPython)
{
  if (SerialPython == "Alarma")
  {
    digitalWrite(Alarma,HIGH);
    digitalWrite(Bocina,HIGH);
    Mensaje();
  }
  else{
    digitalWrite(Alarma,HIGH);
    digitalWrite(Bocina,HIGH);
  }
}

void setup(){
    Alarma.begin(9600);
    Serial.begin(9600);
    pinMode(Alarma,OUTPUT);
    pinMode(Bocina,OUTPUT);
}

void loop(){
  if (!Serial.available())
  {
    getEstado(Serial.readString());
  }
}