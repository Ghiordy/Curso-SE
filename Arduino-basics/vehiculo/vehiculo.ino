#include "vehiculo.h"

vehiculo mazda,toyota;

void setup() {
  mazda.SetColor("Verde");
  mazda.SetCilindraje(4.5);
  toyota.SetColor("Negro");
  toyota.SetCilindraje(2.3);
  Serial.begin(9600);
}

void loop() {
  Serial.print(mazda.GetColor());
  Serial.print(",");
  Serial.print(mazda.GetCilindraje);
  Serial.print(",");
  Serial.print(toyota.GetColor);
  Serial.print(",");
  Serial.println(toyota.GetCilindraje);
  Serial.print("Cilindrajes toyota: ")
  for(double i=0;i<10;i++){
    toyota.SetCilindraje(i);
    Serial.print(toyota.GetCilindraje)
    }
}
