/*
  wheel_VR_hiddenRewMultTrigRand_esp32_1m_091722c.ino
  from: treadmill_hiddenRewardMultTrigRFIDrand_(date).ino
  Clay 2022

  Using on OpenMaze OMw small PCB
  for VR behavior.
  - Position input from rotary encoder ESP32 on Serial2
  - Solenoid valve control for liquid reward on ULN2803 (or H-bridge)
  - Lick detection with capacitive touch sensor (ESP32 or other)
  - Olfactory stim/airpuff via solenoid valve
  - Zero position on input from VR (via rotary ESP32)
  - Multiple reward position random option (isRandRew)
  - Operant/non on alternate laps option (altOpt)
  

*/


/// VARIABLES TO CHANGE EXPERIMENT PARAMS
String programName = "wheel_VR_hiddenRewMultTrigRand_esp32_1m_092422a";

int rewDur = 100;
int isESP = 1;  // 1 if you're detecting licks with ESP32 touch pins
int isButtonStart = 1;  // this means that prog doesn't print out position data until button is pressed
int isOperant = 1;  // animal has to lick to get reward
int altOpt = 0; // alternate operant on even laps? 
int maxNumZoneRew = 5;//5;
int rewTimeout = 500;//1000; //5000; // timeout for multiple reward licks within a single zone/epoch

int lickThresh = 120;//4;//50; //150; // 5*touch thresh value (for 5 read sum)

// reward vars
int numRew = 1; //8; // number of reward zones (if isRandRew=0, make equal to length rewPosArr) 
int rewWidth = 300;//200;//450;  // width of reward zone
int isRandRew = 0;
int rewPosArr[] = {1500}; //{1500};// {100, 500, 1000, 1500, 2000, 2500, 3000, 3500}; // specify exact positions if isRandRew=0
int rewZoneOptTime = 4000;  //2000; // ms after entering rewZone animal has the option to lick for rew
long interLickInt = 2;  // make really large if you want single lick choice (but might have to use 'long' var)

int trackLength = 2000;//1800;//0;
int startSession = 0;

// for velocity-based reward
int isVelRew = 0;   // reward if animal reaches a certain min velocity (in rotary clicks)
float velThresh = 20;  // for velRew
int velRewTimeout = 2000;

int evPos1 = 900; // olfactory stim params
int evWidth1 = 200;
int prevEv1 = 0;

// mult rew location defaults
int rewPosInds[] = {0, 1, 2, 3, 4, 5, 6, 7}; //,12}; // indices of reward zones (zero based)
int rewPosArrMaster[] = {40, 250, 500, 750, 1000, 1250, 1500, 1750}; //{100, 500, 1000, 1500, 2000, 2500, 3000, 3500}; //, 3600}; // possible start positions of reward zones
int numZones = 8; // the length of rewPosArrMaster

int rollOver = 0; // just to make tolerance for long belt (treadmill)

long rewZoneStartTime = 0;
int rewZone; // = 0;
int prevRewZone = 0;

int numZoneRew = 0;
int lastRewZone = 100;
int numRewZone = 0;

// sync pulse params
int syncDur = 500;  // duration of pulse
int syncIntv = 5000;  // interval of pulse train

////////////////PINS
// Pin numbers
int lickPin = 36;//2;//
//int spkrPin = 47;
int ledPin = 13;
int buttonPin1 = 15;
int trigPin = 2;//12;//26;  // pin for triggering nVista imaging (high during session if isButtonStart)
int syncPin = 33; // pin for nVista sync
int syncPin2 = 25;  // LED for video sync
int solPin1 = 14;//12; //5;
int solPin2 = 32; //6;

int touchPin = T0; // = pin 4, if using esp32 touch sensing

#define RXD2 16 // for Serial2 on ESP32
#define TXD2 17

/////////////////////

// times
long startTime = 0;
long endTime = 0;

//
int currPos = 0;
int prevPos = 0;
int dy = 0;
float vel = 0;

// rotary encoder serial input variables
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

int yInd = 0; // more encoder vars
int mInd = 0;
String dyStr = "";
String msStr = "";
long dt = 0;
long reTime = 0;
long prevReTime = 0;

long syncStartTime = 0; // sync vars
long prevSyncTime = 0;
int prevSync = 0;
long lastSyncTime = 0;

// initialize times and counts
int prevRew = 0;
long rewStartTime = 0;

// lick vars
int prevLick = 0;
long lickTime = 0;
long prevLickTime = 0;
int lickState = 0;
int lickStateArr[6];
int numReading = 0;
int lickStateSum = 0;
int justLicked = 0;  // for MPR

// esp32 lick vars
int touchVal = 0;

long buttonTime = 0;
long prevButtonTime = 0;

int isRewZone = 0;
int rewZoneSum = 0;

int lapNum = 0;

// SETUP ///////////////////
void setup()
{
  // set up pins
  pinMode(lickPin, INPUT);
  //pinMode(spkrPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(solPin1, OUTPUT);
  pinMode(solPin2, OUTPUT);
  pinMode(buttonPin1, INPUT_PULLUP);
  pinMode(syncPin, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(syncPin2, OUTPUT);

  //digitalWrite(solPin1, LOW);

  // Open serial communications (to computer)
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. 
  }

  // set the data rate for the rotary encoder port
  // NOTE: must match the rate of the rotary encoder ESP32
  Serial2.begin(115200, SERIAL_8N1, RXD2, TXD2); // Serial2 on ESP32
  inputString.reserve(200);
  //delay(1000);

  printHeader();

  if (!isESP) {
    lickThresh = 4;
  }

  randomSeed(analogRead(A4));

}  // end SETUP

// start LOOP  ///////////////////////////
void loop() // run over and over
{
  serialEvent1(); // look for input from PC/RasPi via rotary ESP32 (e.g. from Processing start to reprint header)
  
  // read rotary encoder input
  serialEvent2(); // reads movement and runs updatePosition

  // see if you need to turn off reward valve (for any given reward)
  if (prevRew == 1) {
    checkRewState();
  }

  checkLicks();

  //if (isButtonStart == 1) {
    checkButton();
  //}
  if (startSession == 1) {
    checkSyncState();
  }

}  // end LOOP


// SUBFUNCTIONS ////////////////////

// use rotary input to update position (and check if reward zone) every rotary read
void updatePosition() {
  //prevPos = currPos;
  
  // parse serial input from rotary encoder ESP32
  yInd = inputString.indexOf(',');
  dyStr = inputString.substring(0, yInd); //(yInd+4, mInd-3); //strtok(inputString, ","); //
  //    Serial.println(dyStr);
  dy = dyStr.toInt();
  mInd = inputString.indexOf(',', yInd);
  msStr = inputString.substring(mInd, inputString.length() - 1); //(mInd+8, inputString.length()-1);//strtok(NULL, ","); //
  reTime = msStr.toInt(); // rotary encoder arduino time
  dt = reTime - prevReTime;
  prevReTime = reTime;

  vel = dy; //float(dy)/float(dt)*1000;
  currPos = prevPos + dy;
  prevPos = currPos;

  // only print output and check reward zone after track calibrated and session started
  if (startSession == 1) {

    Serial.print("vel=" + String(vel) + ", ");
    Serial.println("currPos=" + String(currPos) + ", ms=" + String(millis()));

    // see if mouse is in any reward zone (but need to change so he can't go back through)
    rewZoneSum = 0;
    for (int i = 0; i < numRew; i++) { // check through all possible reward zones (nb. order not sorted)
      if (currPos >= rewPosArr[i] && currPos <= rewPosArr[i] + rewWidth) { // if currPos is in a rewZone
        rewZone = i; // number of curr rew zone in rewPosArr (nb. order not sorted)
        if (prevRewZone == 0 && rewZone != lastRewZone) { // if new entry into new zone (this prevents re-entry rewards)
          //rewZone = i;
          lastRewZone = i;
          numRewZone = numRewZone+1; // number/index of this reward zone along track this lap (nb. not ind in rewPosArr)
          rewZoneStartTime = millis();
          Serial.println("rewZone=" + String(numRewZone) + ", ms=" + String(rewZoneStartTime));
          //            isRewZone = 1;
          //            prevRewZone = 1;
          //            rewZoneSum = rewZoneSum +1;
          //break;
          
        }
        isRewZone = 1;
        prevRewZone = 1;
        rewZoneSum = rewZoneSum + 1;
      }
    }

    if (rewZoneSum == 0) {  // else if not in any reward zone
      isRewZone = 0;
      prevRewZone = 0;
      numZoneRew = 0;
    }

    if (isVelRew == 0 && isRewZone == 1) {    // for non-operant rewards in rewZone entry
      if (isOperant == 0 && prevRew == 0 && millis() - rewStartTime > rewTimeout && numZoneRew < maxNumZoneRew) {
        prevRew = 1;
        numZoneRew = numZoneRew + 1;
        giveReward();
      }
      //digitalWrite(ledPin, HIGH); // to turn on LED while in rew zone
    }  // end IF in rewZone
    else {
      //digitalWrite(ledPin, LOW);
      isRewZone = 0; // this turns off rewZone if isVelRew
    }

    // if pos is more than estimate of track length, start new lap
    if (currPos >= trackLength + rollOver) {
      lapReset();
    }

    // if isVelRew and vel is high enough, give reward
    if (isVelRew == 1 && vel > velThresh && millis() - rewStartTime > velRewTimeout) {
      giveReward();
      prevRew = 1;
    }

    /////////////olf stim NEW
//    if (currPos >= evPos1 && currPos < evPos1 + evWidth1) {
//      if (prevEv1 == 0) {
//        digitalWrite(solPin2, HIGH);
//        Serial.print("olfOn, ms=");
//        Serial.println(millis());
//        prevEv1 = 1;
//      }
//    }
//    else {
//      if (prevEv1 == 1) {
//        digitalWrite(solPin2, LOW);
//        Serial.print("olfOff, ms=");
//        Serial.println(millis());
//        prevEv1 = 0;
//      }
//    }

    /// ADD NEW POSITION EVENTS HERE
    /// e.g.  if (currPos >= eventPos1 && currPos < eventPos1+zoneWidth) {tone(pin, freq);} else {noTone(pin);}
    ///
    ///

  }
}

////////////////////////////////////////////
////////basic event state check functions
// reward functions
void giveReward() {
  rewStartTime = millis();
  digitalWrite(solPin1, HIGH);
  Serial.print("REWARD, ms=");
  Serial.println(rewStartTime);
  //delay(500);
}

void checkRewState() {
  if (prevRew == 1 && millis() - rewStartTime >= rewDur) {
    digitalWrite(solPin1, LOW);
    prevRew = 0;
  }
}

///////////////////////
void checkButton() { // for button start
  if (digitalRead(buttonPin1) == 0) {
    if (millis() - prevButtonTime > 2000) {
        prevButtonTime = millis();
        Serial.print("exp");
        giveReward();
        prevRew = 1;
      if (startSession == 0) {
        startSession = 1;
        startTime = millis();
        digitalWrite(trigPin, HIGH); // trig stays HIGH whole session after button start
        Serial.print("START SESSION button, ms = ");
        Serial.println(startTime);
        Serial.print("trigTime, ms=");
        Serial.println(startTime);
        prevButtonTime = startTime;

      }
      else {
        startSession = 0;
        endTime = millis();
        digitalWrite(trigPin, LOW);
        digitalWrite(syncPin, LOW);
        digitalWrite(syncPin2, LOW);
        Serial.print("END session button, ms=");
        Serial.println(endTime);
        prevButtonTime = endTime;
      }
    }
  }
}

////////////////////////
void checkSyncState() {
  if (prevSync == 1 && millis() - syncStartTime >= syncDur) {
    digitalWrite(syncPin, LOW);
    digitalWrite(syncPin2, LOW);
    prevSync = 0;
  }
  else if (millis() - lastSyncTime >= syncIntv) {
    digitalWrite(syncPin, HIGH);
    digitalWrite(syncPin2, HIGH);
    syncStartTime = millis();
    Serial.print("syncOut, ms = ");
    Serial.println(syncStartTime);
    lastSyncTime = syncStartTime;
    prevSync = 1;
  }
}


//////////////////////
void checkLicks() {

  if (isESP == 1) { // if using ESP32 touch sensor pin
    touchVal = touchRead(touchPin); // pre-read reduces noise spikes (found this online)
    delayMicroseconds(10);
    touchVal = 60-touchRead(touchPin);//60-touchRead(touchPin); // real read, inverted
  }
  else {
    touchVal = digitalRead(lickPin);
  }
  //Serial.println(touchVal);

  numReading++;

  lickStateSum = lickStateSum + touchVal;

  if (numReading == 5) {  // every 5 readings
    if (lickStateSum > lickThresh) { // if all readings were lick ON
      if (prevLick == 0) { // if new lick
        digitalWrite(ledPin, HIGH);
        prevLick = 1;
        lickTime = millis();
        Serial.print("lick, ms=");
        Serial.println(lickTime);

        // if reward zone lick, giveReward()
        if (isOperant == 1 && isRewZone == 1 && prevRew == 0 && millis() - rewZoneStartTime <= rewZoneOptTime && millis() - rewStartTime > rewTimeout && numZoneRew < maxNumZoneRew) { //  && lickTime-prevLickTime<interLickInt
          prevRew = 1;
          numZoneRew = numZoneRew + 1;
          giveReward();
        }
      }
    }
    else if (lickStateSum == 0) {  //if (prevLick == 1 && lickState == 0 && millis()-lickTime>50) {
      prevLick = 0;
      digitalWrite(ledPin, LOW);
    }
    numReading = 0;
    lickStateSum = 0;
  }

}  // END checkLicks();

/////////////////////////////////////
// to reprint header on Processing start for Processing 4 (which doesn't restart arduino)
void serialEvent1() { // to read serial input from Processing
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
      inputString.trim();

      // reset arduino pos if '0' from VR RasPi
      if (inputString.equals("1")) {
        printHeader();
      }

      // clear the string:
      inputString = "";
      stringComplete = false;

    }
  }
}

/////////////////////////////////////
/* ROTARY ENCODER SERIAL INPUT
  SerialEvent occurs whenever a new data comes in the
  hardware serial RX.  This routine is run between each
  time loop() runs, so using delay inside loop can delay
  response.  Multiple bytes of data may be available.
*/
void serialEvent2() {
  while (Serial2.available()) {
    // get the new byte:
    char inChar = (char)Serial2.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
      inputString.trim();

      // reset arduino pos if '0' from VR RasPi
      if (inputString.equals("0")) {
        lapReset();
      }
      else {
        updatePosition(); // update position and see if this is a reward zone
      }

      // clear the string:
      inputString = "";
      stringComplete = false;

    }
  }
}

//////////////////////////////


///////////////////////

void lapReset() {

  if (currPos>1500) {
    lapNum++;
  }
  
  Serial.print("lapNum=");
  Serial.print(lapNum);
  Serial.print(", ms=");
  Serial.println(millis());

  prevPos = 0;
  prevRew = 0;  // reset reward
  numRewZone = 0; //reset reward zone number at lap
  digitalWrite(solPin1, LOW); // reset reward solenoid output just in case

  if (altOpt==1) {
    if (lapNum%2==0) {
      isOperant=1;
      Serial.print("isOperant=");
      Serial.println(isOperant);
    }
    else {
      isOperant=0;
      Serial.print("isOperant=");
      Serial.println(isOperant);
    }
  }

  // randomize reward positions?
  if (isRandRew == 1) {

    // trick for generating random rewPosInds (switch each index with random other one, so no repeats)
    for (int i = 0; i < numZones; i++) {
      int randInd = random(numZones); // gen random number
      int t = rewPosInds[i];  // load in index
      rewPosInds[i] = rewPosInds[randInd]; // change this index to random other one
      rewPosInds[randInd] = t; // make the random index equal to other one (i.e. switch)
    }

    // now use random reward positions this lap (and print this array)
    Serial.print("rewPosArr={");
    for (int j = 0; j < numRew; j++) {
      rewPosArr[j] = rewPosArrMaster[rewPosInds[j]];
      Serial.print(rewPosArr[j]);
      if (j != numRew - 1) {
        Serial.print(", ");
      }
      else {
        Serial.println("}");
      }
    }
  }
  //      else  {
  //        rewPosArr[0]=rewPos; // added 062222 for single static reward zone
  //      }

  if (numRew == 1) { // resets last rewZone index at lap
    lastRewZone = 100; // just some absurd number so that next rew can activate
  }

}

///////////////////
void printHeader() {
  // Now print out some header information with behavioral program parameters
  Serial.println(programName);
  Serial.println("numRew=" + String(numRew)); // number of reward zones
  Serial.println("rewWidth=" + String(rewWidth));  // width of reward zone
  Serial.println("rewZoneOptTime=" + String(rewZoneOptTime));  // ms after entering rewZone animal has the option to lick for rew
  Serial.println("interLickInt=" + String(interLickInt));  // make really large if you want single lick choice (but might have to use 'long' var)
  Serial.println("rewTimeout=" + String(rewTimeout));

  Serial.print("rewPosArr={");
  for (int i = 0; i < numRew; i++) {
    if (i != numRew - 1) {
      Serial.print(String(rewPosArr[rewPosInds[i]]) + ", ");
    }
    else {
      Serial.print(String(rewPosArr[rewPosInds[i]]));
    }
  }
  Serial.println("}");

  Serial.print("isRandRew=");
  Serial.println(isRandRew);

  Serial.print("rewDur=");
  Serial.println(rewDur);
  Serial.print("isButtonStart=");
  Serial.println(isButtonStart);
  Serial.print("isOperant=");
  Serial.println(isOperant);
  Serial.print("altOpt=");
  Serial.println(altOpt);
  Serial.print("isVelRew=");
  Serial.println(isVelRew);
  Serial.print("velThresh=");
  Serial.println(velThresh);
  Serial.print("ms=");
  Serial.println(millis());
  Serial.println("END HEADER");

  lapNum = 0;
}
