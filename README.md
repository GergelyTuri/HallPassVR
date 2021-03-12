# mouseVR
virtual reality environment for mice

This project aims to support neuroscientist explore mice brain cells working when it running in the virtual reality environment. The main part for this project is designing a system which can synchronize the mice movement to the virtual corridor with low latency. The prototype virtual corridor has been done with basic functions. The most recent demo videos can be found here: https://drive.google.com/drive/u/2/folders/1Ucv_41gNv25MAfak_pyqquLuZ15v62hw 

Hardware: 1) Arduino: Tracking and converting mice movement on treadmill to serial data. 
          2) Raspberry Pi 3B: Building and simulating the virtual reality environment. 
          3) DLPDLCR2010EVM: Projector

Software: 1) Python: Used for designing the corridor. The mainly used language for the Project is python 
          2) Linux: 

How to setup and run the demo: 1) Download and intall the python file Silo1023.py under pi3d_demo. Run command: python3 Silo1023.py on the terminal under the pi3d_demo 
