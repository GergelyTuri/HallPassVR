//STM_encoder Hongtao Cai Columbia University


//--- DEFINE ---
const int LED_PIN        = PC13;
const int Encoder_PinA   = PB6;
const int Encoder_PinB   = PB7;

volatile float EnCoderPos = 0;
float currPos;
float oldPos = 0;

unsigned long currTime;
unsigned long oldTime    = 0;

float velocity_angle = 1;
float velocity;
float distance;
float S_time;
float radius  = 0.07; //7cm 

int currDigA;
int oldDigA              = 0;



// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(38400);
  // initialize digital pin PB1 as an output.
  pinMode(LED_PIN, OUTPUT);
  pinMode (Encoder_PinA, INPUT);
  pinMode (Encoder_PinB, INPUT);
  //WRITE INPUT DATA
  digitalWrite (Encoder_PinA, HIGH);
  digitalWrite (Encoder_PinB, HIGH);

  Serial.println("Check, start here");

  attachInterrupt(digitalPinToInterrupt(Encoder_PinB),EnCoder_Position,CHANGE); 

  
}

// the loop function runs over and over again forever
void loop() {
  currPos  = EnCoderPos;
  currTime = millis();

  //Serial.println(currPos);

  //Serial.println(currTime);
  
  //speed calculation
  distance = currPos - oldPos;
  S_time = currTime - oldTime;
  velocity_angle = ((float)(distance))
 
  //Serial.println(currPos);
  //Serial.println(oldPos);
  Serial.println(velocity_angle);

  oldPos  = currPos;
  oldTime = currTime;


  delay(50);
  
   
}


//clockwise A != B dy positive;    counterclockwise A == B  dy negative
void EnCoder_Position()
{
   //Serial.println("call from Encoder_Position");
   currDigA = digitalRead(Encoder_PinA);
   if (currDigA != oldDigA)
   {
      if (currDigA == !digitalRead(Encoder_PinB))
      {
        EnCoderPos = EnCoderPos + 1;
      }

      else if (currDigA == digitalRead(Encoder_PinB))
      {
        EnCoderPos = EnCoderPos - 1; 
      }
   }
   oldDigA = currDigA;
}

