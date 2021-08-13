//STM_encoder Hongtao Cai Columbia University 6/25/2021


//--- DEFINE ---
const    int   LED_PIN         = 13;
const    int   Encoder_PinA    = 2;
const    int   Encoder_PinB    = 3;
volatile float EnCoderPos      = 0;
         float currPos;
         float oldPos          = 0;
unsigned long currTime;
unsigned long oldTime    = 0;

         float velocity_angle = 1;
         float velocity;
         float distance;
         float S_time;
         float radius  = 0.07; //7cm 

         int currDigA;
         int currDigB;
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

  //speed calculation
  distance = currPos - oldPos;
  S_time = currTime - oldTime;
  velocity_angle = ((float)(distance));
  
  oldPos  = currPos;
  oldTime = currTime;
  Serial.println(velocity_angle);
  
  delay(50);   
}

//clockwise A != B dy positive;    counterclockwise A == B  dy negative
void EnCoder_Position()
{
   currDigA = digitalRead(Encoder_PinA);
   if (currDigA != oldDigA)
   {
      if (currDigA == !digitalRead(Encoder_PinB))
      {
        EnCoderPos = EnCoderPos + 1;
        //Serial.println("clockwise");
      }
      else if (currDigA == digitalRead(Encoder_PinB))
      {
        EnCoderPos = EnCoderPos - 1; 
        //Serial.println("countclockwise");
      }
   }
   oldDigA = currDigA;
 
}