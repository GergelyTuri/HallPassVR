/**
 * VRwheel_RecGraphSerialTxt_110622
 * 
 * This sketch uses a PrintWriter object to write serial data from the Arduino continuously to a file
 * over the course of a behavioral session. After the end of this period, the file closes
 * itself and the program is stopped (or press 'q' while plot window selected). 

 - Required libraries (none)
 **/

/////// Trial variables

String animal = "110622_mouseName1";  // mouse name (change for each mouse; becomes file name)      
int sessionMinutes = 20;
String serialPort = "/dev/ttyUSB1"; //"COM41";  // serial port number for behavior ESP32 on your PC
int trackLen = 2000;//1800;

// plotting vars
int binsize = 30000; // size of time bins in plot (ms)
int rewWidth = 200; // just for plotting reward zones (no effect on actual zones)
int toPlot = 1;

// change plot scales if desired
int plot1scale = 1; //5; // plot 1 scale, etc.
int plot2scale = 20;
int plot3scale = 5; //20;

// position plot parameters
int posPlotXorig = 0;
int posPlotYorig = 0;
int posPlotWidth = 0;
int posPlotHeight = 0;

int mouseXpos = 0;

/////////////  
import processing.serial.*;    // import the Processing serial library
PrintWriter output;    // initialize the PrintWriter Java object (don't know much about this)

Serial behavSerPort;    // the serial port for behavioral input

long time=0;    // initialize variable for the current time since program started
int timeSec = 0; // current time in sec
String event;  // initialize variable for serial data from Arduino

int h = 0; // variable for recording hour of start/stop
int m = 0; // variable for recording minute of start/stop
int n = 0; 

int i = 0;  // variable for incrementing event strings and times
int j = 0;  // variable for incrementing time bins
int eventType = 0;  // variable for event type number
int event1binCt = 0;
int event2binCt = 0;
int event3binCt = 0;
int event4binCt = 0;
int event5binCt = 0;

int binLick = 0;
int binTag = 0;
int binRew = 0;

long eventTime = 0;

//ArrayList eventArray;
//ArrayList eventTimeArray;

int xOffset = 30;
int yOffset = 20;

String extension = "";
String filename = "";

long sessionLength = sessionMinutes*60000;

String velTxt;
float velSum = 0;
float vel = 0;
String posTxt;
int pos = 0;
float relPos = 0;
//int rewBegPos = 0;
//int rewEndPos = 0;
// array to read in reward positions from arduino
int[] rewPosArr = new int[8]; //10];

int check = 1; // var for initial filname check (for overwrite)

//////////////////////////
void setup() 
{
  size(600, 800);  // plot window size
  smooth();
  
  checkFilename(); // exits program if .png (i.e. completed session) for this animal/filename already exists
  
  // Create a new file in the sketch directory ready for writing text
  extension = ".txt";
  filename = animal.concat(extension);
  output = createWriter(filename);
  // set up serial port
  println(Serial.list());
  behavSerPort = new Serial(this, serialPort, 115200); // Serial baud rate with wheel rotary enc. Arduino (must agree with Arduino Serial.begin(baudRate);)
  behavSerPort.bufferUntil('\n');
  
  // print out a bit of header info and draw axes
  
  // start time (PC)
  output.println(animal);
  h = hour();
  m = minute();
  output.println("START time");
  output.print(h);
  output.print(":");
  if (m<=9) {
   output.println("0"+m); 
  }
  else {
  output.println(m);
  }
  println("START time");
  print(h);
  print(":");
  println(m);
  behavSerPort.write("1\n"); // prompt behav arduino to print header (instead of restarting for Processing 4)

  // DRAW and label graph axes
  drawAxes();
  
}


////////////////////////////DRAW (like LOOP)
// executes for every frame updated on screen
void draw() {      //draw() can be empty, everything's in SerialEvent

  time = millis();    // see how long it's been since program started

  //////////////
  // this section computes bin totals for each event category
  if (time >= j*binsize) {    // at the end of each timebin
    plotBinTotals();
  }
  
  updatePosition();

  // if total time has elapsed, then write everything to file
  if (time >= sessionLength) {
    endSession();
  }
  
  if (time > timeSec*1000) { // update time text ea sec
      timeSec++;
      
      pushStyle(); // to isolate rect style
      rectMode(CORNERS);
      fill(200);
      noStroke();
      rect(500, 0, width, 40);
      popStyle(); // back to original style
      textSize(20); 
      fill(255);
      //stroke(255, 0, 0);
      text(timeSec + " sec", 500, 20);
      
    }
    
  
} // end void draw()

////////////////////////////////////
////// use serialEvent() because of intermittent Arduino data
void serialEvent(Serial behavSerPort) {  

  if (behavSerPort.available() > 0) {  // when serial data is sent from Arduino (when the animal does something)
    // read serial data of trigger times (since start of this script) from Arduino
    //inBuffer = new byte[14];  // don't need this because of following...
    event = behavSerPort.readStringUntil('\n');  // use readStringUntil() to make sure we get entire serial package
    // Write the Arduino data to a file
    output.print(event);  // write the output to .txt file as string (will just be number in text)
    print(event);  // print trigger times to this display
    
    // parse and plot things from incoming strings
    if (toPlot == 1) {
      if (int(event) == 0) {  // if this serial data is an event type
        parseString();
      } // end IF event is a string (prob not necessary now)    
    } // end IF to plot event data
    //      output.println(time);  // uncomment to also output Processing time
  }  // end IF for behavSerPort.available
}  // end loop for serial input/print object



/////////////////////////////////////
// draw the axes for plotting
void drawAxes() {
  // DRAW and label graph axes
    // quadrant lines for diff plots/panels
    line(0, height/4, width, height/4);
    line(0, height/2, width, height/2);
    line(0, 3*height/4, width, 3*height/4);

    line(xOffset, 30, xOffset, height/4-yOffset);  // top graph (plot 1) vertical axis line
    line(xOffset, height/4-20, width-30, height/4-yOffset);  // horizontal
    line(xOffset, height/4+30, xOffset, height/2-yOffset);  // plot 2 vertical axis
    line(xOffset, height/2-yOffset, width-30, height/2-yOffset); // horiz
    line(xOffset, height/2+30, xOffset, 3*height/4-yOffset);  // plot 3 vertical axis
    line(xOffset, 3*height/4-yOffset, width-30, 3*height/4-yOffset); 
    
    fill(0);
    textSize(14);
    // Plot labels
    String plot1title = "Licks";
    String plot2title = "Laps";
    String plot3title = "Rewards";
    String plot4title = "Position";

    text(plot1title, 20, 20);
    text(plot2title, 20, height/4+20);
    text(plot3title, 20, height/2+20);
    text(plot4title, 20, 3*height/4 + 20); 

    textSize(20);
    text("file: " + animal, width/2-120, 20);
    textSize(10);
    text("(click window and press 'q' to quit/save)", width/2-80, 35);
    //fill(0);
    
    //////////////////////////
    textSize(12);
    // Plot1 (from top)
    text("0", 5, height/4-20);
    text(Integer.toString(20/plot1scale), 5, height/4-40);
    text(Integer.toString(40/plot1scale), 5, height/4-60);
    text(Integer.toString(60/plot1scale), 5, height/4-80);
    text(Integer.toString(80/plot1scale), 5, height/4-100);
    text(Integer.toString(100/plot1scale), 5, height/4-120);
    text(Integer.toString(120/plot1scale), 5, height/4-140);
    
    // Plot2
    text("0", 5, height/2-20);
    text(Integer.toString(20/plot2scale), 5, height/2-40); // "20" // these vales div by plot2scale
    text(Integer.toString(40/plot2scale), 5, height/2-60); // "40"
    text(Integer.toString(60/plot2scale), 5, height/2-80); // "60"
    text(Integer.toString(80/plot2scale), 5, height/2-100); // "80"
    text(Integer.toString(100/plot2scale), 5, height/2-120); // "100"
    text(Integer.toString(120/plot2scale), 5, height/2-140); // "120"
    
    // Plot3
    text("0", 5, 3*height/4-20);
    text(Integer.toString(20/plot3scale), 5, 3*height/4-40); // "20"
    text(Integer.toString(40/plot3scale), 5, 3*height/4-60); // "40"
    text(Integer.toString(60/plot3scale), 5, 3*height/4-80); // "60"
    text(Integer.toString(80/plot3scale), 5, 3*height/4-100); // "80"
    text(Integer.toString(100/plot3scale), 5, 3*height/4-120); // "100"
    text(Integer.toString(120/plot3scale), 5, 3*height/4-140); // "120"
    
    // Plot4
    // Draw track plot
    
    posPlotXorig = 30;
    posPlotYorig = 3*height/4+50;
    posPlotWidth = width-60;
    posPlotHeight = 60;


}

/////////////////////////////
void plotBinTotals() {
  
    if (event2binCt != 0) {    // lick
      binLick = event2binCt;
    } 
    else {binLick = 0;}

    if (event3binCt != 0) {  // tag
      binTag = event3binCt;
    } 
    else {binTag = 0;}
    
    if (event4binCt != 0) {    // reward
      binRew = event4binCt;
    } 
    else {binRew = 0;}

    // display the data for the past bin
   
    // make bar with rect(xpos, ypos, xVal, yVal)
    // NOTE: CORNERS mode for rect format: rect(topleftX, topleftY, botrightX, botrightY)
    rectMode(CORNERS);
    fill(200);
    rect(j*10+xOffset, (height/4)-(binLick*plot1scale)-yOffset, (j*10)+xOffset+10, height/4-yOffset);  // plot 1 (top)
    fill(255);
    rect(j*10+xOffset, (height/2)-(binTag*plot2scale)-yOffset, (j*10)+xOffset+10, height/2-yOffset);  // plot 2
    fill(122);
    rect((j*10)+xOffset, (3*height/4)-(binRew*plot3scale)-yOffset, (j*10)+xOffset+10, 3*height/4-yOffset );  // plot 3

    // then reset all bin counts
    event1binCt = 0;
    event2binCt = 0; 
    event3binCt = 0;
    event4binCt = 0;
    event5binCt = 0;

    j = j+1;    // increment the time bin number 
}

////////////////////////////////////
void parseString() {
  //String eventType = event;
  i = i + 1;  // count the events
  //eventArray.add(event);  // make an array list of all event strings
  
  String event1string = "vel=";
  String event2string = "lick";
  String event3string = "lap";
  String event4string = "REWARD";
  String event5string = "length=";
  //String event6string = "rewBegPos=";
  //String event7string = "rewEndPos=";
  String event8string = "rewPosArr=";
  

  if (event.contains(event1string)) {  // see what type of event
    eventType = 1;
    //println("break");
    event1binCt = event1binCt + 1;  // and count events in this bin
    
    // extract velocity
    int ind1 = event.indexOf("vel=");
    int ind2 = event.indexOf("currPos");  // string at end of "vel" number
    velTxt = event.substring(ind1+4,ind2-2);
    //println(velTxt);

    // convert to number
    vel = float(velTxt);
    // add to vel array for this timebin
    velSum = velSum + vel;
     
    // extract position
    int ind3 = event.indexOf("ms");
    posTxt = event.substring(ind2+8, ind3-2);
    pos = int(posTxt);
    
    // update position graph
    if (pos>=0) {
    relPos = float(pos)/trackLen;
    }
    else {
     relPos = float(trackLen+pos)/trackLen; 
    }
    
  } 
  else if(event.contains(event2string)) {  // lick
    eventType = 2; 
    event2binCt = event2binCt + 1;
  } 
  else if(event.contains( event3string)) {  // tag
    eventType = 3; 
    event3binCt = event3binCt + 1;
  } 
  else if(event.contains(event4string)) {  // reward
    eventType = 4;
    event4binCt = event4binCt + 1;
  } 
  else if(event.contains(event5string)) {  // track length
    int evLen = event5string.length();//println(evLen);
    int evInd = event.indexOf(event5string);//println(evInd);
    String evTxt = event.substring(evInd+evLen, event.length()-2);println(evTxt); //println(evTxt.indexOf("7"));
    trackLen = int(evTxt);
    println("trackLength = " + trackLen);
  } // end ELSE for event type
  //else if(event.contains(event6string)) {  // rewBegPos
  //  //int evLen = event6string.length();
  //  //int evInd = event.indexOf(event6string);
  //  //String evTxt = event.substring(evInd+evLen, event.length()-2);
  //  //rewBegPos = int(evTxt);
  //} // end ELSE for event type
  //else if(event.contains(event7string)) {  // rewEndPos
  //  int evLen = event7string.length();//println(evLen);
  //  int evInd = event.indexOf(event7string);//println(evInd);
  //  String evTxt = event.substring(evInd+evLen, event.length()-2);//println(evTxt);
  //  rewEndPos = int(evTxt);
  //} // end ELSE for event type
  else if(event.contains(event8string)) {  // rewPosArr = {500, 1000, 2000}
    int evLen = event8string.length();//println(evLen);
    int evInd = event.indexOf(event8string);//println(evInd);
    String evTxt = event.substring(evInd+evLen+1, event.length()-3);//println(evTxt);
    //rewPosArr = int(evTxt);
    // evTxt should look like 500, 1000, 2000
    updateRewPos(evTxt);
    print(evTxt);
  } // end ELSE for event type
} // end parseString();

// this just parses the rewPosArr string and updates the reward positions on track
void updateRewPos(String evTxt) { 
  // evTxt should now look like long, long, ....
  String[] rewArrStr = splitTokens(evTxt, ", ");
  //int numRew = rewArrStr.length;
  for (int i=0; i<rewArrStr.length; i++) {
    rewPosArr[i] = int(rewArrStr[i]); 
  }
  
}

/////////////////////////////
void updatePosition() {
  
  // redraw track to clear each frame
  rectMode(CORNER);
  fill(255, 100);
  //posPlotXorig = 30;
  //posPlotYorig = 3*height/4+50;
  //posPlotWidth = width-60;
  //posPlotHeight = 60;
  rect(30, 3*height/4+50, width-60, 60); 
  
  rectMode(CORNERS);
  fill(200);
  
  // 012719: now plot all reward zones in array
  for (int i=0; i<rewPosArr.length; i++) {
    if (rewPosArr[i]!=0) {
    int rewXbeg = round(float(rewPosArr[i])/trackLen*(posPlotWidth)+posPlotXorig);
    int rewXend = round(float(rewPosArr[i]+rewWidth)/trackLen*(posPlotWidth)+posPlotXorig);
    rect(rewXbeg, posPlotYorig, rewXend, posPlotYorig+60);
    }
  }
  
  mouseXpos = round(relPos*float(posPlotWidth-30)+posPlotXorig);
  //println(relPos);
  //println(mouseXpos);
  rectMode(CORNER);
  fill(100);
  rect(mouseXpos, posPlotYorig, 20, 60);
  
}

//////////////////////
// check sessName with previous files in data dir to keep from copying over

void checkFilename() {
   String path = sketchPath();
   File file = new File(path);// + "/data");
   String names[]=file.list();
   //printArray(names);
   String dataFilename = animal + ".png"; // only checks for completed session with .png plot image file
   //println(dataFilename);
   for (int i=0;i<names.length;i++) {
     String thisFilename = names[i];
     if (thisFilename.equals(dataFilename)== true) {
       println("Session name " + animal + " repeated, so aborting to avoid copying over previous.");
       exit(); 
       //check = 0;
       //return check;
     }
   }
 
}

///// ends program and saves output TXT (and graph)  
void keyPressed() {
  if (key=='q') {
  endSession();
  }
}  // end keyPressed


/////////////////////////////
void endSession() {
  h = hour();
  m = minute();
  output.println("END SESSION");
  output.print(h);
  output.print(":");
  if (m<=9) {
   output.println("0"+m); 
  }
  else {
  output.println(m);
  } 
  
  output.flush(); // Write the remaining data
  output.close(); // Finish the file
  println("END SESSION");
  
  extension = ".png";
  filename = animal.concat(extension);
  saveFrame(filename);  // added 121010 to save graph  
  exit(); // Stop the program
  //  }  // end ELSE for writing end of file
  
}