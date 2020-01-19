/**
 * Project: Recycle Right - Womxn/Hacks 2.0
 * Created by: Monica Aguilar
 * Date: Jan. 18, 2020
 */
 
#include <LiquidCrystal.h>

//Instance variables
LiquidCrystal lcd(12,11,5,4,3,2);
int greenLED = 9;
int yellowLED = 8;
int redLED = 6;
int buttonReady = LOW;
int button = 7;
char photoResult[10];
int randomNum = 0;

void setup() {
  Serial.begin(9600);
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  lcd.begin(16,2);
  displayTitle();
  pinMode(button, INPUT_PULLUP);
  digitalWrite(button, HIGH);
  randomSeed(350);
}

void loop() {
  displayTitle();
  delay(100);
  buttonReady = digitalRead(button);

  //Checks if button was pressed
  if (buttonReady == LOW){
    //showing testing phase
    activateYellow();
    //
    lcd.clear();
    lcd.print("[Item type here]");
    lcd.setCursor(0,1);

    //for testing purposes
    tester();
    
    buttonReady = HIGH;
    lcd.clear();
  }
}
//Reseting the title
void displayTitle(){
  lcd.clear();
  lcd.begin(16,2);
  lcd.print("Press button to");
  lcd.setCursor(0,1);
  lcd.print("take picture.");
}
// Taking in information
void activateYellow(){
  lcd.clear();
  digitalWrite(yellowLED, HIGH);
  lcd.print("Taking photo...");
  delay(2000);
  //photoResult = photo stuff; see recvInfo()?
  lcd.clear();
  lcd.print("Analyzing...");
  delay(2000);
  digitalWrite(yellowLED, LOW);
}
// Product is not recyclable
void activateRed(){
  digitalWrite(redLED, HIGH);
   lcd.print("Do not recycle!");
   delay(4000);
   digitalWrite(redLED, LOW);
   lcd.clear();
}
// Product is recyclable
void activateGreen(){
  digitalWrite(greenLED, HIGH);
  lcd.print("Recycle!");
  delay(4000);
  digitalWrite(greenLED, LOW);
}

// Generates a random number to randomly pick an option
void tester(){
  randomNum = random(2,4);
  if (randomNum == 2)
    activateGreen();
  else
    activateRed();
}
