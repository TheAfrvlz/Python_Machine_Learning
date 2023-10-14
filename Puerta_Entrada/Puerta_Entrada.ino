#include <Servo.h>
#include <Adafruit_NeoPixel.h>
#include <avr/power.h>
#include <SoftwareSerial.h>

#define Puerta_Estado 9
#define Indicador 6
#define Led_Size 2
SoftwareSerial Puerta_alarma(3, 2);
Adafruit_NeoPixel pixels(Led_Size, Indicador, NEO_GRB + NEO_KHZ800);
Servo Puerta;


void llamada() {
  // Begin serial communication with Arduino and SIM800L
  Puerta_alarma.begin(9600);

  Serial.println("Initializing...");
  delay(1000);

  Puerta_alarma.println("AT"); // Once the handshake test is successful, i t will back to OK


  Puerta_alarma.println("ATD+ +522227142973;"); // change ZZ with country code and xxxxxxxxxxx with phone number to dial

  delay(20000);            // wait for 20 seconds...
  Puerta_alarma.println("ATH"); // hang up

}

void setup()
{
  Serial.begin(9600);
  Puerta_alarma.begin(9600);
  Serial.print("Inicio Reconocimiento");
  pixels.begin();
  pixels.clear();
  Puerta.attach(Puerta_Estado);
}

void loop()
{
  if (Serial.available())
  {
    char SerialPython = Serial.read();
    if (SerialPython == 'P')
    {
      Puerta.write(80);
      for(int i=0;i<Led_Size;i++){
       pixels.setPixelColor(i, pixels.Color(0, 250, 0));
      }
      pixels.show(); 
    }
    if (SerialPython == 'N')
    {
      Puerta.write(0);
      for(int i=0;i<Led_Size;i++){
       pixels.setPixelColor(i, pixels.Color(250, 0, 0));
      }
      pixels.show(); 
      
    }
    if (SerialPython == 'A')
    {
      Puerta.write(0);
      for(int i=0;i<Led_Size;i++){
       pixels.setPixelColor(i, pixels.Color( 255, 195, 0 ));
      }
      pixels.show(); 
      delay(1000);
      for(int i=0;i<Led_Size;i++){
       pixels.setPixelColor(i, pixels.Color(0,0,0));
      }
      pixels.show(); 
      delay(1000);
      for(int i=0;i<Led_Size;i++){
       pixels.setPixelColor(i, pixels.Color( 255, 195, 0 ));
      }
      pixels.show(); 
      delay(1000);
      for(int i=0;i<Led_Size;i++){
       pixels.setPixelColor(i, pixels.Color(0,0,0));
      }
      pixels.show(); 
      delay(1000);
      llamada();
    }
  }
}
