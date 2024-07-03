/*
 * This is from a basic example from the
 * AiEsp32RotaryEncoder library
 * "TheShortestExample"
 * Clay modified for treadmill use by
 * making output in JSON like previous
 * HCTL rotary encoder.
 * Also made hack for rollover.
 * 
 * 081222
 * Changing for VR to output simple (non JSON)
 * 
 */


#include "AiEsp32RotaryEncoder.h"
//#include <ArduinoJson.h>
/////////////////////
#define RXD2 16 // for Serial2 on ESP32
#define TXD2 17
/////////////////////
#define ROTARY_ENCODER_A_PIN 27
#define ROTARY_ENCODER_B_PIN 26
#define ROTARY_ENCODER_BUTTON_PIN 25
#define ROTARY_ENCODER_STEPS 4
AiEsp32RotaryEncoder rotaryEncoder = AiEsp32RotaryEncoder(ROTARY_ENCODER_A_PIN, ROTARY_ENCODER_B_PIN, ROTARY_ENCODER_BUTTON_PIN, -1, ROTARY_ENCODER_STEPS);

/////////////////////////////
//StaticJsonBuffer<200> jsonBuffer;
//JsonObject& message = jsonBuffer.createObject();
//JsonObject& value = message.createNestedObject("position");;
//////////////////////////////

int printInt = 30; // print rotary output every Xms

int dy = 0;
int prevDy = 0;
int val = 0;
int prevVal = 0;
long currT = 0;

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

///////////////////////////
void rotary_onButtonClick()
{
    Serial.println("button pressed");
}

///////////////////////////
void setup()
{
    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, RXD2, TXD2); // Serial2 on ESP32
    
    rotaryEncoder.begin();
    rotaryEncoder.setup(
        [] { rotaryEncoder.readEncoder_ISR(); },
        [] { rotary_onButtonClick(); });
    rotaryEncoder.setBoundaries(0, 1000, true); //minValue, maxValue, circleValues true|false (when max go to min and vice versa)
    rotaryEncoder.setAcceleration(0);

//    value["dy"] = 0;
//    message["millis"] = 0;
}
///////////////////////////
void loop()
{
    if (rotaryEncoder.encoderChanged())
    {
        val = rotaryEncoder.readEncoder();
        //Serial.println(val);
//        prevVal = val;

        currT = millis();
        
        dy = val-prevVal;

        if (dy>=900 || dy<=-900) { // build in catch for rollover (ins prev good val)
          dy = prevDy;
        }

//        // print JSON to main Serial/USB
//        value["dy"]=dy;
//        message["millis"]=currT;
//        message.printTo(Serial);
//        Serial.println();

        Serial.print(dy); Serial.print(","); Serial.println(currT); // or simple to USB

        // print simple to esp32 Serial2
        Serial2.print(dy); Serial2.print(","); Serial2.println(currT);
        
        prevVal = val;
        prevDy = dy;
    }
//    else {
//      Serial.println(prevVal);
//    }
    delay(printInt);

    serialEvent1();
}
/////////////////////////////
// Read data from RasPi VR (Serial2) to reset behav arduino pos
void serialEvent1() {
  while (Serial2.available()) {
    //Serial.println("Reading...");
    // get the new byte:
    char inChar = (char)Serial2.read(); // read RasPi serial
    //Serial.println(inChar);
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
      Serial.print(inputString); // output to behav arduino/esp32

//      // reset arduino pos if '0' from VR RasPi
//      if (inputString.equals("0")) {
//        Serial.println("VR reset");
//        prevPos = 0;
//        prevRew = 0;  // reset reward
//      }
      
      // clear the string:
      inputString = "";
      stringComplete = false;

    }
  }
}
