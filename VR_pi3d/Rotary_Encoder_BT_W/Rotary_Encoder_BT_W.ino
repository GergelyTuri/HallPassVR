#include "AiEsp32RotaryEncoder.h"
#include "BluetoothSerial.h"
#include "esp_bt_device.h"
#include <ArduinoJson.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#define ROTARY_ENCODER_A_PIN 26
#define ROTARY_ENCODER_B_PIN 27
#define ROTARY_ENCODER_BUTTON_PIN 25
#define ROTARY_ENCODER_STEPS 4
AiEsp32RotaryEncoder rotaryEncoder = AiEsp32RotaryEncoder(ROTARY_ENCODER_A_PIN, ROTARY_ENCODER_B_PIN, ROTARY_ENCODER_BUTTON_PIN, -1, ROTARY_ENCODER_STEPS);


StaticJsonBuffer<200> jsonBuffer;
JsonObject& message = jsonBuffer.createObject();
JsonObject& value = message.createNestedObject("position");;

BluetoothSerial SerialBT;

int dy = 0;
int prevDy = 0;
int val = 0;
int prevVal = 0;

void rotary_onButtonClick()
{
    Serial.println("button pressed");
}

void printdeviceaddress()
{
  //Serial.print("start from here");
  const uint8_t* point = esp_bt_dev_get_address();
  for (int i = 0; i <6 ; i++)
  {
    char str[3];
    sprintf(str, "%02X", (int)point[i]);
    Serial.print(str);

    if (i < 5){
      Serial.print(":");
    }

  }
}


void setup()
{
    Serial.begin(115200);
    SerialBT.begin("ESP32test"); //Bluetooth device name
    
    rotaryEncoder.begin();
    rotaryEncoder.setup(
        [] { rotaryEncoder.readEncoder_ISR(); },
        [] { rotary_onButtonClick(); });
    rotaryEncoder.setBoundaries(0, 1000, true); //minValue, maxValue, circleValues true|false (when max go to min and vice versa)
    rotaryEncoder.setAcceleration(0);

    value["dy"] = 0;
    message["millis"] = 0;

    Serial.println("The device started, now you can pair it with bluetooth!");
    Serial.print("BT Mac: ");
    printdeviceaddress();
    Serial.println();
}

void loop()
{
    if (rotaryEncoder.encoderChanged())
    {
        val = rotaryEncoder.readEncoder();
        //Serial.println(val);
//        prevVal = val;

        dy = val-prevVal;

        if (dy>=900 || dy<=-900) {
          dy = prevDy;
          value["dy"]=dy;
        }
        else {value["dy"]=val-prevVal;}
        message["millis"]=millis();
        message.printTo(SerialBT);
        message.printTo(Serial);
        SerialBT.println();
        Serial.println();
//        Serial.println(val);
        prevVal = val;
        prevDy = dy;
    }
//    else {
//      Serial.println(prevVal);
//    }
    //
    delay(25);
}
